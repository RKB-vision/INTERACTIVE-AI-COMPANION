# import pyttsx3 as tts
import speech_recognition as sr

recognizer=sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(audio)
        print("You: "+text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



