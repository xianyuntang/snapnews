from django.shortcuts import render
from ..utils import load_system_config
# Create your views here.


# 設定
def setting(request):
    if request.method == 'GET':
        return render(request, 'setting/setting.html')


