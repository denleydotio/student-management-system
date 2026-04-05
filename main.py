#main.py
import json # json file to save student details even after exiting system
from student import Student # import Student class from student.py

student_list = []  # list to save all students

def load_data():
    try: # try - except block to prevent crash if no json file found
        with open("students.json", "r") as file:
            saved_data = json.load(file) # saves data in json file to saved_data list

            for item in saved_data:
                s = Student(item["name"], item["age"], item["reg_No"]) # create Student object and assign attributes
                student_list.append(s) # add created Student object to student_list
            print("Data loaded successfully!")

    except FileNotFoundError:
        print("No data found. Start recording!")

def save_data():
    data_to_save = [] # list to hold created dictionaries to save Student class instances in json file
    for student in student_list:
        student_dict = {
            "name": student.name,
            "age": student.age,
            "reg_No": student.reg_No
        } # create dictionary to store in json file
        data_to_save.append(student_dict)

    with open("students.json", "w") as file:
        json.dump(data_to_save, file, indent=4)


def add_student():
    reg_No = input("Enter Reg_No: ")
    name = input("Enter name: ")
    try: # try - except block to verify input is int
        age = int(input("Enter age: "))
    except ValueError:
        print("Enter valid age")
        return # return to main loop

    for student in student_list:
        if student.reg_No == reg_No:
            print("Student already exists!")
            return # return to main function if reg_No already exists
                    #data not saved

    s = Student(name, age, reg_No)
    student_list.append(s) # add s to student_list
    save_data()
    print("Records saved")

def view_students():
    if len(student_list) == 0:
        print("No records exist")
        return
    for student in student_list:
        student.display_details()

def search_student():
    index = input("Enter Reg_No: ")
    for student in student_list:
        if index == student.reg_No:
            student.display_details()
            return  #break out of function if student found

    print(f"{index} does not exist in records!")

def update_student():
    index = input("Enter Reg_No: ") # request student to be updated
    for student in student_list:
        if index == student.reg_No: # check if input matches existing reg_No
            print("Input new details.")
            new_reg = input("Enter Reg_No: ")
            for other_student in student_list:
                if other_student.reg_No == new_reg and other_student != student: # check if reg_no already exists
                    print("Error! Reg_No belongs to another student.")
                    return # prevents updating to reg_no belonging to another student
            new_name = input("Enter name: ")
            try: # try - except to ensure age is int preventing crash
                new_age = int(input("Enter age: "))
            except ValueError:
                    print("Enter valid student details")
                    return # back to main function
            student.reg_No = new_reg
            student.name = new_name
            student.age = new_age
            print("Record Updated")
            save_data()
            return # kill function

    print(f"{index} does not exist!") # function wasn't killed so record not found

def delete_student():
    index = input("Enter Reg_No: ")
    for student in student_list:
        if index == student.reg_No:
            choice = input("Delete Record(Y/N): ") # ask if user wants to commit to deleting a record
            if choice.upper() == "Y":
                student_list.remove(student) # delete record from list
                print("Student deleted successfully!")
                save_data()
                return # exit function if student found
            else:
                print("Delete cancelled!")
                return

    print(f"{index} does not exist")

def main():
    load_data()
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
                save_data()
                print("System Exit")
                break
            case _: # checks for int ! 1 to 6
                print("Invalid Option! Select from 1 to 6")

main()

