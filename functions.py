students = []
student_list = []

def get_students_title():
    students_title = []
    for student in students:
        students_title.append(student["name"].title())
        return students_title


def print_student_title():
    students_title = []
    students_title = get_students_title()
    print(students_title)


def add_student(name, student_id=200):
    student = {"name":name, "id":student_id}
    students.append(student)


def readFile():
    try:
        f = open("students.txt", "r")
        for sname in f.readlines():
            add_student(sname)
        f.close()
    except Exception:
        print("The file is inaccessible")


def writeFile(student_name):
    try:
        f = open("students.txt", "a")
        f.write(student_name + "\n")
        f.close()
    except Exception:
        print("Unable to write to file")


def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **barfs):
    print(name)
    print(barfs["description"], barfs["feedback"])

readFile()
print_student_title()

student_name = input("Enter student name : ")
student_id = input("Enter student id : ")

add_student(student_name, student_id)
writeFile(student_name)


