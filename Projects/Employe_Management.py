# Employee Management App 

employees = {} # Creating a Dictonery to store All employee data 

# Add Employee :
def add_employee() :  
    name = input("Enter Empleyee Name :")
    emp_id = int(input("Enter Employee ID :"))
    department = input("Enter Department Name :")
    salary = int(input("Enter Employee Salary $ :"))

    # Storing Employee Data in Dictonery and using id as a idefication id 
    employees[emp_id] = {
        "Name" : name,
        "Department" : department , 
        "Salary" : salary,
    }
    print("Employee Added Successful")


# Print all Employee Record :
def view_employee ():
    # If any employee record not exist 
    if not employees:
        print("No employees found.")
        return

    # If employee record exist it print all the record 
    for emp_id in employees:
        print("ID:", emp_id)
        print("Name:", employees[emp_id]["Name"])
        print("Department:", employees[emp_id]["Department"])
        print("Salary:", employees[emp_id]["Salary"])


# Searching Employee by their ID :
def search_employee():
    emp_id = int(input("Enter Employee ID :"))
    if emp_id in employees :
        print("Employee Found")
        print(f"ID :{emp_id}")


# Delete Employee Record :
def delete_empleyee() :
    emp_id = int(input("Enter Employee ID : "))
    if emp_id in employees :
        del employees[emp_id]
        print("Employee Deleted Successful")

    else :
        print("Employee Not Found")


# Printing Menu 
while True :
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Your Choice (1-5) : ")

    if choice == "1" :
        add_employee()
    elif choice == "2" :
        view_employee()
    elif choice == "3" :
        search_employee()
    elif choice == "4" :
        delete_empleyee() 
    elif choice == "5" :
        print("Exiting Program")
        break
    else :
        print("Invalid Choice ")
