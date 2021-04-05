texto = (input('Ingrese una frase a codificar: '))

text = ''
textoCodificado = text.join(list(map(lambda a: chr(ord(a) + 1), texto )))

print (textoCodificado)



