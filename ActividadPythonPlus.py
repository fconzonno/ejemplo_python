import PySimpleGUI as sg
import json
import csv


layout = [
        [sg.Text('Que opcion desea realizar?',text_color='black', background_color='pink')],
        [sg.Button(button_text = 'Medicamentos', button_color=('black', 'pink'))],
        [sg.Button(button_text = 'Denuncias No Penales', button_color=('black', 'pink'))],
        [sg.Button(button_text= 'Salir', button_color=('black', 'DarkRed'))]    
        ]
    
window = sg.Window('Bienvenido a la interfaz de usuario', layout, background_color='Purple' )

while True:
     event, values = window.read()
     try: 
         if event == 'Medicamentos':
             archivo = open("./medicamentos.csv","r")
             csvreader = csv.reader(archivo, delimiter=";")
             lista = []
             sg.Popup('A continuacion se agregaran al archivo los medicamentos cuyo precio superan los 5000 pesos ')
             next(csvreader,None)
             lista = list(filter(lambda x: float(x[7]) > 5000, csvreader))
             sg.Popup(f'Se creo el archivo correctamente, el archivo contiene {len(lista)} elementos')
             with open('ArchivoMedicamentos.json', 'w') as file:
                 json.dump(lista, file, indent = 4, ensure_ascii = False)

         elif event == 'Denuncias No Penales':
             archivo = open("./denuncias_no_penales.csv","r", encoding='utf-8')
             csvreader = csv.reader(archivo, delimiter=",")
             lista = []
             sg.Popup('A continuacion se agregaran al archivo las primeras 10 denuncias No penales ocurridas en La Plata ')
             next(csvreader,None)
             ordenarLista = sorted(csvreader, reverse=True, key = lambda x: x[4] == 'La Plata')
             for i in range(0,10):
                 lista.append(ordenarLista[i])  #Hay alguna forma de hacer esto en una sola linea?
             #lista = list(filter(lambda x: x[4] == 'La Plata', csvreader)) solo para filtrar las denuncias en LP
             sg.Popup(f'Se creo el archivo correctamente, el archivo contiene {len(lista)} elementos')
             with open('ArchivoDenuncias.json', 'w', encoding='utf-8') as file:
                 json.dump(lista, file, indent = 4, ensure_ascii = False)
         elif event == None or 'Salir':
             break
     except:
         sg.Popup('Upss.. algo salio mal',
                  'Vuelva a iniciar el programa')
         break