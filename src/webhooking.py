from prayer import send_today, send_tomorrow 
from dhooks import Webhook, Embed
from timings import fajr_to_dhuhr, dhuhr_to_asr, asr_to_maghrib, maghrib_to_isha, isha_to_fajr
from datetime import datetime
import asyncio

hook = Webhook('https://discord.com/api/webhooks/1155438123979898940/o0hqSiaOU-LDfldB12N2L4Lo3M24k3l-QSZzcc2Mvl3YrCF-xi9bdwbiOsn5r-49HG-b')
now = datetime.now().strftime("%H:%M")    

async def send_prayer_notification(prayer_name, prayer_time):
    embed = Embed(
        title = f"@_____11111 It is time for {prayer_name} at {prayer_time}",
        color= 0xac6969
    )
    hook.send(embed=embed)

async def check_prayer_times():
    while True:
        for prayer, time in send_today().items():
            if now == time and prayer == 'Fajr':
                await send_prayer_notification(prayer, time)
                await asyncio.sleep(fajr_to_dhuhr)
            elif now == time and prayer == 'Dhuhr':
                await send_prayer_notification(prayer, time)
                await asyncio.sleep(dhuhr_to_asr)
            elif now == time and prayer == 'Asr':
                await send_prayer_notification(prayer, time)
                await send_prayer_notification(asr_to_maghrib)
            elif now == time and prayer == 'Maghrib':
                await send_prayer_notification(prayer, time)
                await asyncio.sleep(maghrib_to_isha)
            elif now == time and prayer == 'Isha\'a':
                await send_prayer_notification(prayer, time)
                await asyncio.sleep(isha_to_fajr)
            else:
                await asyncio.sleep(60)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_prayer_times())
