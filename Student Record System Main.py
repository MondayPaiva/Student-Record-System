# Luan Paiva, ID:75523. This is my project for python, Dorset college, first year second semester.
import os
os.system("pip install tabulate")
import csv
from tabulate import tabulate


# Studente class
class Student:

  def __init__(self, student_id, name, subjects, grades):
    self.student_id = student_id
    self.name = name
    self.subjects = subjects
    self.grades = grades

  def average(self):
    return sum(self.grades.values()) / len(self.grades)

# Main student list
students = []

# Add a new student
def add_student():
  student_id = input("Enter student ID: ")

  # Check for duplicati ID
  for s in students:
    if s.student_id == student_id:
      print("This ID already exists. Try another one.")
      return

  name = input("Enter student name: ")
  subjects = input("Enter subjects separated by comma: ").split(",")
  grades = {}

  for subject in subjects:
    try:
      grade = float(input(f"Grade for {subject.strip()}: "))
      if grade < 0:
        print("Grade cannot be negative.")
        return
      grades[subject.strip()] = grade
    except ValueError:
      print("Invalid number. Please try again.")
      return

  student = Student(student_id, name, subjects, grades)
  students.append(student)
  print("Student added!\n")


# View all students
def view_all_students():
  if not students:
    print("No student records found.\n")
    return

  table = []
  for s in students:
    table.append([
        s.student_id, s.name, ", ".join(s.subjects), s.grades,
        f"{s.average():.2f}"
    ])

  print(
      tabulate(table,
               headers=["ID", "Name", "Subjects", "Grades", "Average"],
               tablefmt="grid"))
# Search student by ID
def search_by_id():
  search_id = input("Enter student ID to search: ")
  for s in students:
    if s.student_id == search_id:
      print(
          tabulate([[
              s.student_id, s.name, s.subjects, s.grades, f"{s.average():.2f}"
          ]],
                   headers=["ID", "Name", "Subjects", "Grades", "Average"],
                   tablefmt="grid"))
      return
  print("Student not found.")


# View top-performing student
def top_student():
  if not students:
    print("No records available.\n")
    return
  top = max(students, key=lambda s: s.average())
  print(
      f"Top student: {top.name} (ID: {top.student_id}) - Average: {top.average():.2f}"
  )


# Save into to CSV
def save_to_csv():
  try:
    with open("students.csv", "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["ID", "Name", "Subjects", "Grades"])
      for s in students:
        writer.writerow([s.student_id, s.name, ",".join(s.subjects), s.grades])
    print("Data saved to students.csv\n")
  except Exception as e:
    print(f"Error saving file: {e}")


# Load from CSV
def load_from_csv():
  try:
    with open("students.csv", "r") as f:
      reader = csv.DictReader(f)
      for row in reader:
        subjects = row["Subjects"].split(",")
        grades = eval(row["Grades"])  # Assumes grades are stored as dictionary
        student = Student(row["ID"], row["Name"], subjects, grades)
        students.append(student)
    print("Data loaded from students.csv\n")
  except FileNotFoundError:
    print("File students.csv not found.\n")
  except Exception as e:
    print(f"Error loading file: {e}")


# Main menu
def menu():
  while True:
    print("""
---- STUDENT RECORD SYSTEM ----
1. Add new student
2. View all students
3. Search student by ID
4. View top-performing student
5. Save to CSV file
6. Load from CSV file
7. Exit
""")
    choice = input("Enter your choice: ")
    if choice == "1":
      add_student()
    elif choice == "2":
      view_all_students()
    elif choice == "3":
      search_by_id()
    elif choice == "4":
      top_student()
    elif choice == "5":
      save_to_csv()
    elif choice == "6":
      load_from_csv()
    elif choice == "7":
      print("Exiting the program...")
      break
    else:
      print("Invalid option. Try again.")


# Start the program here
menu()
