"""
with open('-', 'r') as f:
    for i in range(100):
        print(f.readline())

"""

clients = {}

with open('-', 'r', encoding="utf-8") as f:
    # deplacer le curseur vers la permiere ligne du csv
    for i in range(9):
        f.readline()
    line = f.readline()
    while line != "":
        elem = line.split(',')
        solde = int(elem[-1])
        name = elem[2] + ' ' + elem[3]
        clients[name] = solde
        line = f.readline()
        #print(clients)
    
    list_client_solde = []
    for client in clients:
        list_client_solde.append((client, clients[client]))
    
    list_client_solde.sort(key=lambda x: x[1], reverse=True)
    print(list_client_solde[:3])
