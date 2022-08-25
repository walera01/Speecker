import webbrowser

import speech_recognition
import os


sr =speech_recognition.Recognizer()
sr.pause_threshold = 0.5

webbrowser.open('https://habr.com/ru/post/470938/', new=2)

def greeting():
    return "You will die"
def telegram():
    os.startfile(r"C:\Users\nout.pssel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram")

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()


print(query)
if "привет" in query:
    print(greeting())
else:
    print("Хз что тебе надо")

if "запусти telegram" in query:
    print(telegram())


