from tkinter import *
from tkinter import filedialog
import tkinter as tk
import pytesseract
from PIL import Image
import os


def readTxt1():
    fln = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="select Image File",
        filetype=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")),
    )
    t1.set(fln)
    # txt2.delete("1.0", "end")
    # txt2.insert(INSERT, pytesseract.image_to_string(Image.open(fln)))

    #  Get OCR output using Pytesseract

    custom_config = r"--oem 3 --psm 6"
    txt3.delete("1.0", "end")
    # txt2 = pytesseract.image_to_string(Image.open(fln), config=custom_config)
    txt3.insert(
        INSERT, pytesseract.image_to_string(Image.open(fln), config=custom_config)
    )
    # img = Image.open(fln)
    # img.thumbnail((350, 350))
    # img = ImageTk.PhotoImage(img)
    # # to show the image
    # lbl.configure(image=img)
    # lbl.image = img


root = Tk()

t1 = StringVar()
wrapper = LabelFrame(root, text="Choose File")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

wrapper2 = LabelFrame(root, text="Receipt Image ")
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

wrapper3 = LabelFrame(root, text="Image Text")
wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

txt = Entry(wrapper, textvariable=t1)
txt.pack(side=tk.LEFT, padx=10, pady=10)

btn = Button(wrapper, text="Browse", command=readTxt1)
btn.pack(side=tk.LEFT, padx=10, pady=10)

btn2 = Button(wrapper, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10, pady=10)

txt2 = Text(wrapper2)
txt2.pack(padx=10, pady=10)

txt3 = Text(wrapper3)
txt3.pack(padx=10, pady=10)


root.geometry("900x650")
# root.title("text reader")
root.resizable(False, False)
root.mainloop()