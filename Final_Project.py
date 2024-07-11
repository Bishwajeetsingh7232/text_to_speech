import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk,messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox 
import customtkinter
import googletrans
import textblob
import pyttsx3
import speech_recognition as sr
from PyDictionary import PyDictionary
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()

root.title('Text And Speech Tool')
root.geometry("900x450+200+200")
root.resizable(False, False)

image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg="#308695",width=900,height=100)
Top_frame.place(x=0,y=0)

#Logo=PhotoImage(file="Logo")
#Label(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

Label(Top_frame,text="TEXT AND SPEECH TOOL" ,font="arial 20 bold",bg="#455054",fg="#D4CFC9").place(x=250,y=30)

def TextToSpeech():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    texttospeechwindow = customtkinter.CTk()

    texttospeechwindow.title('Text To Speech Convertor')
    texttospeechwindow.geometry("900x450+200+200")
    texttospeechwindow.resizable(False, False)

    #   Top Frame
    Top_frame=Frame(texttospeechwindow,bg="#308695",width=900,height=100)
    Top_frame.place(x=0,y=0)

    #Logo=PhotoImage(file="Logo")
    #Label(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

    Label(Top_frame,text="TEXT TO SPEECH CONVERTER" ,font="arial 20 bold",bg="#455054",fg="#D4CFC9").place(x=250,y=30)
    ########

    engine = pyttsx3.init()
    def speak():
        text=text_area.get(1.0,END)
        gender=gender_combobox.get()
        speed=speed_combobox.get()
        voices=engine.getProperty('voices')
    
        def setvoice():
            if(gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                engine.say(text)
                engine.runAndWait()
            
        if(text):
            if(speed =="Fast"):
                engine.setProperty('rate',250)
                setvoice()
            elif(speed=="Normal"):
                engine.setProperty('rate', 150)
                setvoice()
            else:
                engine.setProperty('rate', 60)
                setvoice()
                   
    def download():
        text=text_area.get(1.0,END)
        gender=gender_combobox.get()
        speed=speed_combobox.get()
        voices=engine.getProperty('voices')
    
        def setvoice():
            if(gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
            
        if(text):
            if(speed =="Fast"):
                engine.setProperty('rate',250)
                setvoice()
            elif(speed=="Normal"):
                engine.setProperty('rate', 150)
                setvoice()
            else:
                engine.setProperty('rate', 60)
                setvoice()

    text_area=Text(texttospeechwindow,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
    text_area.place(x=10,y=150,width=500,height=250)

    Label(texttospeechwindow,text="VOICE",font="arial 15 bold",bg="#181818",fg="#305065").place(x=580,y=160)
    Label(texttospeechwindow,text="SPEED",font="arial 15 bold",bg="#181818",fg="#305065").place(x=760,y=160)

    gender_combobox=Combobox(texttospeechwindow,values=['Male','Female'],font="arial 14",state='r',width=10)
    gender_combobox.place(x=550,y=200)
    gender_combobox.set('Male')

    speed_combobox=Combobox(texttospeechwindow,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
    speed_combobox.place(x=730,y=200)
    speed_combobox.set('Normal')
    
    #imageicon=PhotoImage(file="speak.png")
    btn=Button(texttospeechwindow,text="Speak",width=10,font="arial 14 bold",command=speak)
    btn.place(x=550,y=280)
    
    #imageicon2=PhotoImage(file="speak.png")
    save=Button(texttospeechwindow,text="Save",width=10,bg="#39c790",font="arial 14 bold",command=download)
    save.place(x=730,y=280)

    texttospeechwindow.mainloop()

def SpeechToText():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    speechtotextwindow = customtkinter.CTk()

    speechtotextwindow.title('Speech To Text Converter')
    speechtotextwindow.geometry("900x450+200+200")
    speechtotextwindow.resizable(False, False)

    #   Top Frame
    Top_frame=Frame(speechtotextwindow,bg="#308695",width=900,height=100)
    Top_frame.place(x=0,y=0)

    #Logo=PhotoImage(file="Logo")
    #Label(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

    Label(Top_frame,text="SPEECH TO TEXT CONVERTER" ,font="arial 20 bold",bg="#455054",fg="#D4CFC9").place(x=250,y=30)
    ########
    text1=''
    file_name=("D:/Project (22-23)/Speech.wav")
    def recordvoice():
        while True:
            text1 =''
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:    
                    text1 = r.recognize_google(audio)
                except:
                    pass
                return text1
    def Filevoice():
        while True:
            text1 =''
            r = sr.Recognizer()
            with sr.AudioFile(file_name) as source: # open file 
                audio=r.listen(source)
                try:    
                    text1 = r.recognize_google(audio)
                except:
                    pass
                return text1           
    def Reset():
        text.delete(1.0,END)            
 
    text = Text(speechtotextwindow, font=12, height=5, width=30)
    text.place(x=10,y=150,width=500,height=250)
   
    recordbutton = Button(speechtotextwindow,text="Record",width=10,bg="#39c790",font="arial 14 bold", command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=550, y=200)

    filebutton = Button(speechtotextwindow, text='Import',width=10, bg='#39c790',font="arial 14 bold", command=lambda: text.insert(END, Filevoice()))
    filebutton.place(x=730, y=200)

    speechtotextwindow.mainloop()
def Translator():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root= customtkinter.CTk()

    root.title('Translator')
    root.geometry("900x450+200+200")
    root.resizable(False, False)

    #   Top Frame
    Top_frame=Frame(root,bg="#308695",width=900,height=100)
    Top_frame.place(x=0,y=0)

    #Logo=PhotoImage(file="Logo")
    #Label(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

    Label(Top_frame,text="Translator" ,font="arial 20 bold",bg="#455054",fg="#D4CFC9").place(x=365,y=30)
    ########

    def translate_it():
	# Delete Any Previous Translations
        translated_text.delete(1.0, END)

        try:
            # Get Languages From Dictionary Keys
            # # Get the From Langauage Key
            for key, value in languages.items():
                if (value == original_combo.get()):
                    from_language_key = key

            # Get the To Language Key
            for key, value in languages.items():
                if (value == translated_combo.get()):
                    to_language_key = key
            
            # Turn Original Text into a TextBlob
            words = textblob.TextBlob(original_text.get(1.0, END))

            # Translate Text
            words = words.translate(from_lang=from_language_key , to=to_language_key)

            # Output translated text to screen
            translated_text.insert(1.0, words)

        except Exception as e:
            messagebox.showerror("Translator", e)




    def clear():
	# Clear the text boxes
        original_text.delete(1.0, END)
        translated_text.delete(1.0, END)

    #language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1)

    # Grab Language List From GoogleTrans
    languages = googletrans.LANGUAGES

    # Convert to list
    language_list = list(languages.values())




    # Text Boxes
    original_text = Text(root, height=10, width=40,bg="#7E909A")
    original_text.place(x=40,y=130)

    #translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
    #translate_button.place(x=450,y=180)

    translated_text = Text(root, height=10, width=40,bg="#7E909A")
    translated_text.place(x=530,y=130)

    # Combo boxes
    original_combo = ttk.Combobox(root, width=50, value=language_list)
    original_combo.current(21)
    original_combo.place(x=40,y=320)

    translated_combo = ttk.Combobox(root, width=50, value=language_list)
    translated_combo.current(26)
    translated_combo.place(x=530,y=320)
    translated_button = customtkinter.CTkButton(root, text="<-- Translate -->", command=translate_it)
    translated_button.place(x=377,y=200)

    # Clear butt
    #clear_button = Button(root, text="Clear", command=clear)
    #clear_button.grid(row=2, column=1)
    clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
    clear_button.place(x=377,y=315)


    root.mainloop()
    

def Dictionary():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()

    root.title('Dictionary')
    root.geometry("700x450")
    root.resizable(False, False)

    def search():
        my_text.delete(1.0, END)
        dictionary = PyDictionary()
        definition = dictionary.meaning(my_entry.get())
        for key,value in definition.items():
            my_text.insert(END, key + '\n\n')
            for values in value:
                my_text.insert(END, f'- {values}\n\n')




    my_labelframe = customtkinter.CTkFrame(root, corner_radius=10)
    my_labelframe.pack(pady=20)

    my_entry = customtkinter.CTkEntry(my_labelframe, width=400, height=40, border_width=1, placeholder_text="Enter A Word", text_color="silver")
    my_entry.grid(row=0, column=0, padx=10, pady=10)

    my_button = customtkinter.CTkButton(my_labelframe, text="Search", command=search)
    my_button.grid(row=0, column=1, padx=10)

    text_frame = customtkinter.CTkFrame(root, corner_radius=10)
    text_frame.pack(pady=10)

    my_text = Text(text_frame, height=20, width=67, wrap=WORD, bd=0, bg="#292929", fg="silver")
    my_text.pack(pady=10, padx=10)
    root.mainloop()

texttospeechbutton = customtkinter.CTkButton(root, text='Text-To-Speech Conversion', font=('Times New Roman', 24), command=TextToSpeech)
texttospeechbutton.place(x=280, y=150)

speechtotextbutton = customtkinter.CTkButton(root, text='Speech-To-Text Conversion', font=('Times New Roman', 24), command=SpeechToText)
speechtotextbutton.place(x=280, y=210)

translatorbutton = customtkinter.CTkButton(root,text=   '      Language Translator      ',font=('Times New Roman', 24), command=Translator)
translatorbutton.place(x=280, y=270)

dictionarybutton = customtkinter.CTkButton(root,text=   '        Word Dictionary         ',font=('Times New Roman', 24), command=Dictionary)
dictionarybutton.place(x=280, y=330)

root.update()
root.mainloop()
