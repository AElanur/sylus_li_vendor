import json
import random
from requests.exceptions import SSLError

def get_timer_buttons():
    try:
        with open('resource/json/config.json', 'r', encoding="utf8") as file:
            data = json.load(file)
            return data['timer_buttons']
    except SSLError as ssl_err:
        print(f"SSL error: {ssl_err}")
        return None

def get_love_interest():
    with open('resource/json/messages/love_interests.json', 'r') as file:
        data = json.load(file)
    return data

def get_sylus_responses():
    with open('resource/messages/sylus_responses.json', 'r') as file:
        data = json.load(file)
    return data

def get_specific_li(name):
    data = get_love_interest()
    love_interest = next((item for item in data['love_interests'] if item['name'] == name), None)
    return love_interest

def get_sylus_response_upon_picking(name):
    data = get_sylus_responses()
    response_list = next((item for item in data['decision'] if name in item), None)
    response = random.choice(response_list[name])
    return response

def get_pomodoro_timers():
    try:
        with open('resource/json/config.json', 'r', encoding="utf8") as file:
            data = json.load(file)
        return data['pomodoro_timers']
    except SSLError as ssl_err:
        print(f"SSL error: {ssl_err}")
        return None
