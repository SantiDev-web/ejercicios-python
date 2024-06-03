#Escribe un programa que encuentr el numero mas grade en una lista de numeros dada por el usuario

lista = list(map(int, input('Ingresa una lista de numeros separados por espacios: ').split()))

#encontrar el numero mas grande

max_num = max(lista)

#mostrar el resultado

print(f'El numero mas grande de la lista es: {max_num}')