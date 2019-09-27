from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from ..forms import ProfileForm, KeywordForm
from ..models import UserProfile, UserKeyword
import requests
import json


# Create your views here.


@login_required
def profile(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user_profile.line_api_key = form.cleaned_data['line_api_key']
            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()

            return render(request, 'account/profile.html', {'form': form, 'user': user})
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'org': user_profile.org, 'telephone': user_profile.telephone,
                        'email_address': user_profile.email_address, 'line_api_key': user_profile.line_api_key}
        form = ProfileForm(default_data)

        return render(request, 'account/profile.html', {'form': form, 'user': user})


@login_required
@transaction.atomic
def keyword(request):
    user = request.user
    user_keyword = UserKeyword.objects.filter(user=user).order_by('id')
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            user_keyword.delete()
            for k in form.cleaned_data['keyword_list'].split('\n'):
                if k:
                    user_keyword = UserKeyword(user=user, keyword=k.strip())
                    user_keyword.save()
        render(request, 'account/keyword.html', {'user': user, 'form': form})

    else:
        keyword_list = [k.keyword for k in user_keyword]
        default_data = {'keyword_list': '\n'.join(keyword_list)}
        form = KeywordForm(default_data)
    return render(request, 'account/keyword.html', {'user': user, 'form': form})


@login_required
def update_line_api_key(request):
    if request.method == 'GET':
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        params = {
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://snapnews.cdc.gov.tw/account/profile/update_line_api_key/',
            'client_id': 'xBhzCgHqqkrUmxffRZvgsi',
            'client_secret': 'YfUqRIbpiGbp8fsiXBHZQKHoibmV5sirfVDl3s11q71',
            'code': request.GET['code']
        }
        r = requests.post('https://notify-bot.line.me/oauth/token', params=params)
        r = json.loads(r.content)
        user_profile.line_api_key = r['access_token']
        user_profile.save()
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'org': user_profile.org, 'telephone': user_profile.telephone,
                        'email_address': user_profile.email_address, 'line_api_key': user_profile.line_api_key}
        form = ProfileForm(default_data)

        return render(request, 'account/profile.html', {'form': form, 'user': user})
