# This code is a simple university analytics dashboard taht allows users to add student grades, calculate performance statistics, and show students who failed a course.
def add_students(new_lst):
    new_dict = {}
    student_name = input("Enter the name of the student: ")
    course = input("Enter the name of the course: ")
    grade = float(input("Enter the grade: "))
    if grade < 0 or grade > 20 :
        print("Invalid grade, please enter a grade between 0 and 20.")
    else:
        new_dict = {
            "student_name": student_name,
            "course": course,
            "grade": grade
        }
        new_lst.append(new_dict)
    return new_lst
def calculate_statistics(new_lst):
    if len(new_lst) == 0 :
        print("No student in list")
        return
    total = 0
    top_student = ""
    max_grade = -1
    for student in new_lst:
       total += student["grade"]
       if student["grade"] > max_grade:
            max_grade = student["grade"]
            top_student = student["student_name"]
    average = total / len(new_lst)
    print(f"top student: {top_student} with grade: {max_grade}")
    print(f"average grade: {average}")
    return average , top_student
def show_conditional_students(new_lst):
    condition = False
    if len(new_lst) ==0 :
        print("No student in list")
        return
    for student in new_lst:
        if student["grade"] < 12 :
                condition = True
                print(f"Student: {student["student_name"]}, course: {student["course"]}, grade: {student["grade"]}")
        if condition  == False:
                print("No student has a grade below 12.")
def main_menu():
    main_lst = []
    while True:
        print("\n ===== University Analytics Dashboard =====")
        print("1. Add student grade")
        print("2. Show performance statistics")
        print("3. Show conditional students")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_students(main_lst)
        elif choice == "2":
            calculate_statistics(main_lst)
        elif choice == "3":
            show_conditional_students(main_lst)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("invalid choice, please try again")
main_menu()




