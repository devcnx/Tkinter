""" Creation of a simple GUI to convert distance in feet to the equivalent distance in meters. """


from tkinter import *
from tkinter import ttk


# Performing the calculation.
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
        # NOTE: These values should be stored in constants, but for the sake of simplicity, they are hardcoded here.
    except ValueError:
        pass


if __name__ == '__main__':
    root = Tk()  # Create the root window.
    root.title('Feet to Meters')  # Set the title for the window.

    """ Creating a Content Frame """
    mainframe = ttk.Frame(root, padding='3 3 12 12')  # Create a frame to hold the content.
    mainframe.grid(column=0, row=0, sticky='NSEW')  # Place the frame in the window.
    root.columnconfigure(0, weight=1)  # Make the frame expandable.
    root.rowconfigure(0, weight=1)  # Make the frame expandable.

    # NOTE: Using a themed frame widget to hold the content ensures the background matches the rest of the window.

    """ Creating the Entry Widget """
    feet = StringVar()  # Creates a special string variable to hold the value of the entry widget.
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  # Creates an entry widget in the frame.
    feet_entry.grid(column=2, row=1, sticky='WE')

    # NOTE: When creating a widget, its parent must be specified. The parent is the widget that will contain the new
    # widget. In this case, the parent is the mainframe.

    """" Creating the Remaining Widgets """
    meters = StringVar()  # Creates a special string variable to hold the value of the label widget.
    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky='WE')  # Creates a label widget in the frame.

    ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=3, sticky='W')  # Creates a button in
    # the frame.

    ttk.Label(mainframe, text='feet').grid(column=3, row=1, sticky='W')
    ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky='E')
    ttk.Label(mainframe, text='meters').grid(column=3, row=2, sticky='W')

    """ Finishing Touches to the User Interface """
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)  # Adds padding around each widget.
    feet_entry.focus()  # Sets the focus to the entry widget.
    root.bind('<Return>', calculate)  # Binds the Enter key to the calculate function.

    root.mainloop()  # Start the main event loop.
