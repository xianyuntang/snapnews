from django.http import JsonResponse
from ..models import UserKeyword
from django.contrib.auth.decorators import login_required


@login_required
def add_keyword_group(request):
    if request.method == "POST":
        keyword_group = request.POST['keyword_group']
        if keyword_group:
            user_keyword = UserKeyword(user=request.user, keyword_group=keyword_group)
            user_keyword.save()
            return JsonResponse(None, safe=False)
        else:
            return JsonResponse(None, safe=False)


@login_required
def mod_keyword_group(request):
    if request.method == "POST":
        keyword_group_name = request.POST['keyword_group_name']
        keyword_group_id = request.POST['keyword_group_id']
        if keyword_group_name and keyword_group_id:
            user_keyword = UserKeyword.objects.get(id=keyword_group_id)
            user_keyword.keyword_group = keyword_group_name
            user_keyword.save()

        return JsonResponse(None, safe=False)


@login_required
def del_keyword_group(request):
    if request.method == "POST":
        keyword_group_id = request.POST['keyword_group_id']
        if keyword_group_id:
            user_keyword = UserKeyword.objects.get(id=keyword_group_id)
            user_keyword.delete()

        return JsonResponse(None, safe=False)


@login_required
def del_keyword(request):
    if request.method == "POST":
        keyword_group_id = request.POST['keyword_group_id']
        keyword = request.POST['keyword']
        print(keyword)
        keyword_type = request.POST['keyword_type']
        if keyword_group_id and keyword:
            if keyword_type == 'inclusive':
                user_keyword = UserKeyword.objects.get(id=keyword_group_id)
                user_keyword.keyword_included.remove(keyword)
                user_keyword.save()
            elif keyword_type == 'exclusive':
                user_keyword = UserKeyword.objects.get(id=keyword_group_id)
                user_keyword.keyword_excluded.remove(keyword)
                user_keyword.save()
        return JsonResponse(None, safe=False)


@login_required
def add_keyword(request):
    if request.method == "POST":
        keyword_group_id = request.POST['keyword_group_id']
        keyword = request.POST['keyword']
        keyword_type = request.POST['keyword_type']
        if keyword and keyword_group_id:
            if keyword_type == 'inclusive':
                user_keyword = UserKeyword.objects.get(id=keyword_group_id)
                user_keyword.keyword_included.append(keyword)
                user_keyword.save()
            elif keyword_type == 'exclusive':
                user_keyword = UserKeyword.objects.get(id=keyword_group_id)
                user_keyword.keyword_excluded.append(keyword)
                user_keyword.save()
        return JsonResponse(None, safe=False)
