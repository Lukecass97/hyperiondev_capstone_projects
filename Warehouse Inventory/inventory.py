#========Shoe class created==========
class Shoe:

    # Initialising the shoe attributes.
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
       
    # Method to get the cost of a shoe.
    def get_cost(self):
        return (self.cost)
            
    # Method to get the quatity of a shoe.
    def get_quantity(self):
        return (self.quantity)

    # Method to return a string representation of the class.
    def __str__(self):
        return f'''---------------------------------------
Counrty: {self.country}   
Code: {self.code}   
Product: {self.product}
Cost: R{self.cost}   
Quantity: {self.quantity}
---------------------------------------'''

# Empty list to hold the objects.
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    
    '''This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this 
    data and append this object into the shoes list.
    '''

    # try-except for error handling. 
    try:
        with open("inventory.txt", "r") as file:
            data = file.readlines()
            
            # Reading from index 1 to miss out top line of file.
            for lines in data[1:]:
                line = lines.strip().split(",")
                
                # Shoes object created.
                shoes = Shoe(line[0], line[1], line[2],
                            line[3], line[4])
                
                # Append object to shoe_list.
                shoe_list.append(shoes)
                
    except FileNotFoundError as error:
        print("The file you are trying to open does not exist.")
        print(error)


def capture_shoes():
    
    '''This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    # Requests user input to be used to create a shoe object.
    country = input("Enter the country where the shoe is stocked: ")

    code = input("Enter the shoe code: ")

    product = input("Enter the shoe name: ")

    cost = input("Enter the cost of the shoe (R): ")

    quantity = input("Enter the quantity of the shoe: ")

    # Object created containing user input.
    captured_shoe = Shoe(country, code, product, cost, quantity)

    # Appends object to shoe_list
    shoe_list.append(captured_shoe)    
   
    # Writes object to inventory.txt.
    with open("inventory.txt", "a") as file:
        file.write(f'''\n{captured_shoe.country},{captured_shoe.code},\
{captured_shoe.product},{captured_shoe.cost},{captured_shoe.quantity}''')

        print(f"{product} added to inventory.")

    
def view_all():
    
    '''This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. 
    '''

    # Iterating through shoe_list and printing all shoes.
    for shoe in shoe_list:
        print(shoe)


def re_stock():

    '''This function will find the shoe object with the lowest quantity,
    which is the shoes that needs to be re-stocked. Then will ask the user 
    if they want to add to this quantity of shoes and then update the 
    text file "inventory.txt".
    '''

    # Empty list to hold the quantities of shoes.
    quantity_list = []
    
    # Finding the quantitites of shoes in shoe_list.
    for shoe in shoe_list:
        shoe_quantity = int(shoe.get_quantity())
        
        # Appending quantities to quantity_list.
        quantity_list.append(shoe_quantity)

    # Use of min() to find the shoe with the lowest quantity.    
    lowest_stock = min(quantity_list)
    
    for shoe in shoe_list:
        if lowest_stock == int(shoe.quantity):

            while True:
                # Asks user if they would like to restock the shoe with the 
                # lowest stock.
                restock = input(f'''Quantity of {shoe.product} is {shoe.quantity}. 
Would you like to restock {shoe.product}?
Enter Y for yes or N for no:\n''').upper()
        
                if restock == "Y":
                    # try-except shows error if an integer is not entered.
                    while True:
                        try:
                            restock_amount = int(input('''Enter the amount you 
would like to restock by:\n'''))
                
                            previous_qty = int(shoe.quantity)
                            
                            # Calculate the new quantity.
                            new_qty = previous_qty + restock_amount

                            shoe.quantity = str(new_qty)
                            
                            # Informs user of the new quantity of shoe.
                            print(
f'''---------------------------------------
Product: {shoe.product}
Previous quantity: {previous_qty} 
Increased quantity: {restock_amount} 
New quantity: {new_qty}
---------------------------------------''')
                            break
                        
                        except ValueError:
                            print("Invalid entry! Please enter a number.")
                              
                    updated_shoe = f'''{shoe.country},{shoe.code},\
{shoe.product},{shoe.cost},{shoe.quantity}\n'''
                        
                    # Updates "inventory.txt" with new shoe quantity.
                    with open("inventory.txt", "r") as file:
                        data = file.readlines()

                        for lines in data:
                            line = lines.split(",")

                            if shoe.product == line[2]:
                                data[data.index(lines)] = updated_shoe

                    with open("inventory.txt", "w") as file:
                        for lines in data:
                            file.write(lines)
                    break

                # If "N" is selected, informs user that the shoe has not been
                # restocked. 
                elif restock == "N":
                    print(f"{shoe.product} not restocked.")
                    break
                
                # Error message for invalid entry.
                elif restock != "Y" or "N":
                    print(f'''Invalid entry! Please enter "Y" or "N".\n''')
                    
    
def search_shoe():

    '''This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    while True:
        # User inputs the code of the shoe they wish to search for.
        search = input(f'''Enter the code of the shoe you would like to
search for: ''').upper()
        
        # If code is in shoe_list, the shoe info will be printed to console.
        for shoe in shoe_list:
            if search == shoe.code:
                return shoe

        # If the code is not in shoe_list an error message is displayed.    
        else:
            print("Invalid code! Please try again.")
                               

def value_per_item():
    
    '''This function will calculate the total value for each item.
    Then print this information on the console for all the shoes.
    '''
    
    # Prints the total value of each shoe in shoe_list.
    for shoe in shoe_list:
        # Converting to float and integer to perform calculation.
        shoe_cost = float(shoe.get_cost())

        shoe_quantity = int(shoe.get_quantity())

        # Calculating total value for each item and round to 2 decimal places.
        total_value = round(shoe_cost * shoe_quantity, 2)

        print(
f'''---------------------------------------
Product: {shoe.product} 
Cost: R{shoe.cost}
Quantity: {shoe.quantity}
Total value: R{total_value}
---------------------------------------''')
    
    
def highest_qty():

    '''This function will determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    
    # Empty list to hold shoe quantities.
    quantity_list = []

    # Finding quantities of the shoes and appending to quantity_list.
    for shoe in shoe_list:
        shoe_quantity = int(shoe.get_quantity())

        quantity_list.append(shoe_quantity)

    # Use of max() to find the shoe with the highest quantity.
    highest_stock = max(quantity_list)

    for shoe in shoe_list:
        # Shoe with the highest stock is printed to the console as being
        # for sale.
        if highest_stock == int(shoe.quantity):
            print(
f'''---------------------------------------       
{shoe.product} quantity: {shoe.quantity}
{shoe.product} for sale!
---------------------------------------''')


#==========Main Menu=============
'''Menu created that executes each function above.'''

# Populate shoe_list.
read_shoes_data()

menu = True

while True:
    # try-except displays error message if an integer is not entered.
    try:
        user_choice = int(input(
'''\nHello! Below are the options available to you:
1: Add new shoe
2: View all shoes
3: Re-stock shoe
4: Search for specific shoe
5: See total value of each shoe
6: See highest quantity shoe
7: Exit
                            
Please enter the number of the option you would like to select: \n'''))
        
        if user_choice == 1:
            capture_shoes()

        elif user_choice == 2:
            view_all()

        elif user_choice == 3:
            re_stock()

        elif user_choice == 4:
            print(search_shoe())

        elif user_choice == 5:
            value_per_item()

        elif user_choice == 6:
            highest_qty()

        elif user_choice == 7:
            print("Goodbye!")
            exit()

        else:
            print("Incorrect input! Please try again.")
            continue

    except ValueError:
        print("Incorrect input! Please try again.")