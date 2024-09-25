'''  Write a program that takes a list of student names as input,
sorts the names in alphabetical order, and prints the sorted list. '''

def student_names():
    students = input("Enter Students Name with spaces:").split()
    students_sort = sorted(students)
    return students_sort

print(student_names())