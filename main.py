from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox

root = Tk()
root.title("Test the Sounds")
root.geometry('470x480+500+100')
root.resizable(False,False)

def welcome():
    music = AudioSegment.from_mp3('sounds/welcome1.mp3')
    play(music)
    

welcome()
root.mainloop()