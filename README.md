# Student Management System
A lightweight, terminal - based python application to manage student records. 
This project moves away from manual management of records, providing an automated way to add, view, update, search and delete student records.

## Features
* **Interactive CLI Menu:** Easy to read and use terminal based interface implementing modern "match - case" providing structural pattern matching.
* **Data Validation:** Prevents invalid data input(like typing text where numbers are required) and duplicate Registration Numbers being saved.
* **Atomic Updates:** Existing data is secured when updating records by ensuring all changes are validated before commiting.
* **Persistent Storage:** Records are saved and loaded using JSON. No data is lost after sessions.

## Tech Stack
* **Language:** Python 3.12
* **Storage:** JSON(Built in Python Module)

## How To Run
1. Clone the repository to your local machine.

2. Ensure you have python installed.
3. Navigate to the folder the main file is stored in and run `python main.py` on terminal.

## What I Learned
* Implementing OOP and using custom classes.
* Using git and github for version control.
* Implementing persistent storage by using JSON dictionaries to store python objects.
* Using try - except blocks to ensure data validation during user entry.

## Challenges Overcome
* **Data Corruption when Updating Records:** Initially if a user crashed the program during update operation, incomplete data would be recorded.
    * *Fix:* Implementing Atomic Updates where all details are input to temporary variables then validated before the updates are commited. if an error occurs, original data remains unchanged.

