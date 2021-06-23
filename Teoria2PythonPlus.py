import pandas as pd
from matplotlib import pyplot as plt
# import PySimpleGUI as sg

data_set = pd.read_csv('usuarios.csv', encoding='utf-8',error_bad_lines=False)
cantJugados = data_set['CantJugado']
nombres = data_set['Nombre']

# sg.popup(f'Los nombres son:  {nombres}, y la cantidad de veces jugado son {cantJugados} respectivamente', auto_close= True, auto_close_duration=10)

explode = (0.1, 0)

plt.pie(cantJugados, explode=explode, labels=nombres, autopct='%1.1f%%',
shadow=True, startangle=90, labeldistance= 1.1)
plt.axis('equal')
plt.legend(nombres)
plt.title("Cantidad jugadas por jugador")
plt.show()



