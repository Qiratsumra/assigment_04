import time

def count_down_timer(seconds):
    while seconds > 0:
        hours, remainder = divmod(seconds, 3600)  # calculation of hours and remainder
        mins, sec = divmod(remainder, 60)  # calculation of minutes and seconds
        time_formate = '{:02d}:{:02d}:{:02d}'.format(hours, mins, sec)
        print(time_formate, end='\r')
        time.sleep(1)  # delay of seconds
        seconds -= 1
    print("00:00 \n Time's up!🎉")


totalSeconds = int(input('Enter time second for countdown: '))
count_down_timer(totalSeconds)