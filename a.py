!pip install SpeechRecognition
import speech_recognition as sr
r = sr.Recognizer()
# For microphone input
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# For audio file input
audio = sr.AudioFile('path_to_audio_file.wav')
with audio as source:
    audio = r.record(source)
try:
    # Recognize the speech using the default Google Speech Recognition API
    text = r.recognize_google(audio)
    print("Text: " + text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error: {0}".format(e))


