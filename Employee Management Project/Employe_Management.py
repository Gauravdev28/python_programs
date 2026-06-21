# Employee Management App 
import json

try :
    with open("employees.json" , "r") as file :
        employees = json.load(file)
except :
    employees = {} # Creating a Dictonery to store All employee data 

def data_store() :
        with open("employees.json" , "w") as file :
            json.dump(employees, file , indent=4)

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
    data_store()
    print("Employee Added Successful")

# Update the Employee Details 
def update_employee():
    emp_id = int(input("Enter Employee ID :"))

    if emp_id in employees:
        name = input("Enter Empleyee Name :")
        emp_id = int(input("Enter Employee ID :"))
        department = input("Enter Department Name :")
        salary = int(input("Enter Employee Salary $ :"))

        employees[emp_id]["Name"] = name
        employees[emp_id]["department"] = department
        employees[emp_id]["salary"] = salary

        print("Employee Added Successfull ")
    else :
        print("Employee ID Not Found ")


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

        data_store()
        
        print("Employee Deleted Successful")

    else :
        print("Employee Not Found")


# Count of total Employee

def count_employee():
    print("Total Employees :" , len(employees))


# Printing Menu 
while True :
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. View Employee")
    print("4. Search Employee")
    print("5. Delete Employee")
    print("6. Count Employee")
    print("7. Exit")

    choice = input("Enter Your Choice (1-7) : ")

    if choice == "1" :
        add_employee()
    elif choice == "2" :
        update_employee()
    elif choice == "3" :
        view_employee()
    elif choice == "4" :
        search_employee()
    elif choice == "5" :
        delete_empleyee()
    elif choice == "6" :
        count_employee() 
    elif choice == "7" :
        print("Exiting Program")
        break
    else :
        print("Invalid Choice ")
