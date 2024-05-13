from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minute_left:02d}:{seconds_left:02d}")

    playsound("mixkit-classic-alarm-995.wav")


minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)
