import webbrowser
from search_googol import *
import speech_recognition
import os
from gtts import gTTS
from playsound import playsound




# webbrowser.open('https://habr.com/ru/post/470938/', new=2) #открывает ссылку


def greeting():
    return "You will die"
def telegram():
    os.startfile(r"C:\Users\nout.pssel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram")
def lisener():
    try:
        sr = speech_recognition.Recognizer()
        sr.pause_threshold = 0.5
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print(query)
            return query
    except:
        return lisener()
# s = gTTS(query)
# s.save("test.mp3")
# playsound('test.mp3')
def main(query):
    query=str(query)
    print(query)
    if "привет" in query:
        print(greeting())
    if "запусти telegram" in query:
        print(telegram())
    if "что такое" or "кто такой" or "кто такая" in query:
        s = gTTS(search_google(query))
        s.save("ansver.mp3")
        playsound("ansver.mp3")

    else:
        print("Хз что тебе надо")


if __name__ == "__main__":
    main(lisener())