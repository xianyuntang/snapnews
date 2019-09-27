from django.shortcuts import render
from django.utils import dateparse
from django.http import Http404
from snapnews.models import Record
from setting.models import Channel
from django.contrib.auth.decorators import login_required
import datetime


# Create your templates here.

@login_required
def index(request):
    if request.method == 'GET':
        response = render(request, 'snapnews/index.html')
        latest_news = int(Record.objects.last().id) - 1
        response.set_cookie('latest_news', latest_news)
        return response
    else:
        return Http404


@login_required
def search(request):
    if request.method == 'GET':

        keyword = request.GET.get('keyword')
        start = request.GET.get('start')
        start = dateparse.parse_datetime('{} 21:00:00'.format(start)) - datetime.timedelta(days=1)
        end = request.GET.get('end')
        end = dateparse.parse_datetime('{} 21:00:00'.format(end))
        channel_object = Channel.objects.values_list('name', flat=True)
        channel = []
        for i in range(len(channel_object)):
            record_object = Record.objects.filter(time__range=(start, end), keyword=keyword,
                                                  channel=channel_object[i],user=request.user)
            if len(record_object) != 0:
                channel.append(channel_object[i])
        response = render(request, 'snapnews/search.html', context={'channels': channel})
        return response
    else:
        return Http404
