import math 

# Informing the user of the calculations and prompting them to 
# choose the one they want to proceed.
print('''investment - to calculate the amount of interest you'll
earn on your investment''')

print("bond - to calculate the amount you'll have to pay on a home")

# Using the .casefold() method so the user can enter their 
# answer in upper or lower case. 
calculation = input('''Enter either "investment" or "bond" from the menu above
to proceed: ''').casefold()

investment = "investment"

bond = "bond"

calculation in (investment, bond) 

while True:
    calculation in (investment, bond)
        
    # Prompting user to input a deposit amount and then storing that 
    # amount in a float variable called "deposit". 
    if calculation in investment:
        deposit = input("Enter the amount of money you are depositing: \n$")
        deposit = float(deposit)
        
        # Prompting the user to input the interest rate and storing in 
        # a variable called "interest_rate". Dividng the interest rate
        # by 100 to ensure the calculation is correct.
        interest_rate = input("Enter the interest rate %: \n")

        interest_rate = float(interest_rate)

        interest_rate = interest_rate / 100
        
        
        # Prompting the user to input the number of years they want to 
        # invest and storing in an integer variable called "num_of_years".
        num_of_years = input("Enter the number of years you plan to invest: \n")
        
        num_of_years = int(num_of_years)
        
        # Prompting user to input the type of interest they want and
        # storing in a variable called "interest".
        # Using the .casefold() method so the user can enter in either
        # upper or lower case.
        interest = input('''Enter the type of interest, either "simple" 
or "compound": \n''').casefold()
        
        simple = "simple"
        
        compound = "compound" 
        
        interest == simple or compound
        
         # Printing the calculated amount to 2 decimal places in an 
         # f string style. 
         # Using nested if-elif statements so the program bypasses
         # these if "bond" is entered at the start. 
        while True:
            interest == simple or compound
            
            if interest == simple:
                total_amount = deposit * (1 + (interest_rate)*num_of_years) 
                
                total_amount = float(round(total_amount, 2))
                
                print(f'''The appropriate amount you will recieve after the given
period at the specified interest rate is: \n${total_amount}''')
                break
                
            elif interest == compound:
                total_amount = deposit * math.pow((1 + interest_rate), num_of_years)
                
                total_amount = float(round(total_amount, 2))
                
                print(f'''The appropriate amount you will recieve after the given 
period at the specified interest rate is: \n${total_amount}''')
                break
             
            else: 
                print("Error!")

                # Using the .casefold() method so the user can enter 
                # their answer in either upper or lower case.  
                interest = input('''Enter the type of interest, either "simple" 
or "compound": \n''').casefold()
        break 
        
        # Using a while loop to enable the user to re-enter if they 
        # write something other than "simple" or "compound". 

    # Prompting the user to input the present value of the house
    # and storing in a float variable called "house_value".  
    elif calculation in bond:
        house_value = input("Enter the present value of the house: \n$")
        
        house_value = float(house_value)
        
        # Prompting the user to input the interest rate and storing in
        # a float variable called "interest_rate2".
        # Dividing the interest rate by 100 and then the answer of 
        # that by 12 to ensure the calculation will be correct.
        interest_rate2 = input("Enter the interest rate %: \n")
        
        interest_rate2 = float(interest_rate2)
        
        interest_rate2 = ((interest_rate2 / 100) / 12)
        
        # Prompting the user to input the number of months they plan to 
        # repay and storing in an integer variable called "num_of_months"
        num_of_months = input('''Enter the number of months you plan to take
to repay the bond: \n''')
        
        num_of_months = int(num_of_months)
        
        # Calculating the "bond_repayment" and printing to 2 decimal places
        # in an f string style. 
        bond_repayment = (interest_rate2 * house_value)/(1 - (1 + interest_rate2)**(-num_of_months))
        
        bond_repayment = float(round(bond_repayment, 2)) 
        
        print(f'''The total you will have to repay each month is: \n${bond_repayment}''')
        break

    else:
        print("Error!")
        calculation = input('''Enter either "investment" or "bond" from the menu above
to proceed: ''').casefold()
    
    # Using the .casefold() method so the user can enter in upper
    # or lower case.
    # Using a while loop so the user can re-enter if they wrote 
    # something other than "investment" or "bond".


    # I used https://www.dataquest.io/blog/tutorial-using-if-statements-in-python/ 
    # to help solve this problem. This resource helped me to understand 
    # how to use nested if statements. 
    # I used https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid
    # to help add while loops. 
    # I used https://stackoverflow.com/questions/12719586/how-to-let-python-recognize-both-lower-and-uppercase-input
    # to understand how to use the .casefold() method.