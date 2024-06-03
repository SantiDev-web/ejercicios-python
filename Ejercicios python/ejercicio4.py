#Factorial de un numero

#Entrada de un numero

num = int(input('Ingresa un numero: '))

#Calcular el factorial

factorial = 1

for i in range(1, num + 1):
    factorial *= i
    
#Mostrar el resultado

print(f'El factorial de {num} es {factorial}')