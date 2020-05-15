import speech_recognition as sr

def listen_to_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        return command

    except sr.UnknownValueError:
        print('Your command couldn\'t be heard')
