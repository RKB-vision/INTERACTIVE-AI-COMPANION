import pyttsx3 as tts
import speech_recognition as sr
from speech_recognition.recognizers.google import UnknownValueError
import time

recognizer=sr.Recognizer()

engine=tts.init()
engine.setProperty('voice','com.apple.speech.synthesis.voice.alex')
engine.setProperty("rate",200)



def speak():
    with sr.Microphone() as source:
        audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio)
            print("You : ",text)
            return text
        except sr.UnknownValueError:
            print("Did not Understand what you said")
        except sr.RequestError as e:
            print("OH! could not properly communicate with google ",e)

engine.say("Hello! Welcome to the Project. Can I  know your name sir?")
engine.runAndWait()


time.sleep(2)
name = speak()
if name: # Check if 'name' is NOT None
    engine.say(f"Welcome {name.split()[0]}.Good to see you. Can I know your favourite color? ")
else:
    # Handle the failure gracefully, maybe ask again or skip the question
    engine.say("I didn't catch your name. Moving on. Can I know your favourite color?")
engine.runAndWait()

time.sleep(2)
color = speak()
if color:
    engine.say(f"{color} is a beautiful color!.Thank you for coming here. Goodbye!")
else:
    engine.say("I didn't catch your color. Thank you for coming here. Goodbye!")

engine.runAndWait()
