import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Johnson. Please tell me how may I help you?")

def takeCommand():
    # It takes Microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("I didn't Get That, Say that again please...")
        speak("I didn't Get That, Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            print("Opening YouTube...")
            webbrowser.open_new("https://www.youtube.com")

        elif 'open my school' in query:
            speak("Opening Sainik School Purulia...")
            print("Opening Sainik School Purulia...")
            webbrowser.open_new("http://sainikschoolpurulia.com")

        elif 'open google' in query:
            speak("Opening Google...")
            print("Opening Google...")
            webbrowser.open_new("https://www.google.com")

        elif 'open technology news' in query:
            speak("Opening Technology news...")
            print("Opening Technology news...")
            webbrowser.open_new("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")

        elif 'open gmail' in query:
            speak("Opening Gmail...")
            print("Opening Gmail...")
            webbrowser.open_new("https://gmail.com")

        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow...")
            print("Opening Stackoverflow...")
            webbrowser.open_new("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'YOUR MUSIC FOLDER'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing Music...")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")
            print(strTime)

        elif 'open visual studio' in query:
            visualstudiopath = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualstudiopath)
            speak("Opening Visual Studio Code...")
            print("Opening Visual Studio Code...")
        
        elif 'open chrome' in query:
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
            speak("Opening Google Chrome...")
            print("Opening Google Chrome...")

        elif 'open photoshop' in query:
            photoshoppath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(photoshoppath)
            speak("Opening Photoshop...")
            print("Opening Photoshop...")

        elif 'open powerpoint' in query:
            powerpointpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powerpointpath)
            speak("Opening PowerPoint...")
            print("Opening PowerPoint...")

        elif 'open firefox' in query:
            firefoxpath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefoxpath)
            speak("Opening Firefox...")
            print("Opening Firefox...")

        elif 'open vpn' in query:
            vpnpath = "C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe"
            os.startfile(vpnpath)
            speak("Opening Proton VPN...")
            print("Opening Proton VPN...")

        elif 'open settings' in query:
            settingspath = "C:\\WINDOWS\\System32\Control.exe"
            os.startfile(settingspath)
            speak("Opening Control Panel...")
            print("Opening Control Panel...")

        elif 'open file explorer' in query:
            explorerpath = "C:\\Windows\\explorer.exe"
            os.startfile(explorerpath)
            speak("Opening File Explorer...")
            print("Opening File Explorer...")

        elif 'open word' in query:
            wordpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordpath)
            speak("Opening Word...")
            print("Opening Word...")

        elif 'open filmora' in query:
            filmorapath = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
            os.startfile(filmorapath)
            speak("Opening Wondershare Filmora...")
            print("Opening Wondershare Filmora...")

        elif 'open scratch' in query:
            scratchpath = "C:\\Program Files (x86)\\Scratch Desktop\\Scratch Desktop.exe"
            os.startfile(scratchpath)
            speak("Opening Scratch...")
            print("Opening Scratch...")

        elif 'open emulator' in query:
            emulatorpath = "E:\\XuanZhi\\LDPlayer\\dnplayer.exe"
            os.startfile(emulatorpath)
            speak("Opening LDPlayer Emulator...")
            print("Opening LDPlayer Emulator...")

        elif 'email to mum' in query:
            try:
                speak("What should I say Sir?")
                content = takeCommand()
                to = "email1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Mom!!!")
            except Exception as e:
                print(e)
                speak("Sorry Mom, I am not able to send this email")
                print("Sorry Mom, I am not able to send this email")

        elif 'email to dad' in query:
            try:
                speak("What should I say Sir?")
                content = takeCommand()
                to = "email2@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Dad!!!")
            except Exception as e:
                print(e)
                speak("Sorry Dad, I am not able to send this email")
                print("Sorry Dad, I am not able to send this email")

        elif 'email to sister' in query:
            try:
                speak("What should I say Sir?")
                content = takeCommand()
                to = "email3@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Sister!!!")
            except Exception as e:
                print(e)
                speak("Sorry Sister, I am not able to send this email")
                print("Sorry Sister, I am not able to send this email")
        
        elif 'buy johnson' in query:
            speak("Good Bye Sir! Talk to You Soon...")
            print("Good Bye Sir! Talk to You Soon...")
            sys.exit()

        elif 'goodbye johnson' in query:
            speak("Good Bye Sir! Talk to You Soon...")
            print("Good Bye Sir! Talk to You Soon...")
            sys.exit()

        elif 'good night johnson' in query:
            speak("Good Night Sir! Have Sweet Dreams...")
            print("Good Night Sir! Have Sweet Dreams...")
            sys.exit()

        elif 'good morning johnson' in query:
            speak("Good Morning Sir! Hope You slept well...")
            print("Good Morning Sir! Hope You slept well...")

        elif 'how are you' in query:
            speak("I am fine Sir! Thanks for Asking...")
            print("I am fine Sir! Thanks for Asking...")

        elif 'who are you' in query:
            speak("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")
            print("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")

        elif 'about you' in query:
            speak("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")
            print("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")
        
        elif 'your introduction' in query:
            speak("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and  virtual assistant... Thank You for using me...")
            print("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")

        elif 'introduce yourself' in query:
            speak("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")
            print("I am Johnson Sir! I have been created by a passionate, young and intelligent software developer named: - Theee Kaushik Goswami. I am made for helping you in your daily works by making your work easier. I am currently in development and soon going to get many other features... Hope that you will not mind me being your digital and virtual assistant... Thank You for using me...")
