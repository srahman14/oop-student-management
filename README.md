# OOP Student Management System

A Student Management System (SMS) built using Python and Object-Oriented Programming (OOP) principles.

---

## Features
- Add, update, delete, and list students.
- Manage Undergraduate students with minors.
- Store and load student records using JSON.
- Input validation and exception handling.
- Interactive, menu-driven system.

---

## Technologies
- Python 3.x
- JSON (for file storage)
- OOP Concepts: Encapsulation, Inheritance, Abstraction

--- 

## Project Structure
```pysqlite
student_management/
│
├── models/
│   ├── student.py
│   ├── undergraduate.py
│
├── student_operations.py
├── serialisers.py
├── validation.py
├── storage.py
├── exceptions.py
├── main.py
│
├── students.json         # (auto-created after running program)
├── README.md
```
---

## Installation & Setup
- Ensure you have Python 3 installed
- Switch to student_management
```bash
cd student_management
```
- Run the program
```bash
python main.py
```

## How to use
You can:
- Follow the interactive menu in main.py
- Add new students.
- Update student details (including courses and minors).
- Delete existing students.
- List all students.
- Data is saved automatically in students.json.
