from tkinter import *
import tkinter as tk
import module


BG_COLOR = '#26004d'
TEXT_COLOR = '#ffffff'
global user_name
global user_number

def processButton(name):
    
    


root = Tk()

# giving title to the main window
root.title(u"Нумерология")
root.geometry('1200x600')
bgc = tk.Canvas(root,bg=BG_COLOR)
bgc.place(relwidth=1,relheight=1)
import os.path
alg_path = os.path.dirname(__file__) + '/'
bg_image = tk.PhotoImage(file=alg_path + 'numbers_bg.png')
bg_lable = tk.Label(root,image=bg_image)
bg_lable.place(x=0,y=0,relwidth=1,relheight=1)


frame1 = tk.Frame(root, bg=BG_COLOR)
frame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
wellcome_text = Label(frame1,bg=BG_COLOR,fg=TEXT_COLOR, text="Узнай цифру своего имени и ее значение",anchor='w',height=3)
wellcome_text.pack()

nameFrame = tk.Frame(frame1)
nameFrame.place(relx= 0.2,rely=0.2,relheight=0.1,relwidth=0.6)

name_label = tk.Label(nameFrame,text=u"Введи имя:").pack(side= 'left')
entry = Entry(nameFrame,bg=BG_COLOR,fg =TEXT_COLOR)
entry.pack(side='top')
start_btn = tk.Button(nameFrame,text="Узнать",command=lambda:processButton(entry.get()))
start_btn.pack(side = 'right')

answerFrame = tk.Frame(frame1)
answerFrame.place(relx= 0.2,rely=0.4,relheight=0.5,relwidth=0.6)

answerLabel = tk.Label(answerFrame, text = f"Число имени {user_name} это {user_number}").pack()
answerText = tk.Text(answerFrame).pack()

root.mainloop()
