from tabulate import tabulate
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    database = edit_grade(database)
    print(tabulate(database, headers="keys", tablefmt="grid"))

main()