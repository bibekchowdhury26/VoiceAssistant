import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia , pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(text):
    try:
        with sr.Microphone() as source:
            talk(text)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        pass
    
state = True   
    

def run_VoiceAssistance():
    global state
    command = take_command('What can I do for you?')

    if not command:
        talk('are you there')
        run_VoiceAssistance()

    elif 'play' in command:
        song = command.replace('play','')
        talk("Playing" + song + "on youtube")
        pywhatkit.playonyt(song)
    
    elif 'call mom' in command:
        talk('rita. rita. rita. rita')

    elif 'create a file' in command:
        exten = take_command('what kind of file')
        if exten == 'text file':
            exten = 'txt'
        name = take_command('what should be the name of this file ').replace(" ","")
        f = open("{}.{}".format(name,exten),"wb")
        print("{}.{}".format(name,exten))
        content = take_command('whats the content').encode("utf8")
        print(content)
        f.write(content)
        f.close()
        talk('file saved successfully')

    elif 'send' in command and 'message' in command:
        number ="+91" + take_command('please tell the phone number').replace(' ','')
        print(number)
        message = take_command('and whats the meassage')
        print(message)
        tts = datetime.datetime.now().strftime('%H:%M')
        pywhatkit.sendwhatmsg(number,message,int(tts[:2]),int(tts[3:])+2)
        talk('Message successfully sent')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'what' in command or 'who' in command or 'how' in command:
        search = command.replace('what', '')
        search = command.replace('who', '')
        search = command.replace('how', '')
        info = wikipedia.summary(search, 1)
        talk(info)

    elif 'search' in command or 'google' in command:
        search = command.replace('search','')
        search = command.replace('google', '')
        search = command.replace('in', '')
        pywhatkit.search(search)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif command == 'thank you':
        talk('Happy to help you my friend')

    elif 'goodbye' in command or 'get lost' in command:
        talk('okay bye bye. Talk to you later')
        state = False

    else:
        talk('Can you be more specific')
    
        
while state:
    run_VoiceAssistance()
    
