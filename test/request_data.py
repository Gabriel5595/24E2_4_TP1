def request_data(database):
    name = input("Enter the student's name: ")
    surname = input("Enter the student's surname: ")
    full_name = name + surname
    grade_1 = float(input("Enter the student's first grade: "))
    grade_2 = float(input("Enter the student's second grade: "))
    grade_3 = float(input("Enter the student's third grade: "))
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

def main():
    database = [
    {"Nome Completo": "João da Silva", "Nota 1": 7.25, "Nota 2": 8.50, "Nota 3": 9.75, "Média": 8.50},
    {"Nome Completo": "Maria Oliveira", "Nota 1": 6.00, "Nota 2": 5.25, "Nota 3": 7.75, "Média": 6.33},
    {"Nome Completo": "Pedro Santos", "Nota 1": 9.00, "Nota 2": 8.25, "Nota 3": 10.00, "Média": 9.08},
    {"Nome Completo": "Ana Pereira", "Nota 1": 8.50, "Nota 2": 7.75, "Nota 3": 6.25, "Média": 7.50},
    {"Nome Completo": "Carlos Costa", "Nota 1": 5.75, "Nota 2": 6.25, "Nota 3": 7.50, "Média": 6.50},
    {"Nome Completo": "Mariana Rodrigues", "Nota 1": 9.25, "Nota 2": 9.50, "Nota 3": 8.75, "Média": 9.17},
    {"Nome Completo": "José Martins", "Nota 1": 7.25, "Nota 2": 8.00, "Nota 3": 7.00, "Média": 7.42},
    {"Nome Completo": "Sandra Ferreira", "Nota 1": 6.00, "Nota 2": 5.25, "Nota 3": 6.00, "Média": 5.75},
    {"Nome Completo": "Rui Sousa", "Nota 1": 8.25, "Nota 2": 7.75, "Nota 3": 9.00, "Média": 8.00},
    {"Nome Completo": "Carla Almeida", "Nota 1": 7.00, "Nota 2": 6.25, "Nota 3": 5.00, "Média": 6.08},
    {"Nome Completo": "Manuel Lima", "Nota 1": 9.50, "Nota 2": 8.25, "Nota 3": 9.25, "Média": 8.83},
    {"Nome Completo": "Patrícia Carvalho", "Nota 1": 6.25, "Nota 2": 7.00, "Nota 3": 8.00, "Média": 7.08},
    {"Nome Completo": "Jorge Pereira", "Nota 1": 7.00, "Nota 2": 6.25, "Nota 3": 5.00, "Média": 6.08},
    {"Nome Completo": "Catarina Silva", "Nota 1": 8.25, "Nota 2": 9.25, "Nota 3": 8.50, "Média": 8.67},
    {"Nome Completo": "Paulo Santos", "Nota 1": 5.75, "Nota 2": 6.25, "Nota 3": 7.50, "Média": 6.50},
    {"Nome Completo": "Andreia Costa", "Nota 1": 9.25, "Nota 2": 8.00, "Nota 3": 7.00, "Média": 8.08},
    {"Nome Completo": "Miguel Oliveira", "Nota 1": 7.25, "Nota 2": 8.00, "Nota 3": 9.25, "Média": 8.17},
    {"Nome Completo": "Filipa Rodrigues", "Nota 1": 6.25, "Nota 2": 7.00, "Nota 3": 8.00, "Média": 7.08},
    {"Nome Completo": "Ricardo Martins", "Nota 1": 8.00, "Nota 2": 9.00, "Nota 3": 8.50, "Média": 8.50},
    {"Nome Completo": "Inês Ferreira", "Nota 1": 5.75, "Nota 2": 6.25, "Nota 3": 7.50, "Média": 6.50}
]
    
    print(request_data(database))

main()