import csv  

archivo = open("appstore_games.csv","r")
csvreader = csv.reader(archivo, delimiter=",")

gratisEspañol= filter(lambda x: x[12] == "ES" and x[7] == "0", csvreader)

for juego in gratisEspañol:
    print(juego)

