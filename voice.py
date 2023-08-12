import pyttsx3
import speech_recognition as sr #import for take command
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
   hour= int(datetime.datetime.now().hour)
   if hour>=0 and hour<12: 
       speak("Good Morning!")
       print("Good Morning!")
   elif hour>=12 and hour<18: 
       speak("Good Afternoon!")
       print("Good Afternoon!")
   else : 
       speak("Good Evening!")
       print("Good Evening!")

def wishMe2():
  speak("I am CD Sir. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")

        except Exception as e:
             print("Say That again please...")
             return "None"
        return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rockykhan675@yahoo.com', '1191172Rockykhan')
    server.sendmail('rockykhan675@yahoo.com', to, content)
    server.close()


if __name__ == "__main__" :
   wishMe()
   wishMe2()
   while True:

    query = takeCommand().lower()
    if 'wikipedia' in query:
       speak('Searching Wilipedia...')
       query = query.replace("wikipedia", "")
       results = wikipedia.summary(query, sentences=3) 
       speak("According to wikipedia")
       print(results)
       speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
  
    elif 'open google' in query:
        webbrowser.open("google.com") 

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'current time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("The Time is ",strTime)
        speak(f"The Time is {strTime}")  

    elif 'open android' in query:
        path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\XAMPP"
        os.startfile(path)

    elif 'email to rocky' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rockykhan675@yahoo.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, can't send email at this moment") 
