import json


def load_system_config():
    with open('./static/system/system.json', 'r', encoding='utf-8') as f:
        system_config = json.load(f)
    return system_config['channel'], system_config['database'], system_config['line']
