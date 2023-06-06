import speech_recognition as sr

r = sr.Recognizer()

audio_file = 'test.wav'

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

text = r.recognize_google(audio, language='zh-CN')
# text = r.recognize_sphinx(audio, language='zh-CN')

print(text)