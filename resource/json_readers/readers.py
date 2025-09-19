import json

def get_love_interest():
    with open('resource/messages/love_interests.json', 'r') as file:
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
