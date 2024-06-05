import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am a cow. How may I assist you today?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__=="__main__":
    speak("Hi Abhinav")
    wishMe()
    while True:
        query  = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codepath="C:\\Users\\abhin\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email me' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to = "abhinavsureshep@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry the email could not be sent")
        elif 'stop' or 'bye' or 'see you later' in query:
            speak("Bye, Have a great day")
            break
        
        
        
