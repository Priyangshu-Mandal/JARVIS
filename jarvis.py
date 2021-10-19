import time

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pygame


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """
    :param audio: any text
    'speaks' the given text
    """

    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    Wishes the user according to the current time
    """

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. Please tell me how may I help you.")


def takeCommand():
    """
    :return: the string form of the audio user input
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:    # input from microphone is stored in source
        print("Listening...")
        r.pause_threshold = 1    # seconds of non-speaking
        r.energy_threshold = 400    # you will have to shout!
        audio = r.listen(source)    # 'listens' to source and stores the string in audio

    try:
        print("Recognizing...")
        userInput = r.recognize_google(audio, language='en-in')    # recognize audio in Indian English using google engine
        print(f"User said: {userInput}\n")

    except Exception:
        print("Say that again please...\n")
        speak("Say that again please...\n")
        return "None"

    return userInput


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # LOGIC FOR EXECUTING TASKS BASED ON QUERY

        # wikipedia search
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            print("According to Wikipedia, " + results + "\n")
            speak("According to Wikipedia, " + results)

        # opening YouTube
        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open('youtube.com')

        # opening Google
        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open('google.com')

        # opening CodeWithHarry.com
        elif "open codewithharry.com" in query:
            speak("Opening CodeWithHarry.com...")
            webbrowser.open('codewithharry.com')

        # opening Java docs
        elif "open java docs" in query:
            speak("Opening Java Documentation...")
            webbrowser.open('docs.oracle.com//en//java//javase//14//docs//api//')

        # asking, "who are you?"
        elif "who are you" in query:
            speak("I am Jarvis")

        # playing music
        elif "play music" in query:
            speak("Playing music...")
            music_dir = 'C:\\Users\\Mrinmoy\\Music\\Music'
            songs = os.listdir(music_dir)
            for i, song in enumerate(songs):
                print(str(i) + ")  " + song + "\n")
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        # asking the time
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time: {strTime}")
            speak(f"The time is {strTime}")

        # opening Visual Studio Code
        elif "open code" in query:
            speak("Opening Visual Studio Code...")
            codePath = "F:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # opening IntelliJ IDEA
        elif "open idea" in query:
            speak("Opening IntelliJ IDEA...")
            codePath = "F:\\IntelliJ IDEA 2020.3.1\\IntelliJ IDEA Community Edition 2020.3.1\\bin\\idea64.exe"
            os.startfile(codePath)

        # opening PyCharm
        elif "open pycharm" in query:
            speak("Opening PyCharm...")
            codePath = "F:\\Pycharm 2020.3.2\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        # opening Google Chrome
        elif "open chrome" in query:
            speak("Opening Google Chrome...")
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        # opening the flappy bird game
        elif "open flappy bird game" in query:
            codePath = "F:\\Flappy Bird Game\\Try\\Try.exe"
            os.startfile(codePath)

        # opening powershell
        elif "open powershell" in query:
            codePath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
            os.startfile(codePath)

        # switching Jarvis off
        elif "jarvis quit" in query:
            speak("Quitting. Hope I was of help.")
            quit()
