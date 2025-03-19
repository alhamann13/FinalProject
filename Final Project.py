# Final STEM 103 Project for Sim Sandhu and Andrew Hamann

def userInput(progPrompt): 
    while True:
        try:   
            userValue = float(input(progPrompt)) # Float number for user input
            return userValue
        except ValueError: 
            print("Invalid input. Please enter your monthly income amount: ") # Will kick user out if their input is invalid

def displayBudget(userIncome, userExpenses): # Function for the income and expenses 
        
    print("\n||||| Monthly Budget Overview |||||") # Header for the budget overview section after all 

    print(f"\nTotal Monthly Net Income: ${userIncome:.2f}") # Prints the monthly income from the user, to 2 decimal places
    
    totalExpenses = sum(userExpenses.values()) # Adds the amounts entered from each expense category, separates the value from the category, to 2 decimal places
    print(f"Total Monthly Expenses: ${totalExpenses:.2f}")

    moneyRemaining = userIncome - totalExpenses # Calculates the entered expense amounts from the entered income, to 2 decimal places
    print(f"Remaining Funds: ${moneyRemaining:.2f}")

    remainingPercent = (moneyRemaining / userIncome) * 100 # Formula to calculate the remaining percentage for the If/Else section below

    print("\nYour Listed Monthly Expenses:") # Heading for the list of user entered monthly expenses

    for expenseCategory, expenseAmount in userExpenses.items(): 
        print(f" - {expenseCategory}: ${expenseAmount:.2f}") # Lists the expenses with the dollar amounts to 2 decimal places

    if remainingPercent <= 15:
        print(f"\nYou have {remainingPercent:.0f}% of your monthly budget. Think about better budgeting strategies for next month.\n")
    elif remainingPercent > 15 and remainingPercent <= 25:
        print(f"\nNot a bad job budgeting. You can do better than {remainingPercent:.0f}% remaining of your monthly budget.\n")
    else:
        print(f"\nGreat job budgeting this month! You have {remainingPercent:.0f}% of your monthly income remaining!\n")

userIncome = userInput ("Enter your net monthly income: $") # Program starts here 

userExpenses = {}

while True: # Loops to continuously ask the user to input an expense category/name
    expenseCategory = input("Enter a monthly expense category/name (or type 'done' to see your results): ") # Asks the user to enter an expense category/name
    if expenseCategory.lower() == 'done': # Enter done to exit the loop and calculate all user inputs
        break
    else:
        expenseAmount = userInput(f"Enter amount for {expenseCategory}: $") # Asks user to enter the amount for the previously entered category
        userExpenses[expenseCategory] = expenseAmount

displayBudget(userIncome, userExpenses)
