import pyttsx3 as tts
import speech_recognition as sr
from speech_recognition.recognizers.google import UnknownValueError
import time
from aichat import chat
import sys

def speak():
    with sr.Microphone() as source:
        audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio)
            print("You : ",text)
            return text
        except sr.UnknownValueError:
            print("Did not Understand what you said")
            return None
        except sr.RequestError as e:
            print("OH! could not properly communicate with google ",e)
            return None

recognizer=sr.Recognizer()

engine=tts.init()
engine.setProperty('voice','com.apple.speech.synthesis.voice.alex')
engine.setProperty("rate",200)

engine.say("Hello! Welcome to the Project. Can I  know your name sir?")
engine.runAndWait()

name = speak()
if name: # Check if 'name' is NOT None
    engine.say(f"Welcome {name.split()[0]}.Good to see you. Tell me what you want to know ")
    engine.runAndWait()

else:
    # Handle the failure gracefully, maybe ask again or skip the question
    engine.say("I didn't catch your name. Moving on.")
    engine.runAndWait()

while True:
    engine.say("Anything else you want to know?")
    engine.runAndWait()
    prompt = speak()

    if not prompt:
        engine.say("I didn't get your prompt. If you want to exit, type exit or type the prompt")
        engine.runAndWait()
        prompt = input("Enter your prompt: ").strip()

    if prompt.lower() == "exit":
        engine.say("Goodbye!")
        engine.runAndWait()
        break

    response = chat(prompt)
    print("Chatbot Response:", response)
    engine.say(response)
    engine.runAndWait()
