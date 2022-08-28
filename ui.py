import tkinter
import constants


class User_Interface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Pomodoro")
        print("running gui")
        self.window.mainloop()
