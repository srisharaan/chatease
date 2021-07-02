from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import tkinter as tk
from signup import signupuh 
from login import loginuh


def tutorials():
    root.destroy()
    loginuh()

def startuh():
    root.destroy()
    signupuh()

        
IMAGE_PATH = 'aa.jpeg'
WIDTH, HEIGTH = 600, 400

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGTH))
root.title("Quick Chat")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)



myFont = font.Font(family='Tw Cen MT', size=16)

button = tk.Button(root, text="Signup",bg="#99643A",fg='white',command=startuh,height = 2, 
          width = 7)
button_window = canvas.create_window(160, 190, anchor=tk.NW, window=button)
button['font'] = myFont


button2 = tk.Button(root, text="Login",bg="#99643A",fg='white',command=tutorials,height = 2, 
          width =7)
button_window2 = canvas.create_window(350, 190, anchor=tk.NW, window=button2)
button2['font'] = myFont

root.mainloop()
