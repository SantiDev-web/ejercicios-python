#Escribe un programa que implemente una calculadora simple con las operaciones suma , resta , multiplicacion y division:

#Funcion para realizar las operaciones

def calculadora(a,b,operacion):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicacion':
        return a * b
    elif operacion == 'division':
        return a / b
    else: 
        return 'operacion no valida'
    
#Entrada de los numeros y operacion:

num1 = float(input('Ingresa el primero numero: '))
num2 = float(input('Ingresa el segundo numero: '))
operacion = input('Ingresa la operacion (suma, resta, multiplicacion, division): ').lower()

#Realizar la operacion y mostrar el resultado

resultado = calculadora(num1, num2, operacion)
print(f'El resultado de la {operacion} es : {resultado}')