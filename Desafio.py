texto = (input('Ingrese una frase a codificar: '))

text = ''
textoCodificado = text.join(list(map(lambda a: chr(ord(a) + 1), texto )))

print (textoCodificado)

#Lo que se realizó fue una lista de caracteres incrementados en uno del string ingresado. Luego, cada elemento de la lista se concatena en un string. 
#Quería saber si hay una manera mas facil de realizarlo, sin necesidad de trabajar con una lista.

