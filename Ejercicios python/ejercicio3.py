#Numero par o impar:

#entrada de un numero

num = int(input('Ingresa un numero: '))

#Verificar si es par o impar 

if num % 2 == 0:
    print(f'{num} es un numero par')
else:
    print(f'{num} es un numero impar')