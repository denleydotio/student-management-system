#main.py
import db_manager

def add_student():
    reg_No = input("Enter Reg_No: ").strip()
    name = input("Enter name: ").strip()
    try: # try - except block to verify input is int
        age = int(input("Enter age: "))
    except ValueError:
        print("Enter valid age")
        return # return to main loop

    success = db_manager.add_student_to_database(reg_No, name, age)
    if success:
        print("Student record created")
    else:
        print(f"Error: Student {reg_No} already exists")

def view_students():
    results = db_manager.display_all_students()
    for student in results:
        print(f"Reg: {student[1]} | Name: {student[2]} | Age: {student[3]}")

def search_student():
    reg_no = input("Enter reg_no: ")
    results = db_manager.search_students(reg_no)

    if not results:
        print(f"Student '{reg_no}' not found")
    else:
        for student in results:
            print(f"Reg: {student[1]} | Name: {student[2]} | Age: {student[3]}")

def update_student():
    reg_no = (input("Enter reg_no: "))
    print("Select record to update")
    print("  1. Student reg_no")
    print("  2. Student name")
    print("  3. Student age")
    option = int(input("Select option: "))

    match option:
        case 1:
            reg_no_new = input("Enter Reg_No: ")
            success = db_manager.update_student_reg(reg_no_new, reg_no)
            if success:
                print("Update saved")
            else:
                print(f"Student {reg_no} not found")
        case 2:
            name = input("Enter name: ")
            success = db_manager.update_student_name(name, reg_no)
            if success:
                print("Update saved")
            else:
                print(f"Student {reg_no} not found")
        case 3:
            try:
                age = int(input("Enter age:"))
            except ValueError:
                print("Enter valid input")
                return
            success = db_manager.update_student_age(age, reg_no)
            if success:
                print("Update saved")
            else:
                print(f"Student {reg_no} not found")
        case _:
            print("Enter valid input")
            return

def delete_student():
    reg_no = (input("Enter reg_no: "))
    validation = input("Proceed to delete(y/n): ")
    if validation.upper() == "Y":
        db_manager.delete_student_record(reg_no)
        print("Student record deleted!")
    elif validation.upper() == "N":
        print("Halting delete procedure!")
        return

    else:
        print("Input valid choice!")
        return

def main():
    db_manager.setup_database()
    while True:
        print("=====Student Management System=====")
        print("     1. View Students")
        print("     2. Add Student")
        print("     3. Search Student")
        print("     4. Update Student")
        print("     5. Delete Student")
        print("     6. Exit")
        try: # verify if input is integer
            option = int(input("Select option: "))

        except ValueError:
            print("Invalid Option! Select from 1 to 6")
            continue # if not int, back to top of while loop

        match option:
            case 1:
                view_students()
            case 2:
                add_student()
            case 3:
                search_student()
            case 4:
                update_student()
            case 5:
                delete_student()
            case 6:
                print("System Exit")
                break
            case _: # checks for int ! 1 to 6
                print("Invalid Option! Select from 1 to 6")

if __name__ == "__main__":
    main()

