from tabulate import tabulate

def search_student(database):
    while True:
            print("Would you like to search by Student ID or Full Name?")
            option = int(input("1) student ID.\n2) Full Name.\n"))
            
            if option == 1:
                student_id = int(input("\nPlease, enter the student's ID: "))
                student_id -= 1
                
                if database[student_id] == None:
                    print("student not found.\n")
                    return None
                else:
                    print(tabulate([database[student_id]], headers="keys", tablefmt="grid"))
                    return database[student_id]
            
            elif option == 2:
                student_name = input("Please, enter the student's full name: ")
                
                for data in database:
                    if data["Nome Completo"] == student_name:
                        print(tabulate([data], headers="keys", tablefmt="grid"))
                        return data
                
                print("student not found.\n")
                return None
            
            else:
                print("The entered option is not valid.\n")