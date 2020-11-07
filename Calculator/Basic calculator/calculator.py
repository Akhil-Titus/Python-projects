from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Py Calculator")

        # create screen widget
        self.screen = Text(master, state='disabled', width=30,
                            height=3,background='yellow', foreground='blue')

        # screen's  position in window
        # columnspan = 4 => in a size of 4 column
        #padx,pady =5 => border size of the particular grid ie screen       
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        # initialise screen value as empty
        self.equation= ''

root = Tk()
my_gui = Calculator(root)
root.mainloop()
