import base64
import json
from django.conf import settings


def channel_to_str(channel):
    channel_dict = {
        "30": "華視",
        "53": "台視",
        "54": "壹新聞",
        "55": "中視",
        "56": "公視",
        "57": "中天新聞",
        "58": "NHK",
        "59": "三立新聞",
        "61": "BBC",
        "62": "民視",
        "63": "東森新聞",
        "64": "年代新聞",
        "65": "TVBS新聞",
        "66": "CNN",
        "67": "CCTV",
        "68": "鳳凰衛視"
    }

    return channel_dict.get(channel)


def str_to_channel(channel):
    channel_dict = {
        "華視": 30,
        "台視": 53,
        "壹新聞": 54,
        "中視": 55,
        "公視": 56,
        "中天新聞": 57,
        "NHK": 58,
        "三立新聞": 59,
        "BBC": 61,
        "民視": 62,
        "東森新聞": 63,
        "年代新聞": 64,
        "TVBS新聞": 65,
        "CNN": 66,
        "CCTV": 67,
        "鳳凰衛視": 68
    }

    return channel_dict.get(channel)


def load_and_encode_image(image_name):
    with open(f'{settings.IMAGE_LOC}{image_name}', 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('ascii')

        return f'data:image/jpg;base64,{image_base64}'


def write_system_config(system_config):
    with open('./news/static/system/system.json', 'w', encoding='utf-8') as f:
        json.dump(system_config, f)


def count_freq(array):
    mp = dict()
    for i in array:
        if i in mp.keys():
            mp[i] += 1
        else:
            mp[i] = 1


    return mp
