import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            begine = pyttsx3.init()
            begine.say('Hello! I am Kira, and I am listening!')
            #begine.setProperty('rate',125)
            #begine.setProperty('voice', voices[0].id)
            begine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Kira' in command:
                command = command.replace('Kira', '')
                print(command)
            return command
    except:
        pass


def run_Kira():
    command = take_command()
    print(command)
    if command == None:
        talk('you haven not said anything. if you want me to stop say exit after hearing a joke! here is a joke!')
        talk(pyjokes.get_joke())
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    #elif 'exit' in command:
    #    break

    else:
        talk('Please say the command again.')


#while True:
#   run_Kira()
try:
    while True:
        run_Kira()
except KeyboardInterrupt:
        talk('Bye!!')
        pass
