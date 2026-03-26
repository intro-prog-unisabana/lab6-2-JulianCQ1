def initialize_dict(student_name,subject_grades):
    return {student_name: subject_grades}
def  add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    name = input("Enter student name:\n").title()
    subjects ={}
    while True:
        entry =input("Enter subject adn grade (or 'exit' to finish):\n")
        if entry.lower() == "exit":
        subject, grade = entry.split(",")
        subjects[subject.title()] = float(grade)
    student_grades[name]=subjects
    print(f"Student {name} successfully added to the grades managment system.")
    return student_grades
def get_students(student_grades, keys):
    result = {}
    for key in keys:
        found = False
        for student in student_grades:
            if student.lower() == key.lower():
                result[student]= student_grades[student]
                found = True
                break
        if not found:
            print(f"{key.title()} not found!")
    return result
def avg_by_student(student_grades, keys=None):
    if keys is None:
        data = student_grades
    else:
        data = get_students(student_grades, keys)
    for student, subject in data.items():
        avg = sum(subjects.values())/len(subjects)
        print(f"{student}: {avg:.1f}")

  
