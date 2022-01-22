import speech_recognition as sr
import pyttsx3
import datetime
from pywikihow import search_wikihow
import wikipedia
import webbrowser
import os
import ctypes
import time
import subprocess as sp
from ecapture import ecapture as ec
import wolframalpha
import requests
import pywhatkit
from playsound import playsound
  
print('\n Loading A-I personal assistant - J.E.E.V.A. \n')

#AI's Voice Properties
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#Functions
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Sir.")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon Sir.")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening Sir.")
        print("Hello,Good Evening")

counter=0
def takeCommand():
    global counter
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            counter=0
        
        except Exception as e:
            
            speak("I didn't get that. Please say that again sir! ")
            counter+=1
            if counter==3:
                    speak("sorry, commnad not found sir !")
                    exit()

            return "None"
        return statement

def getCommand():
    global counter
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            confirmation=r.recognize_google(audio,language='en-in')
            print(f"user said:{confirmation}\n")
            counter=0
        except Exception as e:
            speak("Give response as Yes or no..")
            counter+=1
            if counter==3:
                speak("Sorry, Commnad not found sir !")
            return "None"
        return confirmation

def AcceptCommand():
    global counter
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            wake=r.recognize_google(audio,language='en-in')
            print(f"user said:{wake}\n")
            counter=0

        except Exception as e:
            speak ("say wakeup to start your voice assistant")
            counter+=1
            if counter==3:
                speak("Sorry,command not found sir!")
            return "None"
        return wake

# main Function
def task_Gui():
    
    os. system('cls')
    print('Loading your A-I personal assistant - J.E.E.V.A')
    speak('Loading your A-I personal assistant - Jeevaa')
   
    while True:
            print("Say wakeup to start the voice assistant.") 
            speak("Say wakeup to start the voice assistant.") 
            wake = AcceptCommand().lower()
            time.sleep(3)


            if "wakeup" in wake or "start" in wake or "wake" in wake:
                path=('C://Users//Pradeep Mishra//Music//my songs//windows_10_notify(Wakeup_Sound).mp3')
                playsound(path)
                speak("Hi Jeevaa is back! Starting now...")
                wishMe()
                speak ("How are you sir ?")
                print ("How are you sir ?")
                answer=takeCommand().lower()
                time.sleep(2)
        
                if 'you' in answer:
                    if "fine" in answer or "good" in answer or "ok" in answer:
                        speak("Fine sir!")
                    
                while True:
                                      
                    speak("Let me know how can I help you sir?")
                    print("\nLet me know how can I help you sir?")
                    statement = takeCommand().lower()
                    time.sleep(2)

                    # sign out
                    if "good bye" in statement or "ok bye" in statement or "stop" in statement or "sign out" in statement:
                        speak('Thank you, Have a nice day sir. Your personal assistant JEEVA is Signing out !')
                        print('your personal assistant JEEVA is Signing out sir..\n')
                        time.sleep()
                    
                    if "clear screen" in statement or "clear this screen" in statement or "clear the screen" in statement:
                        os.system('cls')
                        time.sleep(4)

                    # wait
                    if 'wait' in statement or 'wait for a second' in statement:
                        speak("ok, waiting for some seconds sir!")
                        print ("waiting for some seconds...")
                        time.sleep(20) 
                    
                    #basic talk
                    
                    elif 'who are you' in statement or 'about you' in statement :
                        speak('I am Jeeva version 1 point O as a personal voice assistant.')
                        time.sleep(5)
                        

                    elif 'how are you' in statement or 'what about you' in statement :
                        speak("I am Fine. and you ?")
                        greet=takeCommand()
                        time.sleep(2)
                        
                
                    elif 'what can you do' in statement or 'features' in statement :  
                        print('I am programmed to perform minor tasks. like;'
                            'Play songs on youtube.'
                            '\nPredict time.\nTake a photo.\nsearch on wikipedia'
                            '\nSearch on Google\nWeather forecast in different cities.'
                            '\nSearch Something on wikipedia.\nGet top headline news from Google.'
                            '\nAnswer computational and geographical questions.')

                        speak('I am programmed to perform minor tasks. like;'
                            'Play songs on youtube, '
                            'Predict time, Take a photo, Search something on Google, Predict Weather forecast in different cities, '
                            'Search Something on wikipedia, Get top headline news from Google and I can Answer computational and geographical questions too.')
                        
                 
                        time.sleep(5)

                    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                        speak("I was built by Shivsagar Mishra")
                        print("I was built by Shivsagar Mishra")
                        time.sleep(5)            
                    
                  
                    elif "like me" in statement:
                        print("sorry sir, I don't made for that !")
                        time.sleep(5)
                         
                    # search on wikipedia
                    elif 'on wikipedia' in statement:
                        speak('Searching on Wikipedia sir...')
                        statement =statement.replace("wikipedia", "")
                        results = wikipedia.summary(statement, sentences=3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                        time.sleep(10)
                
                    #open websites
                    elif 'open youtube' in statement:
                        webbrowser.open_new_tab("https://www.youtube.com")
                        speak("Sure,Opening Youtube!")
                        time.sleep(20)
        
                    elif 'open google search' in statement:
                        webbrowser.open_new_tab("https://www.google.com")
                        speak("sure, Opening Google search!")
                        time.sleep(20)

                    elif 'open gmail' in statement:
                        webbrowser.open_new_tab("https://mail.google.com")
                        speak("Sure, opening Google Mail !")
                        time.sleep(20)

                    elif "open classroom" in statement:
                        webbrowser.open_new_tab("https://classroom.google.com/u/1/h")
                        speak("Opening Your Classroom")
                        time.sleep(15)

                    elif "open stack overflow" in statement or "stackoverflow" in statement:
                        webbrowser.open_new_tab("https://stackoverflow.com/")
                        speak("Here is stackoverflow")
                        time.sleep(25)

                    elif 'news' in statement:
                        news = webbrowser.open_new_tab("https://news.google.com")
                        speak('Here are some headlines from the Google News,Happy reading')
                        time.sleep(25)

                    #open Browsers
                    elif 'open chrome' in statement or 'open google' in statement:
                        path = ("C://Program Files (x86)//Google//Chrome//Application//chrome.exe")
                        speak("Sure sir! opening Google Chrome!")
                        os.startfile(path)
                        time.sleep(20)

                    elif 'open brave' in statement:
                        path = ("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe")
                        speak("Sure sir! opening Brave Browser!")
                        os.startfile(path)
                        time.sleep(20)

                    elif 'open edge' in statement or 'open microsoft edge' in statement:
                        path = ("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe")
                        speak("Sure sir! opening Microsoft Edge!")
                        os.startfile(path)
                        time.sleep(20)

                    #open Applications
                    elif 'notepad' in statement:
                        path = ("C://Windows//System32//notepad.exe")
                        speak("Sure opening NotePad.")
                        os.startfile(path)
                        time.sleep(15)
                    
                    # utilities
                    # who is
                    elif 'who is' in statement:
                        person = statement.replace('who is', '')
                        info = wikipedia.summary(person, 1)
                        print(info)
                        speak(info)
                        time.sleep(7)

                
                    #Telling Time
                    elif 'time' in statement:
                        current_time=datetime.datetime.now().strftime("%I %M %p")
                        current_timeprint=datetime.datetime.now().strftime("%I:%M %p")
                        speak("The current time is"+ current_time)
                        print("The current time is: "+current_timeprint)
                        time.sleep(7) 

                    #playing songs on youtube
                    elif 'play songs on youtube' in statement or 'play song on youtube' in statement:
                        while True:
                            speak ('which song you want to play')
                            song = takeCommand().lower()
                            speak('sure sir,playing ' + song)
                            print('sure sir,playing : ' + song)
                            pywhatkit.playonyt(song)
                            time.sleep(30)
                            speak ("Do you want to play another song?")
                            conf = getCommand().lower()
                            time.sleep(6)
                            if 'yes' in conf:
                                continue
                            elif 'no' in conf:
                                speak("Ok, exiting from here...")
                                print("Ok, exiting from here...")
                                break
                            else:
                                break
                            
                    # search about something
                    elif 'search'  in statement:
                        webbrowser.register('chrome',
                            None,
                        webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
                        statement = statement.replace("search", "https://www.google.com/search?q=")
                        webbrowser.get('chrome').open_new_tab(statement)
                        time.sleep(20)

                    #capturing photo
                    elif "camera" in statement or "take a photo" in statement:
                        speak("Ok, Taking Photo ... ")
                        try:                   
                            ec.capture(0,"camera","img.jpg")
                        except Exception as e:
                            speak("You have closed the window. Exiting from here...")
                            print("Exiting from capturing photo...")
                        time.sleep(7)
                    
                    #Activate how to do mode
                    elif 'activate how to do mode' in statement or 'how to do mode' in statement:    
                        speak('How to do mode is activated. Please tell me what you want to do...')
                        how = takeCommand()
                        time.sleep(5)
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                        time.sleep (10) 

                    # Weather
                    elif "weather" in statement:
                        api_key="0953116aaf855fb55f282e0740ea793b"
                        base_url="https://api.openweathermap.org/data/2.5/weather?"
                        print("Let me know the city name")
                        speak("Let me know the city name:")
                        city_name=takeCommand()
                        time.sleep(5)
                        complete_url=base_url+"appid="+api_key+"&q="+city_name
                        response = requests.get(complete_url)
                        x=response.json()
                        if x["cod"]!="404":
                            y=x["main"]
                            current_temperature = y["temp"]
                            current_humidiy = y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]
                            current_temp_in_celcius=round((current_temperature-273.15),2)
                           
                            print(" Temperature in Degree Celcius is = " +
                                str(current_temp_in_celcius) +
                                "\n °C" +
                                "\n humidity (in percentage) = " +
                                str(current_humidiy) +
                                "\n description = " +
                                str(weather_description))
                            
                            speak(" Here, I got it sir :Temperature in Celcius unit is " +
                                
                                str(current_temp_in_celcius) +
                                "\n Degree Celcius" +
                                "\n humidity in percentage is " +
                                str(current_humidiy) +
                                "\n description  " +
                                str(weather_description))
                        else:
                            speak("sorry, City Not Found sir")
                        
                        time.sleep(10)

                    #answering questions                
                    elif 'ask' in statement and 'question' in statement:
                        speak('Sure, I can answer to computational and geographical questions !!')
                        print('Sure, I can answer to computational and geographical questions !!')
                        while True:
                            speak('what question do you want to ask now?')
                            print('what question do you want to ask now?')
                            question=getCommand()
                            time.sleep(4)
                            app_id=("R2K75H-7ELALHR35X")
                            client = wolframalpha.Client('R2K75H-7ELALHR35X')
                            res = client.query(question)
                            
                            try:
                                answer = next(res.results).text
                                speak(answer)
                                print(answer)
                            except:
                                speak("Sorry, No answer Found sir!!")
                                print("Sorry, No Answer found sir!! ")
                            
                            finally:
                                speak ("Do you want to ask another question?")
                                confirmation = getCommand().lower()
                                time.sleep(6)
                                if 'yes' in confirmation:
                                    continue
                                elif 'no' in confirmation:
                                    speak("Ok, exiting from here...")
                                    print("Ok, exiting from here...")
                                    break
                                else:
                                    break

                    #Shutting down the pc
                    elif "shutdown the pc" in statement or "shut down the pc" in statement :
                        speak("Ok, your pc will Shut down in 10 second make sure you exit from all applications")
                        print("Ok, your pc will Shut down in 10 second make sure you exit from all applications")
                        time.sleep (10)
                        print("Do you really wish to shutdown your computer sir? \n(respond as Yes or no )")
                        speak("Do you really wish to shutdown your computer sir?")
                        confirmation=takeCommand()
                        if 'yes' in confirmation:
                            ctypes.windll.user32.LockWorkStation()
                            sp.call('shutdown /s /t 1', shell=True)

                        elif 'no' in confirmation:
                            continue
                        time.sleep(4)

                    elif "restart the pc" in statement:
                        speak("Ok, your pc will restart in 10 second make sure you exit from all applications")
                        print("Ok, your pc will restart in 10 second make sure you exit from all applications")
                        time.sleep (10)
                        print("Do you really wish to restart your computer sir? \n(respond as Yes or no )")
                        speak("Do you really wish to restart your computer sir?")
                        confirmation=takeCommand()
                        if 'yes' in confirmation:
                           sp.call('shutdown /r /t 1', shell=True)
                        elif 'no' in confirmation:
                            continue
                        time.sleep(4)

                    elif "lock the pc" in statement:
                        print("Ok sir, Locking your pc ")
                        speak("Ok sir, Locking your pc ")
                        time.sleep (2)
                        ctypes.windll.user32.LockWorkStation()
                        time.sleep(4)

                    elif "hibernate the pc" in statement:
                        speak("Ok, your pc will Hybernate in 10 seconds")
                        print("Ok, your pc will Hybernate in 10 seconds")
                        time.sleep (4)
                        print("Do you really wish to Hybernate your computer sir? \n(respond as Yes or no )")
                        speak("Do you really wish to Hybernate your computer sir?")
                        time.sleep(1)
                        confirmation=takeCommand()
                        if 'yes' in confirmation:
                           sp.call('shutdown /h /t 1', shell=True)
                        elif 'no' in confirmation:
                            continue
                        time.sleep(4)
                    
                    elif "sign out current user" in statement or "signout current user" in statement: 
                        time.sleep (3)
                        print("Do you really wish to sing out from PC?\n(respond as Yes or no )")
                        speak("Do you really wish to sing out from PC?")
                        time.sleep(1)
                        confirmation=takeCommand()
                        if 'yes' in confirmation:
                            speak("Ok, Signing out current user...")
                            print("Ok, Signing out current user...")
                            sp.call('shutdown /l /t 1', shell=True)
                        elif 'no' in confirmation:
                            continue
                        time.sleep(5)  
                    
                 

                    else: 
                        print("Sorry sir, I didn't get that ! ")
                        time.sleep(1)
                        continue           
                        
            elif "bye" in wake or "ok bye" in wake or "stop" in wake or "sign out" in wake:
                print('Do you want to leave?')
                speak ('Do you want to leave?')
                conf=getCommand().lower()
                if 'yes' in conf:
                    speak('Ok,Exiting sir...')
                    print('Ok Exiting sir...')
                    exit()
                elif 'no'in conf:
                    speak("ok,Trying Again...")
                    print("ok,Trying Again...")
                    continue 

    
        
                



            
