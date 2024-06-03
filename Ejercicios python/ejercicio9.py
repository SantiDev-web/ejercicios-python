#Escribe un programa que cuente el numero de vocales en una cadena dada

#entrada de una cadena

cadena = input('ingresa una cadena: ')

#contar vocales

vocales = 'aeiouAEIOU'
contador = sum(1 for char in cadena if char in vocales)

#mostrar el resultado

print(f'El numero de vocales en la cadena dada es: {contador}')