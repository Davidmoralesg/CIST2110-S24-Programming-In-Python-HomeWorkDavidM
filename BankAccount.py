import sys


username ="JDOE52" 

PIN = 1234
BALANCE = 1000.00 
def authenticate() -> bool:
    """
    This function will authenticate the user by asking for their username and PIN
    The function will only prompt 3 times for the correct username and PIN


    Keyword arguments:

    Return: True if the user is authenticated, False otherwise
    """

    for i in range(3):
        input_username = input("Enter your username(Case Sensitive): ")
        input_username = input_username.strip()
        while input_username == '':
            print("You must enter a username")
            input_username = input("Enter your username(Case Sensitive): ")
            input_username = input_username.strip()

        input_pin = input("Enter your pin: ")
        input_pin = input_pin.strip()
        while input_pin == '':
            print("You must enter a pin")
            input_pin = input("Enter your pin: ")
            input_pin = input_pin.strip()
        if input_username == username and int(input_pin) == PIN:
            return True
        else:
            print("Invalid username or pin. Please try again. You have "
                  + str(2 - i) 
                  + " attempts remaining")
        if i == 2:
            print("Too many invalid attempts. Please try again later")
            sys.exit()
    return False 

def check_balance() -> float:
    """ This function will return the user's balance
    
    Args:
        none
    Returns:
        Float: The user's balance
    """
    return BALANCE


def print_balance() -> None:
    """ 
    This function will print the user's balance
    Args:
        none
    Returns:
        None
    """

print("Your balance is: $" + str(check_balance()))

def deposit(amount: float = None) -> float:
    """
    This function wil depost money into the user's account
    
    Args:
        amount (float, optional): The amount to deposit 
    Returns:
        Float: The user's balance after the deposit the amount
    """
    global BALANCE
    if amount is None:
        amount = float(input("How much would you like to deposit? $"))  
    BALANCE += amount
    print("Your balance is $" + str(amount))
    return BALANCE

def withdraw(amount: float = None) -> float:
    """
    This function will withdraw money from the user's account
    Args:
        amount (float, optional): The amount to withdraw from the balance.
        Defaults to None and will prompt the user to input the amount to withdraw
        
    Returns:
        Float: The user's balance after the withdraw of the amount
    """
    global BALANCE
    if amount is None:
        print_balance()
        amount = input("How much would you like to withdraw? $")
    while amount == '':
        print("You connot withdraw $0 or a negative amount. Please try agian")
        amount = input("How much would you like to withdraw? $")
    
    while amount <= 0:
        print("You must withdraw a positive amount")
        amount = float(input("How much would you like to withdraw? $"))

    while amount > BALANCE:
        print("You cannot withdraw more than your balance")
        amount = float(input("How much would you like to withdraw? $"))
    BALANCE -= float(amount)
    print("You have withdrawn $" + str(amount))
    return BALANCE

    
def main_menu() -> int:
    """ 
    This function will display the main menu and return the user's choice

    Returns:
        Int: The user's choice
    """
    print("Main Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
       
    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 4:
        print("Invalid choice. Please try again")
        choice = input("Enter your choice: ")
    return choice

def menu_logic(choice: int) -> None:
    """
    this function calls the appropriate function based on the user's choice should only be called in conjunction with the main_menu function
    
    Args:
        choice (int): The user's choice from the main_menu function (1-4) - this is checked in the main_menu function
    """
    
    if choice == 1:
        print_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Goodbye")
        sys.exit()


def main():
    """
    Main function to run the program
    Whether code is in this function will be run when the program is executed
    """
    
    print("Welcome to the Bank Account Managment System")
    if authenticate() is True:
        print("Authentication Successful!")
        
        
        while True:
            choice = main_menu()
            menu_logic(choice)
    

if __name__ == '__main__':
    main()
