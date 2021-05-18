import datetime
import csv
import PySimpleGUI as sg

# print(x)

nro_dia = datetime.datetime.today().weekday()
dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
dias_semana[nro_dia]
print(nro_dia)

print(dias_semana[nro_dia])
mañana, tarde =  [(0, 12), (13, 23) ]
criterios_data = {}


for dia in dias_semana:
    criterios_data[dia] = {mañana:{}, tarde: {}}
# print(x.hour)

mañana, tarde =  [(0, 12), (13, 23) ]
criterios_data = {}

for dia in dias_semana:
    criterios_data[dia] = {mañana:{}, tarde: {}}


# {'lunes': {(0, 12): {}, (13, 23): {}},
# 'martes': {(0, 12): {}, (13, 23): {}},
# 'miercoles': {(0, 12): {}, (13, 23): {}},
# 'jueves': {(0, 12): {}, (13, 23): {}},
# 'viernes': {(0, 12): {}, (13, 23): {}},
# 'sabado': {(0, 12): {}, (13, 23): {}},
# 'domingo': {(0, 12): {}, (13, 23): {}}}




horario_juego = datetime.datetime.now().strftime("%m/%d/%Y,%H:%M:%S")


def get_conex_prov(anioMin, anioMax, rango):

    archivo = open("./metal_bands_2017.csv","r")
    csvreader = csv.reader(archivo, delimiter=",")
    next(csvreader,None)
    lista = list(filter(lambda x: x[3] > anioMin and x[3] < anioMax , csvreader))
    for elem in lista:
        for elemen in lista:
            if elemen[1] == elem[1]:
                lista.remove(elemen)
    lista10 = [] 
    for i in range(0,rango):
        lista10.append(lista[i][1])
    return lista10
    # return lista10[1]
def get_conex_prov2(minimo, maximo, rango):
    archivo = open("./medicamentos.csv","r")
    csvreader = csv.reader(archivo, delimiter=";")
    lista = []
    next(csvreader,None)
    data_precio = sorted(list(filter(lambda x: float(x[7]) > minimo and float(x[7]) < maximo, csvreader)), reverse = True, key = lambda x: x[7])
    for i in range(0,rango):
        lista.append(data_precio[i][2])
    return lista

rango = 10
criterios_data['lunes'][mañana] = {'criterio': 'Bandas de metal de un año en particular',
                                    'funcion': get_conex_prov, 
                                    'params': ('1960' , '1975', rango)
                                   }

criterios_data['lunes'][tarde] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires ',
                                    'funcion': get_conex_prov, 
                                    'params': ('1976', '1983', rango)
                                   }

criterios_data['martes'][mañana] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires',
                                    'funcion': get_conex_prov, 
                                    'params': ('1984', '1989', rango)
                                   }
                
criterios_data['martes'][tarde] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires',
                                    'funcion': get_conex_prov, 
                                    'params': ('1990', '1994', rango)
                                   }

criterios_data['miercoles'][mañana] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires',
                                    'funcion': get_conex_prov, 
                                    'params': ('1995', '2000', rango)
                                   }              

criterios_data['miercoles'][tarde] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires',
                                    'funcion': get_conex_prov, 
                                    'params': ('2000','2005', rango)
                                   } 

criterios_data['jueves'][mañana] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires',
                                    'funcion': get_conex_prov, 
                                    'params': ('2006','2012', rango)
                                   }     
        
criterios_data['jueves'][tarde] = {'criterio': 'Denuncias no penales en localidades de Buenos Aires',
                                    'funcion': get_conex_prov, 
                                    'params': ('2012', '2017', rango)
                                   }  

criterios_data['viernes'][mañana] = {'criterio': 'Medicamentos con precio entre 1 y 200',
                                    'funcion': get_conex_prov2, 
                                    'params': (1, 200, rango)
                                   }  


criterios_data['viernes'][tarde] = {'criterio': 'Medicamentos con precio entre 2001 y 700',
                                    'funcion': get_conex_prov2, 
                                    'params': (201, 700, rango)
                                   }  
                                
criterios_data['sabado'][mañana] = {'criterio': 'Medicamentos con precio entre 701 y 1500',
                                    'funcion': get_conex_prov2, 
                                    'params': (701, 1500, rango)
                                   }  

                                
criterios_data['sabado'][tarde] = {'criterio': 'Medicamentos con precio entre 1501 y 3000',
                                    'funcion': get_conex_prov2, 
                                    'params': (1501, 3000, rango)
                                   }  

criterios_data['domingo'][mañana] = {'criterio': 'Medicamentos con precio entre 3001 y 4000',
                                    'funcion': get_conex_prov2, 
                                    'params': (3001, 4000, rango)
                                   }  
                

criterios_data['domingo'][tarde] = {'criterio': 'Medicamentos con precio entre 4001 y 5000',
                                    'funcion': get_conex_prov2, 
                                    'params': (4001, 5000, rango)
                                   }  

hora = datetime.datetime.now().hour
dia_semana =  dias_semana[datetime.datetime.today().weekday()]

rango = mañana if hora in mañana else tarde
fun_parm = criterios_data[dia_semana][rango]


print(fun_parm['funcion'](*fun_parm['params']))

