import requests

url = 'https://dailyprayer.abdulrcs.repl.co/api/canberra'
r = requests.get(url)

today = r.json()['today']
tomorrow = r.json()['tomorrow']

prayer_times = {
    'Fajr'   : today['Fajr'],
    'Dhuhr'  : today['Dhuhr'],
    'Asr'    : today['Asr'],
    'Maghrib': today['Maghrib'],
    'Isha\'a': today['Isha\'a']
}

prayer_times_tomorrow = {
    'Fajr' : tomorrow['Fajr']
    # 'Dhuhr'  : tomorrow['Dhuhr'],
    # 'Asr'    : tomorrow['Asr'],
    # 'Maghrib': tomorrow['Maghrib'],
    # 'Isha\'a': tomorrow['Isha\'a']
}

def send_today():
    return prayer_times 

def send_tomorrow():
    return prayer_times_tomorrow

print(send_today(), send_tomorrow())