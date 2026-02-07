students = [
    {"name": "Alice", "age": 20, "cgpa": 8.5},
    {"name": "Bob", "age": 21, "cgpa": 7.8},
    {"name": "Charlie", "age": 19, "cgpa": 9.2}
]

print(students[0]["name"])
print(students[1]["age"])
print(students[2]["age"])

for student in students:
    print(student["name"],"has CGPA",student["cgpa"])



