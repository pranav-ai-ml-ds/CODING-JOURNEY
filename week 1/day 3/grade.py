students=[]
def add_student():
    name=input("ENTER STUDENT NAME")

    marks=[]
    subjects=["MATH","PHYSICS","CHEMISTRY","ENGLISH","CS"]

    for subject in subjects:
        mark=float(input(f"ENTER {subject} marks: "))
        marks.append(mark)
    total=sum(marks)
    average=total/len(marks)

    student={
        "name": name,
        "marks": marks,
        "total": total,
        "average": average
    }
    students.append(student)
    print("STUDENT ADDED")
def view_all_students():
    if len(students)==0:
        print("NO STUDENTS YET")
        return
    print("\n=== ALL STUDENTS===")
    for i,student in enumerate(students):
        print(f"\n{i+1}.{student['name']}")
        print(f"\n   TOTAL:{student['total']}")
        print(f"     AVERAGE:{student['average']:.2f}")

        if student['average'] >= 90:
            print("   Grade: A+")
        elif student['average'] >= 80:
            print("   Grade: A")
        elif student['average'] >= 70:
            print("   Grade: B")
        elif student['average'] >= 60:
            print("   Grade: C")
        else:
            print("   Grade: F")

def  find_topper():
    if len(students)==0:
        print("NO STUDENTS YET")
        return
    topper=students[0]
    for student in students:
        if student['average']>topper['average']:
            topper=student
    print(f"\n🏆 TOPPER: {topper['name']}")
    print(f"Average: {topper['average']:.2f}")

while True:
    print("\n=== GRADE MANAGER ===")
    print("1. Add student")
    print("2. View all students")
    print("3. Find topper")
    print("4. Exit")
    
    choice = input("\nChoose: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        find_topper()
    elif choice == "4":
        break
