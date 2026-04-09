import csv

def get_grade_info(avg):
    """This function takes an average and returns the grade and feedback."""
    if avg >= 90:
        return 'A', 'Excellent'
    elif avg >= 75:
        return 'B', 'Good'
    elif avg >= 60:
        return 'C', 'Average'
    elif avg >= 50:
        return 'D', 'Needs Improvement'
    else:
        return 'Fail', 'Work Hard'

student_data = []

while True:
    student_name = input("Enter Student Name: ")

    try:
        student_marks = input("Enter Student Marks: ").split()
        marks_split = list(map(int, student_marks))
    except ValueError:
        print("Please enter numbers only! Try entering once again")
        continue

    student_data.append({"name": student_name, "marks":marks_split})

    question = input("Do you want to add another student? (yes/no): ").lower()
    if question in ['no','n']:
        break
'''student_data = [{"name":"Alexa","marks":[90,50,80,79,86,89]},
                {"name":"Siri","marks":[80,50,20,69,56,99]},
                {"name":"Jake","marks":[30,60,82,70,77,90]}]'''

topper = None
high_avg = float('-inf')
student_count = 0
class_avg = 0
pass_count = 0
fail_count = 0

for student in student_data:

    marks_join = ", ".join(map(str, student['marks']))

    avg = sum(student['marks']) / len(student['marks'])
    grade, feedback = get_grade_info(avg)
    class_avg += avg

    status = 'PASS'
    for mark in student['marks']:
        if mark < 35:
            status = 'FAIL'
            break

    if status == 'FAIL':
        fail_count += 1
    else:
        pass_count += 1
    if(avg > high_avg):
        high_avg = avg
        topper = student['name']

    student['average'] = round(avg, 2) # Rounding it so it looks clean
    student['grade'] = grade
    student['status'] = status
    student['feedback'] = feedback

    print("-"*20)
    print(f"Name: {student['name']}")
    print(f"Marks: {marks_join}")
    print(f"Average: {avg:.2f}%")
    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")
    print(f"Status: {status}")
    print("-"*20)

print(f"\nTopper: {topper} with average {high_avg:.2f}\n")
total_students = len(student_data)

# Create a new CSV file for the detailed student records
if total_students > 0:
    # "newline=''" prevents blank rows between data in Excel
    with open("student_database.csv", 'w', newline='') as csvfile:

        # 1. Define your column headers (these must match your dictionary keys!)
        column_headers = ['name', 'marks', 'average', 'grade', 'status', 'feedback']

        # 2. Set up the writer
        writer = csv.DictWriter(csvfile, fieldnames=column_headers)

        # 3. Write the top row (the headers)
        writer.writeheader()

        # 4. Loop through your data and write each student as a new row
        for student in student_data:
            writer.writerow(student)

    print("Success! Individual student records saved to 'student_database.csv'.")

    with open("class_summary.txt",'w') as file:
        file.write("Class Analysis\n")
        file.write(f"Total Students: {total_students}\n")
        file.write(f"Class Average: {class_avg/total_students:.2f}%\n")
        file.write(f"Passed: {pass_count}\n")
        file.write(f"Failed: {fail_count}\n")
    print("Success! The class analysis has been saved to 'class_summary.txt'.")
else:
    print("No students were entered. No file was created.")

print("Success! The class analysis has been saved to 'class_summary.txt'.")