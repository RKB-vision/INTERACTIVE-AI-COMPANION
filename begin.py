import pyttsx3 as tts

engine=tts.init()
engine.setProperty('voice','com.apple.speech.synthesis.voice.Lekha')
engine.setProperty('rate',150)
engine.setProperty('volume',0.5)

engine.say(input("What would you like me to say? "))

engine.runAndWait()
