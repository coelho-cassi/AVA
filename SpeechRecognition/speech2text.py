from os import path
from pydub import AudioSegment
import speech_recognition as sr

src = (r"C:\Users\Jacob\OneDrive\Documents\GitHub\AVA\SpeechRecognition\DontStopBelievingSong.mp3")
sound = AudioSegment.from_mp3(src)
sound.export(r"C:\Users\Jacob\OneDrive\Documents\GitHub\AVA\SpeechRecognition\song.wav", format="wav")
file_audio = sr.AudioFile(r"C:\Users\Jacob\OneDrive\Documents\GitHub\AVA\SpeechRecognition\song.wav")

r = sr.Recognizer()
with file_audio as source:
    audio_text = r.record(source)

print(type(audio_text))