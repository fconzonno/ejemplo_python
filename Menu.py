import PySimpleGUI as sg
import json
import csv
from datetime import datetime
from PySimpleGUI.PySimpleGUI import popup_auto_close, popup_cancel, popup_ok

def anadirUsuario(usuario):
    '''Añade un usuario al archivo de usuarios''' 
    try:
        with open('usuarios.json', 'x',encoding = 'utf8') as file:
            listaUsuarios = []
            listaUsuarios.append(usuario)
            json.dump(listaUsuarios, file, indent = 4, ensure_ascii = 4)
            sg.popup('FELICITACIONES, es el primer usuario en utilizar nuestro juego',
                'El usuario se cargó correctamente ', auto_close_duration= 2, auto_close=True)
    except:
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:
            listaUsuarios = json.load(file)
            listaUsuarios.append(usuario)
        with open ('usuarios.json', 'w+', encoding = 'utf8') as file: 
            json.dump(listaUsuarios, file, indent = 4, ensure_ascii = 4)
            sg.popup('El usuario se cargó correctamente ',  auto_close_duration= 2, auto_close=True)

def ingresaGenero(genero):
    ''' Permite al usuario especificar su género'''
    respuesta = sg.popup_yes_no('Desea especificar su género?')
    if respuesta == 'Yes':
        texto = sg.popup_get_text('Ingrese su género', 'Ventana de epecificacion de género', size = (25,25))
        if texto == None or texto == 'None' or texto == '' or texto == 'Ingrese su género':
            genero = 'Otro'
            sg,popup_ok('Su género quedó guardado como "Otro" ',auto_close_duration= 3, auto_close=True)
        else:
            genero = texto
            sg.popup('Su género quedó guardado como: ', genero, auto_close_duration= 3, auto_close=True)
    elif respuesta == 'No':
        sg,popup_ok('Ok, su genero quedó guardado como "Otro" ', auto_close_duration= 3, auto_close=True)
        genero = 'Otro'
    return genero



def nombreUsado(texto):
    '''Devuelve True si el nombre del usuario está ocupado o False si se puede utilizar'''
    try: 
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:
            listaUsuarios = json.load(file)
            usuario = list(filter(lambda a: a['Nombre'] == texto, listaUsuarios))
            if (len(usuario) >= 1):
                    return True
            else:
                return False
    except FileNotFoundError:
        return False


def registrar():


    '''el usuario nuevo ingresa sus datos'''

    generos = ['Masculino', 'Femenino','Trans','No binarie', 'Otro']
    dificultad = ['Nivel 1', 'Nivel 2', 'Nivel 3']

    layout = [[sg.Input('Ingresa tu nombre', key = 'Nombre', size = (20,15))], 
            [sg.Input ('Ingresa tu edad', key = 'Edad', size = (15,30))],
            [sg.Text('Seleccione su género')],
            # [sg.Listbox(generos, size=(20,4), enable_events=True, key='_LIST_')]
            [sg.Listbox(generos, size=(15, 3), key='Genero')],
            [sg.Text('Elija la dificultad')],
            [sg.InputCombo(dificultad, auto_size_text= True,key = 'Dificultad')],
            [sg.Text('Desea carteles al jugar? ')],
            [sg.Radio('Si',1, key = 'cartelesSi', default = True),sg.Radio('No',1, key = 'cartelesNo', default = False)],
            [sg.Text('Jugar con imágenes o palabras? ')],
            [sg.Radio('Imagenes',2,  key = 'imagenesSi', default = True),sg.Radio('Palabras',2, key = 'Palabras', default = False)],
            [sg.OK(), sg.Button('Salir', key = 'Salir')]
            ]

    window = sg.Window("Bienvenido a la interfaz de Registro de Usuario ", layout, margins=(30 , 30))
    event, values = window.read()
    while True:
        try:
            
            if event == None or 'Salir':
                break      
            int(values['Edad'])    
            if values['Nombre'] == 'Ingresa tu nombre' or values['Nombre'] == '':
                sg.Popup('No se ingresó ningún nombre, volvé a ingresar los datos')
            elif (nombreUsado(values['Nombre']) == True):
                sg.Popup('El nombre no está disponible, probá otro')
            elif values['Genero'][0] == '':                                         
                sg.Popup('No seleccionó el género, volvé a ingresar los datos') 
            elif values['Edad'] == 'Ingresa tu edad':
                sg.Popup('No se ingresó la edad, volvé a ingresar los datos')
            elif values['Dificultad'] == '':
                sg.Popup('No elijió la dificultad, volvé a ingresar los datos')
            elif values['Dificultad'] not in dificultad:
                sg.popup('No ingresó una dificultad válida',
                        'Debe elegir entre "Nivel 1", "Nivel 2" y "Nivel 3" ')
            else:    
                if values['Genero'][0] == 'Otro':
                    values['Genero'][0] = ingresaGenero(values['Genero'][0])
                elif values['cartelesSi']:
                    sg.popup('El usuario quiere carteles ', auto_close_duration= 2, auto_close=True)
                elif values['cartelesNo']: 
                    sg.popup('El usuario no quiere carteles', auto_close_duration= 2, auto_close=True)
                elif values['Imagenes']:
                    sg.popup('El usuario quiere imagenes ', auto_close_duration= 2, auto_close=True)
                elif values['Palabras']:
                    sg.popup('El usuario quiere palabras ', auto_close_duration= 2, auto_close=True)
               
                window.close()
                dia = datetime.today()
                fecha = dia.strftime("%d/%m/%Y")
                tiempo = datetime.now()
                hora = tiempo.strftime("%H:%M:%S")
                sg.Popup('Los datos ingresados del usuario son: ',
                            'El nombre es: ', values['Nombre'],
                            'La edad: ', values['Edad'],
                            'El género :', (values['Genero']),
                            'La dificultad elegida fue:',  (values['Dificultad']),
                            'Se registró el día', fecha, 'A la hora: ', hora,
                            'Desea carteles ', values['cartelesSi'],
                            'Desea imágenes ', values['imagenesSi']
                            )  
                usuario = {'Nombre': values['Nombre'], 'Edad':values['Edad'], 'Genero' : values['Genero'], 'Dificultad': values['Dificultad'], 'Fecha': fecha,'Hora': hora, 'Puntaje': 0, 'Carteles': values['cartelesSi'], 'Imagenes': values['imagenesSi']}
                sg.popup('A continuación, se agregará el usuario al archivo', auto_close_duration= 2, auto_close=True)
                anadirUsuario(usuario)
                sg.Popup('FELICIDADES, ya puede iniciar sesión en nuestro juego. Será dirigido al menú de inicio', auto_close_duration= 4, auto_close=True)
                break
        except ValueError:
            sg.Popup('No se ingresó un número entero en la edad, volvé a ingresar los datos')
        except KeyError:
            sg.Popup ('No se ingresó el género, volvé a ingresar los datos')
        except IndexError:
            sg.Popup('No se ingresó el género, volvé a ingresar los datos')
        except Exception as ex:
            sg.popup('Upss. algo salio mal, volverá a la pantalla de inicio')
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            sg.popup(message) 
        finally:
            event, values = window.read()
######################################################################### Empieza archivo de inicio de sesion
def mostrarInformacion(usuario):
    '''Función que muestra la información del usuario'''
    return ('La informacion del usuario es: ',
            'El nombre es: ', 
            usuario['Nombre'],
            'La edad : ',
             usuario['Edad'],
            'El género ingresado fue: ',
             (usuario['Genero']),
            'La dificultad elegida fue:',  
            (usuario['Dificultad']),
            'Se registró el día ', usuario["Fecha"], 'A la hora: ', usuario["Hora"],
            'Desea carteles: ', usuario['Carteles'],
            'Desea imágenes ', usuario['Imagenes'] )

def guardarUsuario(usuario):
    '''Guarda el usuario con los datos cambiados'''
    try: 
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:
            listaUsuarios = json.load(file)
            usuarioEliminar = list(filter(lambda a: a['Nombre'] == usuario['Nombre'], listaUsuarios))
            userEliminar = usuarioEliminar[0]
            listaUsuarios.remove(userEliminar)
            listaUsuarios.append(usuario)
            # listaUsuarios.append(usuario)
        with open('usuarios.json', 'w+',encoding = 'utf8') as file:
            json.dump(listaUsuarios, file, indent = 4, ensure_ascii = 4)
    except Exception as ex:
        sg.popup('Upss. algo salio mal, volverá a la pantalla de inicio')
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        sg.popup(message) 
        

def cambiarConfiguracion(usuario):
    '''Pestaña que permite al usuario cambiar su configuracion'''
    dificultad = ['Nivel 1', 'Nivel 2', 'Nivel 3']
    layout = [
            [sg.Text('Elija la dificultad')],
            [sg.InputCombo(dificultad, auto_size_text= True,key = 'Dificultad')],
            [sg.Text('Desea carteles al jugar? ')],
            [sg.Radio('Si',1, key = 'cartelesSi', default = True),sg.Radio('No',1, key = 'cartelesNo', default = False)],
            [sg.Text('Jugar con imágenes o palabras? ')],
            [sg.Radio('Imagenes',2,  key = 'imagenesSi', default = True),sg.Radio('Palabras',2, key = 'Palabras', default = False)],
            [sg.OK()]
            ]
    window = sg.Window("Bienvenido a la interfaz de Registro de Usuario ", layout, margins=(30 , 30))
    event, values = window.read()

    while True:
        try: 
            if event == None:
                    break      
            elif values['Dificultad'] == '':
                sg.Popup('No elijió la dificultad, volvé a ingresar los datos')
            elif values['Dificultad'] not in dificultad:
                sg.popup('No ingresó una dificultad válida',
                        'Debe elegir entre "Nivel 1", "Nivel 2" y "Nivel 3" ')
            else:
                usuario['Dificultad'] = values['Dificultad']
                usuario['Carteles'] = values['cartelesSi']
                usuario['Imagenes'] = values['imagenesSi']
                mostrarInformacion(usuario)
                sg.popup('Se guardará nuevamente el usuario con la configuración actual', auto_close_duration= 2, auto_close=True)
                guardarUsuario(usuario)
                sg.popup('El usuario se cargó correctamente ',  auto_close_duration= 2, auto_close=True)
                window.close()
                break
        except Exception as ex:
            sg.popup('Upss. algo salio mal, volverá a la pantalla de inicio')
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            sg.popup(message) 



        

def interfazUsuario(usuario):
    '''Interfaz de usuario'''

    layout = [ [sg.Text('CLICK EN LA SONRISA PARA JUGAR')],
               [sg.Button('JUGAR', key  = 'Jugar', size = (20,5), image_filename = 'descarga.png')],
               [sg.Button('Ver Puntaje', key = 'Puntaje')],
               [sg.Button('Ver información del Usuario', key = 'MostrarInformacion')],
               [sg.Button('Cambiar Configuracion', key = 'CambiarConfiguracion')],
               [sg.Button('Descargar usuarios en formato CSV', key = 'descargarCSV')],
               [sg.Button('Ver usuarios registrados', key = 'usuariosRegistrados')]
            ]
    window = sg.Window("Bienvenido a la interfaz de Usuario ", layout)
    event, values = window.read()

    while True:
        try:
            if event == None or 'Salir':
                break
            elif event == 'Jugar':
                sg.popup('Pantalla que redirecciona al juego')
            elif event == 'Puntaje':
                sg.popup('El puntaje del usuario', usuario['Nombre'],' es: ', usuario['Puntaje'] )
            elif event =='MostrarInformacion':
                sg.popup(mostrarInformacion (usuario))
            elif event == 'CambiarConfiguracion':
                cambiarConfiguracion(usuario)
            elif event == 'usuariosRegistrados':
                sg.popup('Los usuarios ingresados son:',
                     '',
                     usuariosRegistrados())
            elif event == 'descargarCSV':
             descargarUsuarios()
        except:
            sg.popup('Upss... ha habido un error, vuelva a iniciar sesion', auto_close_duration= 3, auto_close=True)
            break
        finally:
            event, values = window.read()


def nombreEnArchivo(texto):
    '''Esta funcion se fija si el nombre está en el archivo, es decir, si el usuario esta registrado'''
    try:
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:
            listaUsuarios = json.load(file)
        user = list(filter(lambda a: a['Nombre'] == texto, listaUsuarios))   #Como puedo hacer para no guadar una lista en user y solo guardar el elemento?
        usuario = user[0]
        interfazUsuario(usuario)
    except FileNotFoundError:
        sg.popup('No se encontró el archivo, por lo tanto, es el primer usuario en ingresar y No está registrado, lo rediccionaremos a la pantalla de registro',auto_close_duration= 5, auto_close=True)
        registrar()
    except IndexError:
        sg.popup('No se encontró el nombre en el archivo, por lo tanto, usted no está registrado, lo rediccionaremos a la pantalla de registro',auto_close_duration= 5, auto_close=True)
        registrar()



def iniciarSesion():
    '''Permite al usuario ingresar el nombre para poder iniciar sesion'''
    while True:
        texto = sg.popup_get_text('Ingrese su nombre', 'Ventana de inicio de sesión', size = (25,25))
        if texto == None or texto == 'None' or texto == '' or texto == 'Ingrese su nombre':
            sg.popup('No se ingresó el nombre, volverá a la pantalla de inicio',auto_close_duration= 3, auto_close=True)
            break
        else:
            nombreEnArchivo(texto)
            break


def descargarUsuarios():
    '''Esta función lee el archivo de usuarios.json y guarda los datos en un archivo .csv'''
    try:
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:
            listaUsuarios = json.load(file)
            with open('usuarios.csv','w') as csv_file:
                write = csv.writer(csv_file)
                write.writerow(listaUsuarios[0].keys())       #guarda primero el encabezado
                for x in listaUsuarios:
                    write.writerow(x.values())
            sg.popup('El archivo con los usuarios se creó correctamente y se llama: "usuarios.csv" ', auto_close_duration= 3, auto_close=True )
    except FileNotFoundError:
        sg.popup('No se encontró el archivo, por lo tanto, es el primer usuario en ingresar y No está registrado, lo rediccionaremos a la pantalla de registro')
        registrar()
        return
########################################################## Termina archivo inicio de sesion

def usuariosRegistrados():
    '''Devuelve una lista con todos los usuarios registrados'''
    try: 
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:
            listaUsuarios = json.load(file)
        listaPopUp = []
        for usuarios in listaUsuarios:
            listaPopUp.append(f'El usuario con nombre {usuarios["Nombre"]} tiene {usuarios["Edad"]} años ')       
        return listaPopUp
    except FileNotFoundError:
        return('No hay ningún usuario registrado')

# def crearVentana(): 
#     layout = [ [sg.Text('Que operación desea realizar?')],
#             [sg.Button('Iniciar Sesión', key = 'iniciarSesion',size = (10,5)),sg.Button('Registrarse', key = 'registro', size =(10,5))],
#             [sg.Button('Descargar Usuarios Registrados en formato CSV', key = 'descargarCSV', size = (10,5)),sg.Button('Ver Usuarios Registrados', key = 'usuariosRegistrados', size = (10,5))],
#             [sg.Text('Eligí el color de la ventana:')], 
#             [sg.Combo(values=themes, default_value=selected_theme, size=(15, 1), enable_events=True, key='select_theme')],
#             [sg.Button('Salir', key = 'Salir')] 
#         ]
#     window = sg.Window("Bienvenido a la interfaz de Usuario ", layout)
#     event, values = window.read()
#     return  event, values
def cambiarColor(values):
    selected_theme = 'BrightColors'
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.ChangeLookAndFeel(selected_theme)
    sg.theme(selected_theme)  
    selected_theme = values['select_theme']
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.theme(selected_theme)
    try:
        window_bkg = current_them.get('BACKGROUND')
        window.TKroot.config(background=window_bkg)
        # window.TKroot.config(highlightbackground=window_bkg )
        # window.TKroot.config(highlightcolor=window_bkg )

    except Exception as e:
            sg.popup('Upss.. al parecer, Python no reconoce el color, probá con otro',
            'El error fue el siguiente:',
            e)
    sg.theme(selected_theme)
    for values, element in window.AllKeysDict.items():       #MODIFICA TODOS LOS BOTONES           
        try:
            color = current_them.get(element.Type.upper())
            if color:
                if element.Type == 'button':
                    element.Widget.config(foreground=color[0], background=color[1])
                else:
                    element.Widget.config(background=color)
                element.update()
        except Exception as e:
            sg.popup('Upss.. al parecer, Python no reconoce el color, probá con otro',
            'El error fue el siguiente:',
            e)     

sg.theme('BrightColors')
#COLORES INICIO

themes = sg.ListOfLookAndFeelValues()
selected_theme = 'BrightColors'
current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
sg.ChangeLookAndFeel(selected_theme)
#COLORES FIN

layout = [ [sg.Text('Que operación desea realizar?')],
            [sg.Button('Iniciar Sesión', key = 'iniciarSesion',size = (10,5)),sg.Button('Registrarse', key = 'registro', size =(10,5))],
            [sg.Text('Eligí el color de la ventana:')], 
            [sg.Combo(values=themes, default_value=selected_theme, size=(15, 1), enable_events=True, key='select_theme')],
            [sg.Button('Salir', key = 'Salir')] 
]

window = sg.Window("Bienvenido a la interfaz de Usuario ", layout)
event, values = window.read()

while True:
    try: 
        if event == None or 'Salir':
            break
        elif event == 'select_theme':      
            cambiarColor(values)          
        elif event == 'iniciarSesion':
            iniciarSesion()
        elif event == 'registro':
            registrar()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        sg.popup(message) 
        break
    finally: 
        event, values = window.read()