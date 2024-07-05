"""
    Mile to Km Converter

"""

from tkinter import *


# Define the calc_button_clicked function.
def calc_button_clicked():
    """When calc_button_clicked, calculate mile(s) to km.
       Return to main."""

    # Annotate the local variables and define the constant.
    MILES_TO_KM_CONVERSION: float = (8/5)

    conversion: float

    # Obtain the conversion number from the entry widget.
    miles = float(convert_number.get())

    # Calculate the conversion.
    conversion = float(MILES_TO_KM_CONVERSION * miles)

    # Update the calculation label.
    conversion.configure(text=f"{conversion:.2f}")

    # Return the conversion.
    return conversion

# Define the main function.
def main():

    # Display the GUI program to the user.
    window = Tk()
    window.title("Mile to Km. Converter")
    window.minsize(width=500, height=300)
    window.config(padx=100, pady=100)
    
    # Display a user entry in row 1, column 2. Assign the user's
    # number to a variable.
    convert_num = Entry(width=10)
    convert_num.grid(column=1, row=0)

    # Display the word 'miles' in row 1, column 3.
    miles_label = Label(text="miles", font=("Arial", 24, "bold"))
    miles_label.grid(column=2, row=0)

    # Display the words 'is equal to' in row 2, column 1.
    equal_to_label = Label(text="is equal to", font=("Arial", 24, "bold"))
    equal_to_label.grid(column=0, row=1)

    # Display the calculation to the user, else display 0 at first.
    # Display in row 2, column 2.
    calc_label = Label(text=0.00, font=("Arial", 24, "bold"))
    calc_label.grid(column=1, row=1)

    # Display the abbreviation 'Km' in row 2, column 3.
    km_label = Label(text="Km.", font=("Arial", 24, "bold"))
    km_label.grid(column=2, row=1)

    # Display the button with the word 'Calculate' in
    # row 3, column 2.
    calc_button = Button(text="Calculate", command=calc_button_clicked)
    calc_button.grid(column=1, row=2)

    # Loop through the main event loop.
    window.mainloop()


main()
