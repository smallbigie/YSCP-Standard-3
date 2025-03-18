# Global dictionary to store student names and their grades
students_grades = {}

# Function to add a student
def add_student():
    student_name = input("Enter the student's name: ")
    if student_name in students_grades:
        print(f"{student_name} already exists in the system.")
    else:
        students_grades[student_name] = []  # Initialize an empty list for grades
        print(f"Student {student_name} added successfully!")

# Function to select a student
def select_student():
    student_name = input("Enter the student's name to select: ")
    if student_name in students_grades:
        print(f"Student {student_name} selected.")
        return student_name
    else:
        print(f"{student_name} is not in the system.")
        return None

# Function to add grades to the selected student
def add_grade(student_name):
    if student_name:
        while True:
            try:
                grade = float(input(f"Enter a grade for {student_name} (or type 'done' to stop): "))
                students_grades[student_name].append(grade)
                print(f"Grade {grade} added for {student_name}.")
                continue_adding = input("Do you want to add another grade? (yes/no): ")
                if continue_adding.lower() != 'yes':
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the grade.")
    else:
        print("No student selected to add grades.")

# Function to calculate and display the average grade of the selected student
def get_student_average(student_name):
    if student_name:
        grades = students_grades.get(student_name)
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade for {student_name}: {average:.2f}")
        else:
            print(f"No grades found for {student_name}.")
    else:
        print("No student selected to get average.")

# Function to calculate and display the class average
def get_class_average():
    if students_grades:
        total_grades = []
        for grades in students_grades.values():
            total_grades.extend(grades)
        if total_grades:
            class_average = sum(total_grades) / len(total_grades)
            print(f"Class average grade: {class_average:.2f}")
        else:
            print("No grades found in the system.")
    else:
        print("No students in the system.")

# Main function to run the menu-driven system
def main():
    while True:
        print("\n--- Student Grading System ---")
        print("1. Add a Student")
        print("2. Select a Student")
        print("3. Add a Grade")
        print("4. Get Student Average")
        print("5. Get Class Average")
        print("6. Quit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            student_name = select_student()
        elif choice == '3':
            add_grade(student_name)
        elif choice == '4':
            get_student_average(student_name)
        elif choice == '5':
            get_class_average()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
