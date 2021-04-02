# import modules
from tkinter import *
import tkinter.messagebox
import pymongo

# creat class for frontend UI


class Product:
    def __init__(self, root):  # defining my constructor

        self.root = root
        self.root.title = "Super Market Reaceipt Management System"
        self.root.geometry("1300x600")
        self.root.config(bg="orange")
        # creation the variables
        shop = StringVar()
        date_time = StringVar()
        total_cost = StringVar()
        shopped_line_items = StringVar()
        receipt_headers = StringVar()
        shopped_line_items = StringVar()

        # create the frames

        MainFrame = Frame(self.root, bg="red")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=50, pady=10, bg="white", relief=RIDGE)

        HeadFrame.pack(side=TOP)

        self.ITitle = Label(
            HeadFrame,
            font=("arial", 50, "bold"),
            fg="red",
            text=" Super Market Reaceipt ",
            bg="white",
        )
        self.ITitle.grid()

        OperationFrame = Frame(
            MainFrame,
            bd=1,
            width=1200,
            height=100,
            padx=50,
            pady=20,
            bg="white",
            relief=RIDGE,
        )
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(
            MainFrame,
            bd=1,
            width=780,
            height=80,
            padx=60,
            pady=20,
            bg="white",
            relief=RIDGE,
        )
        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(
            BodyFrame,
            bd=2,
            width=400,
            height=380,
            padx=20,
            pady=10,
            bg="orange",
            relief=RIDGE,
            font=("arial", 15, "bold"),
            text="Display Receipt Image ",
        )
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(
            BodyFrame,
            bd=2,
            width=400,
            height=380,
            padx=20,
            pady=10,
            bg="orange",
            relief=RIDGE,
            font=("arial", 15, "bold"),
            text="Display Receipt TEXT ",
        )
        RightBodyFrame.pack(side=RIGHT)

        # Add widget to the LeftBodyFrame
        # shop=StringVar()
        # date_time=StringVar()
        # total_cost=StringVar()
        # shopped_line_items=StringVar()
        # receipt_headers=StringVar()
        # shopped_line_items=StringVar()

        ################# # shop=StringVar()#############
        # lables insde the LeftBodyFrame
        # label no 1 Shop
        self.shop = Label(
            LeftBodyFrame,
            font=("arial", 15, "bold"),
            text="Shop:",
            padx=2,
            pady=2,
            bg="white",
            fg="blue",
        )
        self.shop.grid(row=0, column=0, sticky=W)
        self.shop = Entry(
            LeftBodyFrame, font=("arial", 20, "bold"), textvariable=shop, width=30
        )
        self.shop.grid(row=0, column=1, sticky=W)

        ################# # date_time=StringVar()#############
        # label no 2 date_time
        self.date_time = Label(
            LeftBodyFrame,
            font=("arial", 15, "bold"),
            text="date_time :",
            padx=2,
            pady=2,
            bg="white",
            fg="blue",
        )
        self.date_time.grid(row=1, column=0, sticky=W)
        self.date_time = Entry(
            LeftBodyFrame, font=("arial", 20, "bold"), textvariable=date_time, width=30
        )
        self.date_time.grid(row=1, column=1, sticky=W)

        ################# # total_cost=StringVar()#############
        # label no 3 total_cost
        self.total_cost = Label(
            LeftBodyFrame,
            font=("arial", 15, "bold"),
            text="total_cost:",
            padx=2,
            pady=2,
            bg="white",
            fg="blue",
        )
        self.total_cost.grid(row=2, column=0, sticky=W)
        self.total_cost = Entry(
            LeftBodyFrame, font=("arial", 20, "bold"), textvariable=date_time, width=30
        )
        self.total_cost.grid(row=2, column=1, sticky=W)

        ################# # shopped_line_items=StringVar()#############
        # label no 4 shopped_line_items
        self.shopped_line_items = Label(
            LeftBodyFrame,
            font=("arial", 15, "bold"),
            text="shopped_line_items:",
            padx=2,
            pady=2,
            bg="white",
            fg="blue",
        )
        self.shopped_line_items.grid(row=3, column=0, sticky=W)
        self.shopped_line_items = Entry(
            LeftBodyFrame, font=("arial", 20, "bold"), textvariable=date_time, width=30
        )
        self.shopped_line_items.grid(row=3, column=1, sticky=W)

        ################# # receipt_headers=StringVar()#############
        # label no 5 receipt_headers
        self.receipt_headers = Label(
            LeftBodyFrame,
            font=("arial", 15, "bold"),
            text="receipt_headers:",
            padx=2,
            pady=2,
            bg="white",
            fg="blue",
        )
        self.receipt_headers.grid(row=4, column=0, sticky=W)
        self.receipt_headers = Entry(
            LeftBodyFrame, font=("arial", 20, "bold"), textvariable=date_time, width=30
        )
        self.receipt_headers.grid(row=4, column=1, sticky=W)

        ################# # shopped_line_items=StringVar()#############
        # label no 6 shopped_line_items
        self.shopped_line_items = Label(
            LeftBodyFrame,
            font=("arial", 15, "bold"),
            text="receipt_headers:",
            padx=2,
            pady=2,
            bg="white",
            fg="blue",
        )
        self.shopped_line_items.grid(row=5, column=0, sticky=W)
        self.shopped_line_items = Entry(
            LeftBodyFrame, font=("arial", 20, "bold"), textvariable=date_time, width=30
        )
        self.shopped_line_items.grid(row=5, column=1, sticky=W)

        ###################################################################
        self.pad_space = Label(
            LeftBodyFrame,
            padx=2,
            pady=2,
        )
        self.pad_space.grid(row=6, column=1, sticky=W)
        self.pad_space = Label(
            LeftBodyFrame,
            padx=2,
            pady=2,
        )
        self.pad_space.grid(row=7, column=1, sticky=W)
        self.pad_space = Label(
            LeftBodyFrame,
            padx=2,
            pady=2,
        )
        self.pad_space.grid(row=8, column=1, sticky=W)

        self.pad_space = Label(
            LeftBodyFrame,
            padx=2,
            pady=2,
        )
        self.pad_space.grid(row=9, column=1, sticky=W)

        self.pad_space = Label(
            LeftBodyFrame,
            padx=2,
            pady=2,
        )
        self.pad_space.grid(row=10, column=1, sticky=W)


########################

# call the main
if __name__ == "__main__":
    root = Tk()
    application = Product(root)
    root.mainloop()
