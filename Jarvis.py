import random
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import os
from gtts import gTTS
from playsound import playsound
import subprocess
from tkinter import *
import pyaudio
global flag
flag = 0
def takeCommand():
    global flag
    # Exception handling to handle
    # exceptions at the runtime
    Label(root,text="Listening...." , font="BOLD").pack()

    with sr.Microphone() as source:
            r = sr.Recognizer()
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
    try:
            #listens for the user's input
            Label(root, text='.....', font="BOLD").pack()
            query = r.recognize_google(audio)


    except sr.RequestError as e:
        Label(root, text="Could not request results; {0}".format(e), font = "BOLD")
        return e
    except sr.UnknownValueError:
        Label(root,text="unknown error occured",font="BOLD")
        speak('Sorry ...! your Time is up ')
        flag += 1
        return 'None'
    return query

def speak(command):
    try:
        myobj = gTTS(text=command, lang='en', slow=False)
        myobj.save('welcome.mp3')

        # os.system("welcome.mp3")
        playsound("welcome.mp3")
        os.remove('welcome.mp3')
        Label(root,text=command,font="BOLD").pack()
    except :
        pass
        # speak('i can\'t undestand your command')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        a = "Good morning ", "A pleasent morning ", "Hello  Good Morning", "O, Good morning ", "O, good morning ", "Wow! Welcome back"
        ch = random.choice(a)
        speak(ch)
        # Label(root, text=ch, font="BOLD").pack()

    elif hour>= 12 and hour< 18:
        b = "Good Afternoon ", "Good Afternoon ", "Hello Good Afternoon", "O, Good Afternoon ", "O, good Afternoon", "Wow! Welcome back "
        ch = random.choice(b)
        speak(ch)
        # Label(root, text=ch, font="BOLD").pack()
    else:

        c = "Good Evening", "Good Evening ", "Hello  Good Evening", "O, Good Evening ", "O, good Evening ", "Wow! Welcome back "
        ch = random.choice(c)
        # Label(root, text=ch, font="BOLD").pack()
        speak(ch)


def welcome():
    wel = "So, how can i help you ", "How can i help", "Online and ready ", "What can i do for you", "Please give me a command "
    ch = random.choice(wel)
    speak(ch)

# count=0
def hello():
    Label(root).config(text=" ")
    wishMe()
    # welcome()
    global flag
    # speak('i\'m ready to help you to solve your issue')
    while True:
        time = datetime.datetime.now()
        # Button(root,text= "QUIT" , command=root.destroy).pack(side=BOTTOM, padx=5, pady=5)
        # if count>0:
        speak("i'm listening tell me your command ")

        # label = Label(root, text=takeCommand(), font="BOLD").pack()

        query= takeCommand().lower()
        # query = list(query)

        label = Label(root,text=query,font="BOLD").pack()
        # query = input('Enter the query :')
        if 'wikipedia' in query or 'search on wikipedia' in query:
            speak("what do you want to search")
            try:
                query = takeCommand()
                results = wikipedia.summary(query, sentences = 3)

                speak("so, wikipedia says")
                speak(results)

            except:
                speak("Not available on wikipedia")

        if flag == 3:
            speak('your chances are completed please press start button again to start')
            flag = 0
            break

        if 'open google' in query or 'search on google' in query or 'type on google' in query:
            ak = "what should i search?", "please say the words you want to search for", "what would you like to search ?", "I am typing, say what you want to search on google?"
            ch = random.choice(ak)
            speak(ch)
            h = takeCommand().lower()
            flag = 0
            webbrowser.open(f"https://www.bing.com/search?q={h}")

        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            ch = random.choice(dg)
            speak(ch)
            x = takeCommand().lower()
            flag = 0
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")


        elif 'open web browser' in query or 'open a new tab of browser' in query or 'open a web browser' in query:

            webbrowser.open("www.goolge.com")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish ")
            flag = 0

        elif 'open c drive' in query:
            os.startfile("C:")
            flag = 0

        elif 'open d drive' in query:
            os.startfile("D:")
            flag = 0

        elif 'open e drive' in query:
            os.startfile("E:")
            flag = 0

        elif 'open chrome' in query:
            # path = "C:\Users\Public\Desktop\Google Chrome.lnk"
            os.startfile("C:\\Users\\Public\Desktop\\Google Chrome.lnk")
            flag = 0

        elif 'time' in query :
            a = f'now the time is : {time.hour} : {time.minute}'
            speak(a)
            Label(root, text = a, font = "BOLD").pack()
            flag = 0

        elif 'date' in query:
            a = f'today date is : {time.date()}'
            speak(a)
            label = Label(root,text=a,font="BOLD")
            flag = 0

        elif 'day' in query:
            a = f'today is {time.day}'
            speak(a)
            label = Label(root,text=a,font="BOLD")
            flag = 0

        elif 'joke' in query:
            a = pyjokes.get_joke()
            speak(a)
            flag = 0

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system ?")
            ch = takeCommand()
            if "yes" in ch:
                os.system("shutdown /s /t 1")
            else:
                speak("ok ")
            flag = 0

        elif 'sleep' in query or 'sleep my system' in query or 'sleep my pc' in query:
            speak("Do you really want to sleep the system ?")
            ch = takeCommand()
            if "yes" in ch:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            else:
                speak("ok ")
            flag = 0

        elif 'restart' in query or 'restart my system' in query or 'restart my pc' in query:
            speak("Do you really want to restart the system ?")
            ch = takeCommand()
            if "yes" in ch:
                os.system("shutdown /r /t 1")
            else:
                speak("ok ")
            flag = 0

        elif "play music" in query:
            speak("tell me the song name!")
            p = takeCommand()
            # p = query
            webbrowser.open(f"https://soundcloud.com/search?q={p}")
            flag = 0

        elif "play" in query:
            query = query.replace("play", "")
            speak("Ok  opening your desired song!")
            webbrowser.open(f"https://soundcloud.com/search?q={query}")
            flag = 0

        elif 'who are you' in query or "give me your introduction" in query:
            speak("Wait, i am introducing myself. My name is Jarvis, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more")
            flag = 0

        elif "who am i" in query:
            jh = "if you are speaking then, definately you are a human", "You are ", "You are a human", "I cant identify peoples with their vocies, may be you are  or anybody with relation of "
            ch = random.choice(jh)
            speak(ch)
            flag = 0

        elif 'hello' in query:
            gf = "O hello ", "Hi ", "I am here for your help !", "hello ", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            ch = random.choice(gf)
            speak(ch)
            flag = 0

        elif 'open notepad' in query or 'open note pad' in query :

            ask = query.split()[-1]
            subprocess.call(f'{ask}.exe')
            flag = 0

        elif 'open command prompt' in query or 'open commandprompt' in query:
            subprocess.call('cmd.exe')
            flag = 0

        elif 'open' in query :
            query = query.replace('open', '').strip()
            webbrowser.open(f"https://www.{query}.com/")
            flag = 0

        # elif 'open' in query:
        #     query = query.replace('open','').strip().replace(' ','+')
        #     label = Label(root, text=query, font="BOLD").pack()
        #     webbrowser.open(f"https://www.{query}/")
        #     flag = 0

        elif 'close notepad' in query:
            speak('closing notepad ')
            os.system('taskkill /f /im notepad.exe')
            flag = 0

        elif 'close command prompt' in query:
            speak('closing command prompt ')
            os.system('taskkill /f /im cmd.exe')
            flag = 0

        elif 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query :
            f = "bye ", "ok bye ", "see you again ", "bye bye", "As your wish ", "Waiting for further Activation ", "As your wish, but I dont want to go ! anyhow bye "
            speak(random.choice(f))
            root.destroy()
            return

        elif 'wait' == query:
            break

        # elif query == 'None':
        #     continue

        elif query is sr.RequestError :
            speak("Sorry i cannot do that")
        global count
        count=1

root = Tk()

root.geometry("800x600")

root.title("Jarvis")

count =0

Label(root,text='I\'m Jarvis press start to command me', font = "BOLD").pack()
Button(root,text="START", command=hello, font="BOLD").pack(side=BOTTOM, pady=5)
Button(root,text= "QUIT" , command=root.destroy).pack(side=BOTTOM, padx=5, pady=5)
root.mainloop()

