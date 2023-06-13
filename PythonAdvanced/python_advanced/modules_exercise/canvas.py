from tkinter import *


def create_root():
    root = Tk()

    root.geometry("700x600")
    root.title("GUI online shop")
    root.resizable(False,False)

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, col=0)

    return frame


frame = create_frame()
root = create_root()
