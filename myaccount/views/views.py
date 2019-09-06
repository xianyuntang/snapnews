
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from ..forms import ProfileForm, KeywordForm
from ..models import UserProfile, UserKeyword


# Create your views here.


@login_required
def profile_update(request):
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

            return render(request, 'account/profile_update.html', {'form': form, 'user': user})
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'org': user_profile.org, 'telephone': user_profile.telephone,
                        'email_address': user_profile.email_address, 'line_api_key': user_profile.line_api_key}
        form = ProfileForm(default_data)

        return render(request, 'account/profile_update.html', {'form': form, 'user': user})


@login_required
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
