import speech_recognition as sr
import threading
import pyttsx3
from tkinter import *
from tkinter import ttk



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
    
root = Tk()
root.geometry('400x200')
root.resizable(0,0)
root.config(bg = 'light yellow')

output = Label(root,text ="The transcribed text is: ", font = 'arial 13 bold', bg ='white smoke')
output.place(x=100,y=80)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(output):
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        print('Done')
        print('Enter the number in which language you talk(E-0,H-1,B-2): ')
        languages = ['en-IN','hi-IN','bn-IN']
        choice = int(input(''))
        text = listener.recognize_google(voice,language = languages[choice])
        print(text)
        talk(text = listener.recognize_google(voice))
        output.config(text = text)

def startTakingCommand():
    global output
    t1 = threading.Thread(target = take_command, args=(output,))
    t1.start()


Input_text = Text(root,font = 'arial 10', height = 100, wrap = WORD, padx=200, pady=200, width = 60)

trans_btn = Button(root,text = 'Voice',font = 'arial 12 bold',pady = 5,command = startTakingCommand , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 165, y= 20 )
root.mainloop()
