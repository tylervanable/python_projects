"""
    Write a program that asks the user to enter the monthly costs for the following expenses
    incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
    maintenance. The program should then display the total monthly cost of these expenses,
    and the total annual cost of these expenses.

    Tyler
    4/15/24
"""


def calc_expenses(loan: float, insurance: float, gas: float, oil: float,
             tires: float, maintenance: float) -> float:
    """Calculate the total monthly sum of expenses for loan payment, insurance, gas, oil, tires,
       and maintenance."""

    # Annotate the variables.
    total_expenses: float

    # Calculate the sum of the total expenses.
    total_expenses = loan + insurance + gas + oil + tires + maintenance

    # Return the sum of the total expenses.
    return total_expenses

def calc_yearly_expenses(loan: float, insurance: float, gas: float, oil: float,
             tires: float, maintenance: float) -> float:
    """Calculate the total yearly sum of expenses for loan payment, insurance, gas, oil, tires,
       and maintenance."""

    # Annotate the variables.
    total_yearly_expenses: float

    # Calculate the sum of the total yearly expenses.
    total_yearly_expenses = (loan + insurance + gas + oil + tires + maintenance)*12

    # Return the sum of the total expenses.
    return total_yearly_expenses

def main() -> None:
    """Obtain the amount of money the user pays for their car's loan payment, insurance, gas,
       oil, tires, and maintenance every month."""

    # Annotate the variables and obtain their expense value from the user.
    loan: float = float(input("How much does your monthly loan cost? "))
    insurance: float = float(input("How much does your monthly insurance cost? "))
    gas: float = float(input("How much does your monthly gas cost? "))
    oil: float = float(input("How much does your monthly oil cost? "))
    tires: float = float(input("How much does your monthly tires cost? "))
    maintenance: float = float(input("How much does your monthly maintenance cost? "))

    # Invoke the total_expenses function.
    total_monthly_expenses = calc_expenses(loan, insurance, gas, oil, tires, maintenance)
    total_yearly_expenses = calc_yearly_expenses(loan, insurance, gas, oil, tires, maintenance)

    # Display the total expenses to the user.
    print("The total monthly expenses the user spends is: {}."
          .format(total_monthly_expenses))
    print("The total yearly expenses the user spends is: {}."
          .format(total_yearly_expenses))

main()
