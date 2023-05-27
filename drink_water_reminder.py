from plyer import notification
import pyttsx3
import time
repeat_time=3600
while True:
    notification.notify(
    title = "Drink Water 🥤",
    message = "Mukul Drink Water Please",
    timeout = 10)

    engine = pyttsx3.init()
    engine.say("Mukul Drink Water Please")
    engine.runAndWait()
    time.sleep(repeat_time)