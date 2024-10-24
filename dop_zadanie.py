# Средний балл

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = list(sorted(students))
print(sorted_students)

aaron_grade = grades[0]
bilbo_grade = grades[1]
johnny_grade = grades[2]
khendrik_grade = grades[3]
steve_grade = grades[4]

average_aaron = sum(aaron_grade) / len(aaron_grade)
average_bilbo = sum(bilbo_grade) / len(bilbo_grade)
average_johnny = sum(johnny_grade) / len(johnny_grade)
average_khendrik = sum(khendrik_grade) / len(khendrik_grade)
average_steve = sum(steve_grade) / len(steve_grade)

average_scores = {
    'Aaron': average_aaron,
    'Bilbo': average_bilbo,
    'Johnny': average_johnny,
    'Khendrik': average_khendrik,
    'Steve': average_steve
}

print(average_scores)