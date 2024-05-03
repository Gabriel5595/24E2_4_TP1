from tabulate import tabulate

from components.search_student import search_student

def edit_grade(database):
    student_index = search_student(database)
    
    if student_index != None:
        new_grade_1 = round(float(input("Please enter the student's new first grade: ")), 2)
        new_grade_2 = round(float(input("Please enter the student's new second grade: ")), 2)
        new_grade_3 = round(float(input("Please enter the student's new third grade: ")), 2)
        new_average = round(float((new_grade_1 + new_grade_2 + new_grade_3) / 3))
        
        database[student_index]["Nota 1"] = new_grade_1
        database[student_index]["Nota 2"] = new_grade_2
        database[student_index]["Nota 3"] = new_grade_3
        database[student_index]["Média"] = new_average
        
        print("student's new info:")
        print(tabulate([database[int(student_index)]], headers="keys", tablefmt="grid"))
        
        return database