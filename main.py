# Hey Jasmine
# We import speech recognition module to recognize our voice
# We import Python text to speech module to talk to us

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
jasmine_audio = pyttsx3.init()    # Initializing the jasmine audio
voices = jasmine_audio.getProperty("voices")
jasmine_audio.setProperty("voice", voices[1].id)
jasmine_audio.say("Hello Sir my name is Jasmine! I am at your service. How can I help You!")
jasmine_audio.runAndWait()

def talk(text):
    jasmine_audio.say(text)
    jasmine_audio.runAndWait()


def take_command():
    try:

        with sr.Microphone() as our_audio:
            print("Listening...")
            voice = listener.listen(our_audio)
            audio_text = listener.recognize_google(voice)
            audio_text = audio_text.lower()
            if "jasmine" in audio_text:
                audio_text = audio_text.replace("jasmine", "")
                print("0" + audio_text)


    except:
        pass

    return audio_text


def run_jasmine():
    command = take_command()
    print("1" + command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I %M %p")
        print(time)
        talk("Current time is " + time)
    elif "search about" in command:
        search_text = command.replace("search about", "")
        print("2" + search_text)
        talk("Opening" + search_text)
        pywhatkit.search(search_text)
    elif "wikipedia" in command:
        wikipedia_text = command.replace("wikipedia", "")
        print(wikipedia_text)
        info = wikipedia.summary(wikipedia_text, 1)
        print(info)
        talk(info)
    else:
        talk("Sorry can you repeat!")


a = False
while not a:
    input_command = take_command()
    if "stop running" in input_command:
        a = True
    else:
        run_jasmine()