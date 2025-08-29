from main_app.models import *

def add_subject():
    name = input("Enter subject name: ")
    subject = Subject.objects.create(name=name)
    print(f"Subject '{name}' has been added.")

def add_teacher():
    name = input("Enter teacher's first name: ")
    surname = input("Enter teacher's surname: ")
    email = input("Enter teacher's email: ")
    age = int(input("Enter teacher's age: "))
    subjects = Subject.objects.all()
    if not subjects:
        print("No subjects available. Please add a subject first.")
        return
    print("Available subjects:")
    for subject in subjects:
        print(f"{subject.id} - {subject.name}")
    subject_id = int(input("Enter subject ID: "))
    subject = Subject.objects.get(id=subject_id)
    teacher = Teacher.objects.create(name=name, surname=surname, email=email, age=age, subject=subject)
    print(f"Teacher {name} {surname} has been added.")

def add_class():
    name = input("Enter class name: ")
    number = int(input("Enter class number: "))
    teachers = Teacher.objects.all()
    if not teachers:
        print("No teachers available.")
        return
    print("Available teachers:")
    for teacher in teachers:
        print(f"{teacher.id} - {teacher.name} {teacher.surname}")
    teacher_id = int(input("Enter teacher ID: "))
    teacher = Teacher.objects.get(id=teacher_id)
    my_class = Class.objects.create(name=name, number=number, teacher=teacher)
    print(f"Class {name} created.")

def add_student():
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    email = input("Enter student email: ")
    age = int(input("Enter student age: "))
    classes = Class.objects.all()
    if not classes:
        print("No classes available.")
        return
    print("Available classes:")
    for my_class in classes:
        print(f"{my_class.id} - {my_class.name}")
    my_class_id = int(input("Enter class ID: "))
    my_class = Class.objects.get(id=my_class_id)
    student = Student.objects.create(name=name, surname=surname, email=email, age=age, student_class=my_class)
    print(f"Student {name} {surname} has been added.")

def add_schedule():
    class_id = int(input("Enter class ID: "))
    subject_id = int(input("Enter subject ID: "))
    teacher_id = int(input("Enter teacher ID: "))
    day_of_week = input("Enter day of the week (e.g. Monday): ")
    time = input("Enter time (HH:MM:SS): ")
    
    Schedule.objects.create(school_class_id=class_id, subject_id=subject_id, teacher_id=teacher_id, day_of_week=day_of_week, time=time)
    print(f"Schedule for class {class_id} has been added.")

def add_grade():
    student = int(input("Enter student ID: "))
    subject = int(input("Enter subject ID: "))
    grade = input("Enter grade: ")
    date = input("Enter date (YYYY-MM-DD): ")
    Grade.objects.create(student_id=student, subject_id=subject, grade=grade, date=date)
    print(f"Grade {grade} for student {student} in subject {subject} has been added.")

def list_students():
    students = Student.objects.all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Surname: {student.surname}, Age: {student.age}, Email: {student.email}, Class: {student.student_class.name}")
        
def list_teachers():
    teachers = Teacher.objects.all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}, Surname: {teacher.surname}, Age: {teacher.age}, Email: {teacher.email}, Subject: {teacher.subject.name}")

def list_subjects():
    subjects = Subject.objects.all()
    for subject in subjects:
        print(f"ID: {subject.id}, Name: {subject.name}, Description: {subject.description if hasattr(subject, 'description') else 'No description'}")

def list_classes():
    classes = Class.objects.all()
    for school_class in classes:
        print(f"ID: {school_class.id}, Name: {school_class.name}, Number: {school_class.number}, Teacher: {school_class.teacher.name}")

def list_schedules():
    schedules = Schedule.objects.all()
    for schedule in schedules:
        print(f"ID: {schedule.id}, Class: {schedule.school_class.name}, Subject: {schedule.subject.name}, Teacher: {schedule.teacher.name}, Day: {schedule.day_of_week}, Time: {schedule.time}")

def list_grades():
    grades = Grade.objects.all()
    for grade in grades:
        print(f"ID: {grade.id}, Student: {grade.student.name}, Subject: {grade.subject.name}, Grade: {grade.grade}, Date: {grade.date}")
    
def main():
    while True:
        print("\n--- School Management System ---")
        print("1. How to use this program")
        print("2. Add Student")
        print("3. Add Teacher")
        print("4. Add Subject")
        print("5. Add Class")
        print("6. Add Schedule")
        print("7. Add Grade")
        print("8. List Students")
        print("9. List Teachers")
        print("10. List Subjects")
        print("11. List Classes")
        print("12. List Schedules")
        print("13. List Grades")
        print("14. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("This program allows you to manage a school's data including students, teachers, subjects, classes, schedules, and grades. Use the menu options to add or list data.")
        elif choice == '2':
            add_student()
        elif choice == '3':
            add_teacher()
        elif choice == '4':
            add_subject()
        elif choice == '5':
            add_class()
        elif choice == '6':
            add_schedule()
        elif choice == '7':
            add_grade()
        elif choice == '8':
            list_students()
        elif choice == '9':
            list_teachers()
        elif choice == '10':
            list_subjects()
        elif choice == '11':
            list_classes()
        elif choice == '12':
            list_schedules()
        elif choice == '13':
            list_grades()
        elif choice == '14':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
