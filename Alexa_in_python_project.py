# import libraries -- Speech recognition -- pip install SpeechRecognition
# import libraries -- pyaudio -- pip install PyAudio
# import libraries -- pyttsx3 -- pip install pyttsx3
# import libraries -- pywhatkit -- pip install pywhatkit
# import libraries -- wikipedia -- pip install wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("What can I do for you?")

def alexa_command():
    command = ""

    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()

            if "alexa" in command:
                command = command.replace("alexa", "")
                print("Command:", command)

    except Exception as e:
        print("Error:", e)

    return command

def run_alexa():
    command = alexa_command()

    if command == "":
        return

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time is " + time)

    elif "superstar" in command:
        person = command.replace("superstar", "").strip()

        if person == "":
            talk("Please tell me which superstar?")
            return

        try:
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        except:
            talk("Sorry, I could not find this person")

run_alexa()
