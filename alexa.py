import speech_recognition as sr
import pyttsx3          #to convert text to speech
import pywhatkit        #to open youtube songs
import datetime         #to tell current timing
import wikipedia        #for wiki to direct search of any people
import pyjokes          #for jokes section

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')

        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)



    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person , 5)
        print(info)
        talk(info)



    elif 'date' in command:
        talk('ok i would love to go with you baby')
    elif'are you single'in command:
        talk('I am in a relationship with google')
    elif'joke' in command:
        talk(pyjokes.get_joke())




while True:
    run_alexa()



