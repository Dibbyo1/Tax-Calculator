"""
Problem: Build an income tax calculator, calculating the amount of money to be paid as tax and the after tax salary.
At first, ask the age of the user. If the user is below 18 years old, it means he/she is not an adult and is not
required to pay taxes in this scenery. If so, mention how long they have to wait to become eligible to pay tax.
For people aged 18 years old or more, ask if they are a citizen of this country or not. If they are citizen, the lower
income earners are going to have some reduced tax rates which will be described later. If the user is not a citizen,
the tax rate is fixed 30% for all income range. Ask the user for their annual income.
Calculate the amount of tax they have to pay and the after tax salary.

Citizen income tax rate according to income:
Income($)                                           Tax Rate
0-10000                                             1%
10000-20000                                         2%
greater than 20000-less than or equal to 30000      3%
greater than 30000-less than or equal to 40000      4%
greater than 40000-less than or equal to 50000      5%
greater than 50000-less than or equal to 60000      6%
greater than 60000-less than or equal to 70000      7%
greater than 70000-less than or equal to 80000      8%
greater than 80000-less than or equal to 90000      9%
greater than 90000-less than or equal to 100000     10%
greater than 100000                                 20%
"""

def tax_calculator():
    # This is a function which consists of the whole coding for the income tax calculator.
    age = abs(int(input("What is your age? ")))
    # The age of the user has been asked for input. Only integer values will be taken as input.
    short = abs(int(18-age))
    # Calculates how short is the user's age of being 18 years old.
    if age < 17:
        print("You are too young! Come back in " + str(short) + " years.")
        # The if function checks if the age input is less than 17 years old.
        # The print function prints a statement and time for the user to be eligible to pay tax.
    elif age == 17:
        print("You are too young! Come back in a year.")
        # The if function checks if the age input is 17 years old.
        # The print function prints a statement stating that the user should come back in a year to pay tax.
    elif age >= 18:
        citizen = str(input("Are you a citizen of this country? Yes/No "))
        citizen1 = True
        if citizen == "Yes":
            citizen1 = True
            # Boolean saying that if "citizen" is "Yes", then "citizen1" is set to be True.
            income = abs(int(input("What is you annual income? $")))
            # The input function asks for an integer value of annual income.
            if income <= 10000:
                tax_rate = income*0.01
                # The if function checks if the income is less than or equal to $10000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income > 10000 and income <= 20000:
                tax_rate = income*0.02
                # The if function checks if the income is greater than $10000 and less than or equal to $20000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 20000 and income <= 30000:
                tax_rate = income*0.03
                # The if function checks if the income is greater than $20000 and less than or equal to $30000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 30000 and income <= 40000:
                tax_rate = income*0.04
                # The if function checks if the income is greater than $30000 and less than or equal to $40000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 40000 and income <= 50000:
                tax_rate = income*0.05
                # The if function checks if the income is greater than $40000 and less than or equal to $50000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 50000 and income <= 60000:
                tax_rate = income*0.06
                # The if function checks if the income is greater than $50000 and less than or equal to $60000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 60000 and income <= 70000:
                tax_rate = income*0.07
                # The if function checks if the income is greater than $60000 and less than or equal to $60000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 70000 and income <= 80000:
                tax_rate = income*0.08
                # The if function checks if the income is greater than $70000 and less than or equal to $80000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 80000 and income <= 90000:
                tax_rate = income*0.09
                # The if function checks if the income is greater than $80000 and less than or equal to $90000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income> 90000 and income <= 100000:
                tax_rate = income*0.10
                # The if function checks if the income is greater than $90000 and less than or equal to $100000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            elif income > 100000:
                tax_rate = income*0.20
                # The if function checks if the income is greater than $100000.
                # If the "if" requirement is met, it calculates the tax amount to pay.
            salary_after_tax = income - tax_rate
            # This calculates the salary after tax.
            for i in range(1):
                print("You have to pay $", tax_rate, " as tax.")
                print("You have an after tax salary of $", salary_after_tax)
                # The for loop runs one time and is used to print two statements, each one time.
                # The first statement prints the amount of tax to pay.
                # The second statement prints the amount of salary after tax.
        elif citizen == "No":
            citizen1 = False
            if citizen1 == False:
                # Boolean saying that if "citizen" is "No", then "citizen1" is set to be False
                # If "citizen1" is False, then the following codes will run.
                income = abs(int(input("What is you annual income? $")))
                tax_rate = income * 0.3
                salary_after_tax = income - tax_rate
            for i in range(1):
                print("You have to pay $", tax_rate, " as tax.")
                print("You have an after tax salary of $", salary_after_tax)
                # The for loop is used to print two statements, each one time.
                # The first statement prints the amount of tax to pay.
                # The second statement prints the amount of salary after tax.
tax_calculator()
# The function concludes here.
