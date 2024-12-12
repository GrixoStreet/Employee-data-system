employee_database = {} #Dictionary to store the employee data

#Function to display the menu
def menu_display():
    print("Employee database system")
    print("Operations List:-")
    print("1-Add employee \n2-Update salary \n3-Get employee details \n4-Delete employee \n5-Exit")

#Function to get the user choice
def user_choice():
    return input("Choose the operation: ")

#Function to add employees
def add_employee(emp_id , name , position, salary):
    employee_database[emp_id] = {
        "name_key" : name,
        "position_key" : position,
        "salary_key" : salary
    }
    print("===================================================")
    print(f"{employee_database[emp_id]["name_key"]} got added")

#Function to update employee's salary
def update_salary(emp_id , new_salary):
    if emp_id in employee_database:
        employee_database[emp_id]["salary_key"] = new_salary
        print("===================================================")
        print(f"{employee_database[emp_id]["name_key"]}'s salary got updated")

    else:
        print("===================================================")
        print("Employee doesn't exist please add them")

#Function to get employee data
def get_employee_details(emp_id):
    if emp_id in employee_database:
        print("===================================================")
        print(f"Name: {employee_database[emp_id]["name_key"]} \n"
              f"Position: {employee_database[emp_id]["position_key"]}\n"
              f"Salary: {employee_database[emp_id]["salary_key"]}")
    else:
        print("===================================================")
        print(None)

#Function to delete employee from the database
def delete_employee(emp_id):
    temp_employee_name = employee_database[emp_id]["name_key"]
    del (employee_database[emp_id])
    print("===================================================")
    print(f"{temp_employee_name} got removed")


#Main function
while True: #A While loop to keep  the application running
    print("===================================================")
    menu_display() #Calling the menu function
    userChoice = user_choice() #saving the user choice in a var
    userChoice = userChoice.lower() #changing the user choice into lower case
    #First choice
    if userChoice == "1" or userChoice == "add employee":
        empID = int(input("Enter the employee ID: "))
        name_input = input("Enter the employee name: ")
        position_input = input("Enter the employee position: ")
        salary_input = int(input("Enter the employee salary: "))
        add_employee(empID , name_input , position_input , salary_input )
    #Second choice
    elif userChoice == "2" or userChoice == "update salary":
        empID = int(input("Enter the employee ID: "))
        new_salary_input = int(input("Enter the new salary: "))
        update_salary(empID , new_salary_input)
    #Third choice
    elif userChoice == "3" or userChoice == "get employee details":
        empID = int(input("Enter the employee ID: "))
        get_employee_details(empID)
    #Fourth choice
    elif userChoice == "4" or userChoice == "delete employee":
        empID = int(input("Enter the employee ID: "))
        delete_employee(empID)
    #Fifth choice
    elif userChoice == "5" or userChoice == "exit":
        break
    #else
    else:
        print("Invalid choice")