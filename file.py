from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk

# creat showimage function
def showimage():
    fln = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="select Image File",
        filetype=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")),
    )
    img = Image.open(fln)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    # to show the image
    lbl.configure(image=img)
    lbl.image = img


root = Tk()

# creating a frame
frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="browse Image", command=showimage)
btn.pack(
    side=tk.LEFT,
)

# creat another button
btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)


root.title("Image Browser")
root.geometry("300x350")
root.mainloop()
