students = []

T = int(input())

for _ in range(T):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = []
for student in students:
    if student[1] not in grades:
        grades.append(student[1])

grades.sort()
SecondLowestGrade = grades[1]

names_in_second_lowest = []
for student in students:
    if student[1] == SecondLowestGrade:
        names_in_second_lowest.append(student[0])

names_in_second_lowest.sort()

for name in names_in_second_lowest:
    print(name)
