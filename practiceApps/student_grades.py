# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to determine if the student passed
def check_passed(average):
    if average >= 60:
        return "Passed"
    else:
        return "Failed"

def main():
    # Get student name
    student_name = input("Enter the student's name: ")

    # Get grades input
    grades = []
    while True:
        grade_input = input(f"Enter grade for {student_name} (or type 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            grades.append(grade)
        except ValueError:
            print("Invalid input, please enter a numeric grade.")

    if grades:  # Only proceed if at least one grade was entered
        average = calculate_average(grades)
        result = check_passed(average)
        print(f"{student_name}'s average grade: {average:.2f}")
        print(f"Result: {result}")
    else:
        print("No grades entered for the student.")

if __name__ == "__main__":
    main()
