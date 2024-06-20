"""
    Display a window screen of 500x300 px., a title, and a label to the user.

    Tyler
    6/19/24
"""

# Import the tkinter module.
import tkinter

# Initialize the window screen that displays to the user.
window = tkinter.Tk()

# Display a title to the user with a "minimum size" of 500x300 px.
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Display a label text to the user with Arial font, 24 size font, and bold.
# and "pack" it to the very center of the screen.
first_label = tkinter.Label(text="First Label!", font=("Arial", 24, "bold"))
first_label.pack(expand=True) 





# Initalize the main loop to keep the window on the screen.
window.mainloop() # always on very end of program
