from prayer import send_today, send_tomorrow
from datetime import datetime, timedelta

FMT = "%H:%M"

fajr    = send_today()['Fajr']
dhuhr   = send_today()['Dhuhr']
asr     = send_today()['Asr']
maghrib = send_today()['Maghrib']
isha    = send_today()['Isha\'a'],
isha    = ''.join(isha)
fajr2   = send_tomorrow()['Fajr']

fajr_time    = datetime.strptime(fajr, FMT)
dhuhr_time   = datetime.strptime(dhuhr, FMT)
asr_time     = datetime.strptime(asr, FMT)
maghrib_time = datetime.strptime(maghrib, FMT)
isha_time    = datetime.strptime(isha, FMT)
fajr2_time   = datetime.strptime(fajr2, FMT)
fajr2_time   += timedelta(days=1)
    
def fajr_to_dhuhr():
    return (dhuhr_time - fajr_time).total_seconds()

def dhuhr_to_asr():
    return (asr_time - dhuhr_time).total_seconds()

def asr_to_maghrib():
    return (maghrib_time - asr_time).total_seconds()

def maghrib_to_isha():
    return (isha_time - maghrib_time).total_seconds()

def isha_to_fajr():
    return (fajr2_time - isha_time).total_seconds()
    # return (fajr2_time - isha_time).total_seconds()