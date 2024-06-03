#Escribir un programa que verifique si una cadena es un palindromo o no

#Entrada de una cadena

cadena = input('Ingresa una cadena: ')

#verificar si es palindromo o no

es_palindromo = cadena == cadena[::-1]

if es_palindromo:
    print(f'{cadena} es un palindromo')
else:
    print(f'{cadena} no es un palindromo')