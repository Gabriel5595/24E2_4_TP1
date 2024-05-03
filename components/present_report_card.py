from tabulate import tabulate

def present_report_card(database):
    passing_score = 7
    
    view_data = []
    
    for data in database:
        if data["Média"] >= passing_score:
            data["Status"] = "Aprovado"
            view_data.append(data)
        elif data["Média"] < passing_score:
            data["Status"] = "Reprovado"
            view_data.append(data)
    
    print(tabulate(view_data, headers="keys", tablefmt="grid"))