# Student Management System
A Python-based CLI application to manage student records with a MYSQL backend. 
This project moves away from manual management of records, providing an automated way to add, view, update, search and delete student records.

## Features
* **Interactive CLI Menu:** Easy to read and use terminal based interface implementing modern "match - case" providing structural pattern matching.
* **Data Validation:** Prevents invalid data input(like typing text where numbers are required) and duplicate Registration Numbers being saved.
* **Atomic Updates:** Existing data is secured when updating records by ensuring all changes are validated before commiting.
* **MYSQL relational database integration.**

## Tech Stack
* **Language:** Python 3.12
* **Storage:** MYSQL server installed and running locally

## How To Run
1. Clone the repository to your local machine.
'git clone[https://github.com/denleydotio/student-management-system.git]'
2. Set up the Environment Variables
* Rename '.env.example' file to '.env'
* Open '.env' and fill in your local MYSQL credentials 
3. Install Dependencies
* 'pip install mysql-connector-python python-dotenv'
4. Run the application
* 'python main.py' (Note: The app will build the required database and table automatically on the first run)

## What I Learned
* Implementing OOP and using custom classes.
* Using git and github for version control.
* Implementing persistent storage by using MYSQL server to store python objects.
* Using try - except blocks to ensure data validation during user entry.
