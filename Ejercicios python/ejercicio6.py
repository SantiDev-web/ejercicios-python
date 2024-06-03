#Numero primo:

#Entrada de un numero

num = int(input('Ingrese un numero: '))

#Verificar si es primo o no 
es_primo = True

if num > 1:
    for i in range(2, int(num **0.5)+ 1):
        if num % i == 0:
            es_primo = False
            break
else:
    es_primo = False
    
#Mostrar el resultado

if es_primo:
    print(f'{num} es un numero primo')
else:
    print(f'{num} no es un numero primo')