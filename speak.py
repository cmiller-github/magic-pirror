import pyttsx
import pyaudio

speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

p = pyaudio.PyAudio()

def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

speak("Hi hi hi lori")