import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.request_data import request_data
from components.edit_grade import edit_grade
from components.list_students import list_students
from components.present_report_card import present_report_card

def menu(database):
    while True:
        try:
            print("\n***GRADES MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Register student.\n2) Edit student grades.\n3) List students.\n4) Generate report card.\n5) Exit\n"))

            if option == 1:
                database = request_data(database)

            elif option == 2:
                database = edit_grade(database)

            elif option == 3:
                while True:
                    try:
                        print("Please, select one of the options below")
                        approved = int(input("1) Students that have been approved\n2) Students that failed.\n"))
                        
                        if approved == 1:
                            list_students(database)
                            break
                        elif approved == 2:
                            list_students(database, False)
                            break
                        else:
                            print("The entered option is not valid.\n")
                    except ValueError:
                        print("Please enter one of the valid options.")
            
            elif option == 4:
                present_report_card(database)
            
            elif option == 5:
                print("Exiting...")
                break
            
            else:
                print("The entered option is not valid.\n")

        except ValueError:
            print("Please enter one of the valid options.")

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
    
    menu(database)

main()