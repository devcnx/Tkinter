""" A simple Hello, World! program using Tkinter. """


from tkinter import *
from tkinter import ttk


if __name__ == '__main__':
    root = Tk()  # Create the root window.
    root.title('Hello, Tkinter!')  # Set the title for the window.
    ttk.Button(root, text='Hello, World!').grid()  # Create a button with text and place it in the window.
    root.mainloop()  # Start the main event loop.
