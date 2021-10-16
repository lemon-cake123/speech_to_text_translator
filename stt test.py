import speech_recognition as sr
import sounddevice as sd
import numpy as np
import os
from scipy.io.wavfile import write
from googletrans import Translator, constants

translator = Translator()
to = input('enter the language code for the langguage you want to translate to')
lang = input('enter the language you are converting')
sd.default.dtype='int32', 'int32'

fs = 44100  # Sample rate
seconds = 15  # Duration of recording
print("Speak.....")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file in 16-bit format
recognizer = sr.Recognizer()
sound = "output.wav"

text = ''
with sr.AudioFile(sound) as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Converting to text...")
    audio = recognizer.listen(source,timeout=None)

    try:
        text = recognizer.recognize_google(audio,language = lang)
        print("The converted text: " + text)
    except sr.UnknownValueError:
        print('there is to much loud noise,please try again')

translation = translator.translate(text,dest=to,src=lang)
print(f'{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})')
