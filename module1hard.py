grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students = sorted(students)
avg_grades = {}
for i in range(len(students)):
    average = sum(grades[i]) / len(grades[i])
    avg_grades.update({students[i] : average})
print(avg_grades)