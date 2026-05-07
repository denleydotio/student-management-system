class Student:
    def __init__(self, name, age, reg_No):
            self.name = name
            self.age  = age
            self.reg_No = reg_No

    def display_details(self):
            print(f"Reg_No: {self.reg_No}\n"
                  f"Name: {self.name}\n"
                  f"Age: {self.age}\n")

