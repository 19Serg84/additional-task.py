grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(type(grades))
#print(type(students))
#students_sorted = (sorted(students))
#print(sum(grades[0])/len(grades[0]))
#print(students_sorted)
average_grades_Aaron = (sum(grades[0])/len(grades[0]))
average_grades_Bilbo = (sum(grades[1])/len(grades[1]))
average_grades_Johnny = (sum(grades[2])/len(grades[2]))
average_grades_Khendrik = (sum(grades[3])/len(grades[3]))
average_grades_Steve = (sum(grades[4])/len(grades[4]))
average_grades = { }
average_grades.update ({'Aaron':average_grades_Aaron,
                        'Bilbo':average_grades_Bilbo,'Johnny':average_grades_Johnny,
                        'Khendrik':average_grades_Khendrik,'Steve':average_grades_Steve})
print(average_grades)

