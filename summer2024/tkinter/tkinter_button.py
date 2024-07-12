"""
     Display a button and entry areausing tkinter to the user. 
     When the button is clicked, print text
     in the console and update the label with the 
     entry text from the user. 
     Demonstrate the use of .get() to obtain a user entry. 
"""


# Import the tkinter module.
import tkinter

# Display the 500x300 window with a title
window = tkinter.Tk()
window.title("My Next GUI Program")
window.minsize(width=500, height=300)

# Display a label.
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack()

# Change the label text.
my_label["text"] = "This is the new text..."

# Change the label text a different way.
my_label.config(text="This is the NEW, new text...")

# Define a button_clicked function.
def button_clicked() -> None:
    """Display a message to the user when the button is clicked."""

    # Display the message, change the title.
    print("I got clicked...")
    window.title("Button clicked...")
    my_label.config(text="CLICKETH THE BUTTONETH")

    # Store the user input and display it.
    new_text = input.get()
    my_label.config(text=new_text.upper())
    
# Create a button.
button = tkinter.Button(text="Click me please", command=button_clicked)
button2 = tkinter.Button(text="Store the text", command=button_clicked)
button.pack()
button2.pack()

# Display a typable Entry widget to the user.
input = tkinter.Entry(width=40)
input.pack()

# Store the user input as a variable.

# Execute main loop
tkinter.mainloop()
