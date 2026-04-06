<<<<<<< HEAD

=======
student_data = []
while True:
    student_name = input("Enter Student Name: ")
    student_marks = input("Enter Student Marks: \n").split()
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

for student in student_data:
    marks_join = ", ".join(map(str, student['marks']))

    avg = sum(student['marks']) / len(student['marks'])

    status = 'PASS'
    for mark in student["marks"]:
        if(mark < 35):
            status = 'FAIL'
            break

    if(avg > high_avg):
        high_avg = avg
        topper = student['name']

    print(f"Name: {student['name']}")
    print(f"Marks: {marks_join}")
    print(f"Average: {avg:.2f}%")
    print(f"Status: {status}\n")

print(f"Topper: {topper} with average {high_avg:.2f}")
>>>>>>> 88a72c7 (Added student performance analyzer project)
