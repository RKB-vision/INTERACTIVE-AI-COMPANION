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
            print("You :",text)
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

engine.say("Hello! Welcome to the Project. I am your virtual assistant.")
engine.runAndWait()
time.sleep(1)
count=0
while True:
    count+=1
    if count==1:
        engine.say("What question do you have?")
        engine.runAndWait()
    else:
        engine.say("Anything else?")
        engine.runAndWait()
    time.sleep(3)
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
    time.sleep(10)

print(f"Exiting the program.Bravo! You gave {count} prompts.")
