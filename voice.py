from vosk import Model, KaldiRecognizer
import speech_recognition
import wave
import json
import os 
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
        with sr.Microphone() as source:
            recognized_data = ""

            listener.adjust_for_ambient_noise(source, duration=2)

            try:
                print("Listening...")
                audio = listener.listen(source, 5, 5)

            except speech_recognition.WaitTimeoutError:
                print("Can you check if your microphone is on, please?")
                return
            
            try:
                print("Started recognition...")
                recognized_data = listener.recognize_google(audio, language="ru").lower()

            except speech_recognition.UnknownValueError:
                pass

            except speech_recognition.RequestError:
                print("Trying to use offline recognition...")
                recognized_data = use_offline_recognition()

            return recognized_data

def use_offline_recognition():

    recognized_data = ""
    try:
        if not os.path.exists("models/vosk-model-small-ru-0.4"):
            print('¯\(°_o)/¯')
            exit(1)

        wave_audio_file = wave.open("microphone-results.wav", "rb")
        model = Model("models/vosk-model-small-ru-0.4")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
    except:
        print("Sorry, speech service is unavailable. Try again later")

    return recognized_data
