student_data = []
while True:
    student_name = input("Enter Student Name: ")
    student_marks = input("Enter Student Marks: ").split()
    marks_split = list(map(int, student_marks))
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
    student_count += 1

    marks_join = ", ".join(map(str, student['marks']))

    avg = sum(student['marks']) / len(student['marks'])

    class_avg += avg

    if(avg >= 90):
        grade = 'A'
        feedback = 'Excellent'
    elif(avg >= 75):
        grade = 'B'
        feedback = 'Good'
    elif(avg >= 60):
        grade = 'C'
        feedback = 'Average'
    elif(avg >= 50):
        grade = 'D'
        feedback = 'Needs Improvement'
    else:
        grade = 'Fail'
        feedback = "Work Hard"

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


    print("-"*20)
    print(f"Name: {student['name']}")
    print(f"Marks: {marks_join}")
    print(f"Average: {avg:.2f}%")
    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")
    print(f"Status: {status}")
    print("-"*20)

print(f"\nTopper: {topper} with average {high_avg:.2f}\n")

print("="*10,"Class Analysis","="*10)
print(f"Total Students: {student_count}")
print(f"Class Average: {class_avg/student_count:.2f}%")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print("="*20)
