import os
import requests
import time
import json
from sensitive_data import data_list, x_super_properties, authorization

def transform_url(url):
    parts = url.split('/')
    new_url = '/'.join(parts[:3] + ['channels', '@me', parts[5]])
    return new_url

def fetch_data(name, link, before):
    limit = 100
    accept = "*/*"
    accept_language = "en-US,en;q=0.9,hi;q=0.8"
    referer = transform_url(link)
    se_ch_ua = "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\""
    se_ch_ua_mobile = "?0"
    se_ch_ua_platform = "\"Windows\""
    x_debug_options = "bugReporterEnabled"
    x_discord_locale = "en-GB"
    x_discord_timezone = "America/New_York"
    begin = 1
    continueFetching = True

    dir_path = f'D:\\Projects\\loldudeAI\\rawconversations\\discord\\{name}'
    os.makedirs(dir_path, exist_ok=True)

    headers = {
        "accept": accept,
        "accept-language": accept_language,
        "authorization": authorization,
        "referer": referer,
        "sec-ch-ua": se_ch_ua,
        "x-super-properties": x_super_properties,
        "sec-ch-ua-mobile": se_ch_ua_mobile,
        "sec-ch-ua-platform": se_ch_ua_platform,
        "x-debug-options": x_debug_options,
        "x-discord-locale": x_discord_locale,
        "x-discord-timezone": x_discord_timezone
    }

    while continueFetching:
        tempurl = link + "?before=" + before + "&limit=" + str(limit)
        response = requests.get(tempurl, headers=headers)
        file_path = os.path.join(dir_path, f'{begin}.txt')
        with open(file_path, 'w') as file:
            file.write(response.text)
        begin += 1
        data = json.loads(response.text)
        if len(data) < 50:
            continueFetching = False
        else:
            before = data[-1]['id']

        time.sleep(4)

for data in data_list:
    fetch_data(*data)
    time.sleep(10)
