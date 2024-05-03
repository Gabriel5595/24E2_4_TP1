def request_data(database):
    name = input("Enter the studant's name: ")
    surname = input("Enter the studant's surname: ")
    full_name = name + " " + surname
    grade_1 = float(input("Enter the studant's first grade: "))
    grade_2 = float(input("Enter the studant's second grade: "))
    grade_3 = float(input("Enter the studant's third grade: "))
    average = round(float((grade_1 + grade_2 + grade_3)/3), 2)
    
    student = {
        "Nome Completo": full_name,
        "Nota 1": grade_1,
        "Nota 2": grade_2,
        "Nota 3": grade_3,
        "Média": average
    }
    
    database.append(student)
    
    return database