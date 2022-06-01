import sys
print(sys.path)

import speech_recognition as sr
import pyttsx3

try:

    engine = pyttsx3.init()
except Exception as e:
    print("hello2")
    print(e)
except ImportError:
    print("hello3")
    print("Driver not found")
except RuntimeError:
    print("hello4")
    print("Driver fails to init")

voices = engine.getProperty("voices")

for voice in voices:
    print("hello1")
    print(voice.id)