from django.utils import dateparse
from django.http import JsonResponse, Http404
from snapnews.models import Record
from snapnews.utils import channel_to_str
from snapnews.utils import load_and_encode_image
from snapnews.utils import count_freq
import datetime


# ajax views

# 全部關鍵字文字雲
def get_generate_word_cloud(request):
    if request.method == 'GET':
        data = Record.objects.filter(user_id=request.user).values_list('keyword', flat=True)
        data = count_freq(data)
        return JsonResponse(data, safe=False)
    else:
        return Http404


# 當日關鍵字文字雲

def get_generate_word_cloud_today_only(request):
    if request.method == 'GET':
        start = datetime.datetime.today().date()
        end = start + datetime.timedelta(1)
        data = Record.objects.filter(user_id=request.user, time__range=(start, end)).values_list('keyword', flat=True)
        data = count_freq(data)
        return JsonResponse(data, safe=False)
    else:
        return Http404


def load_snapshot(request):
    if request.method == 'GET':
        channel = request.GET.get('channel')
        keyword = request.GET.get('keyword')
        start = request.GET.get('start')
        start = dateparse.parse_datetime('{} 13:00:00'.format(start)) - datetime.timedelta(days=1)
        end = request.GET.get('end')
        end = dateparse.parse_datetime('{} 13:00:00'.format(end))
        page_num = int(request.GET.get('page_num'))
        __image_per_page = 10
        page_slices = (page_num * __image_per_page, (page_num + 1) * __image_per_page)
        data = list(
            Record.objects.filter(time__range=(start, end),
                                  channel=channel,
                                  keyword=keyword).order_by('id').values()[page_slices[0]:page_slices[1]])
        for i in range(len(data)):
            data[i]['image'] = load_and_encode_image(data[i]['image'])
            data[i]['channel'] = channel_to_str(data[i]['channel'])

        return JsonResponse(data, safe=False)


def load_single_snapshot(request):
    if request.method == 'GET':
        idx = request.GET.get('idx')
        data = list(Record.objects.filter(id=idx).all().values())
        for i in range(len(data)):
            data[i]['image'] = load_and_encode_image(data[i]['image'])
            data[i]['channel'] = channel_to_str(data[i]['channel'])
        return JsonResponse(data, safe=False)
