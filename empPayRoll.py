#Employee Payroll System
# Initialize an empty dictionary to store employee data
employees = {}


def register_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee already exists.")
        return
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    salary = float(input("Enter Employee Salary: "))
    employees[emp_id] = {"name": name, "position": position, "salary": salary, "attendance": {}}
    print("Employee registered successfully.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Employee not found.")
        return
    name = input("Enter updated name (leave empty to keep current): ")
    position = input("Enter updated position (leave empty to keep current): ")
    salary = input("Enter updated salary (leave empty to keep current): ")

    if name:
        employees[emp_id]["name"] = name
    if position:
        employees[emp_id]["position"] = position
    if salary:
        employees[emp_id]["salary"] = float(salary)

    print("Employee information updated successfully.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def mark_attendance():
    emp_id = input("Enter Employee ID for attendance: ")
    if emp_id in employees:
        date = input("Enter date (YYYY-MM-DD): ")
        if date not in employees[emp_id]["attendance"]:
            employees[emp_id]["attendance"][date] = "Present"
            print("Attendance marked as 'Present'.")
        else:
            print("Attendance for this date already marked.")
    else:
        print("Employee not found.")


def calculate_salary():
    emp_id = input("Enter Employee ID to calculate salary: ")
    if emp_id in employees:
        hours_worked = sum(1 for status in employees[emp_id]["attendance"].values() if status == "Present")
        salary = employees[emp_id]["salary"]
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * (salary / 40 * 1.5)
            total_salary = salary + overtime_pay
        else:
            total_salary = salary
        print(f"Total Salary for Employee {emp_id}: RS{total_salary:.2f}")
    else:
        print("Employee not found.")


while True:
    print("\nEMPLOYEE PAYROLL SYSTEM")
    print("1. Register Employee")
    print("2. Update Employee Information")
    print("3. Delete Employee")
    print("4. Mark Attendance")
    print("5. Calculate Salary")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        mark_attendance()
    elif choice == "5":
        calculate_salary()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
