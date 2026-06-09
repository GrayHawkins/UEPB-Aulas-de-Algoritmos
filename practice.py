import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('calculator')
root.geometry('250x400+500+100')
root.resizable(0,0)

frame_1= Frame(root)
frame_1.pack(expand=True,fill=BOTH)

key_1 = Button()
frame_1,
text='1',
font=('Arial',22)
border=0,
relief=GROOVE,
bg='#2E2E2B',
fg='white',
command = lambda:display(1)
    