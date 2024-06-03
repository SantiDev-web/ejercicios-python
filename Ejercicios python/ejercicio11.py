#Escribe un programa para convertir la temperatura de grados celsius a fahrenheit:

#Entrada de una temperatura en celsius:

celsius = float(input('Introduce la temperatura en grados celsius: '))

#convertir a fahrenheit
fahrenheit = (celsius * 9/5) + 32

#mostrar el resultado

print(f'{celsius} grados celsius son {fahrenheit} grados Fahrenheit')