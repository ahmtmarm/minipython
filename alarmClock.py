#pip install playsound
from playsound import playsound
import time

#Clear ve Clear and return adlı iki sabit terminal ekranını temizlemek
#ve imleci başlangıç pozisyonuna döndürmek için kullanılacaktır.
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\003[H"

#Bu fonksiyon geri sayım yapar ve süre sonunda bir alarm çalar.
def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"\r{CLEAR_AND_RETURN}Alarm will sound in{minutes_left:02d}:{seconds_left:02d}", end="")
    playsound("alarm.mp3")

#Kullanıcıdan kaç dakika ve kaç saniye beklemek istediğini öğreniyoruz ve kaydediyoruz.
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
#Dakikayı saniyeye çeviriyoruz
total_seconds = minutes * 60 + seconds
alarm(total_seconds)

