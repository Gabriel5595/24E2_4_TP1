from tabulate import tabulate

def list_students(database, approved=True):
    passing_score = 7
    
    if approved:
        view_data = []
        for data in database:
            if data["Média"] >= passing_score:
                data["Status"] = "Aprovado"
                view_data.append(data)
        
        print(tabulate(view_data, headers="keys", tablefmt="grid"))
    
    else:
        view_data = []
        for data in database:
            if data["Média"] < passing_score:
                data["Status"] = "Reprovado"
                view_data.append(data)
        
        print(tabulate(view_data, headers="keys", tablefmt="grid"))