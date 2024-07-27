import calculator

user_informations = [
    {
        "id" : 1,
        "name" : "George",
        "balance" : 0
    },
    {
        "id" : 2,
        "name" : "Hagi",
        "balance" : 0
    }

] # created user informations like database table

def print_menu():
    print("***MENU***\n" 
      +"1 - Deposit Money... \n" 
      +"2 - Withdraw Money... \n" 
      +"3 - Calculate Deposit Money \n"
      +"4 - Change My Id... \n" 
      +"5 - Exit")

def withdraw_function(selectedUser):
    withdraw_value = int(input("Please Enter Your Value Withdraw "))
    if(selectedUser["balance"] < withdraw_value):
        print("You Don't Have Enough Value, Please Control your balance...")
    else:
        selectedUser["balance"] -= withdraw_value
        print("Withdraw instruction is successful... Your new balance : " + str(selectedUser["balance"]))

def deposit_function(selectedUser):
    deposit_value = int(input("Please Enter Your Value Deposit "))
    selectedUser["balance"] += deposit_value
    print("Deposit instruction is successful... Your new balance : " + str(selectedUser["balance"]))

def change_information(selectedUser):
    selectedUser["id"] = int(input("choose id for change... "))
    print(str(selectedUser["name"])+ " id change successful... new id -> " + str(selectedUser["id"])  + " -> your balance is : " + str(selectedUser["balance"]))

def calculator_function(choice):
    first = int(input("Please Enter Your First Value : "))
    second = int(input("Please Enter Your Second Value : "))

    if choice == 1:
        print(calculator.sum(first, second))
    if choice == 2:
        print(calculator.sub(first, second))
    if choice == 3:
        print(calculator.div(first, second))
    if choice == 4:
        print(calculator.mpy(first, second))
    
    


user_validation = input("Please Enter Your Id for perfom operations... ")

selected_user = {
    "id" : 0,
    "name" : "",
    "balance" : 0
}

for ids in user_informations:    
    if ids["id"] == int(user_validation):
        print("Welcome " + str(ids["name"]) + " and your balance is : " + str(ids["balance"]))
        selected_user["id"] = ids["id"]
        selected_user["name"] = ids["name"]
        selected_user["balance"] = ids["balance"]


print_menu()
instruction_choice = int(input("Please Enter Your Choice For Banking Instruction : "))

while(instruction_choice != 4):
    if(instruction_choice == 1):
       deposit_function(selected_user)

    if(instruction_choice == 2):
        withdraw_function(selected_user)

    if(instruction_choice == 3):
        calculator.print_calc_menu()
        calculation_choice = int(input("Please Enter Your Choice For Calculator Instruction : "))
        if calculation_choice == 5:
            print("Leaving Calculator...")
        else :
            calculator_function(calculation_choice)

    if(instruction_choice == 4):
        change_information(selected_user)

    if(instruction_choice == 5):
        print("Leaving our system thanks for choose us!")
        break

    instruction_choice = int(input("Please Enter Your Choice For Banking Instruction : "))

