#---------------------------------------------------------------#
#   Registro de estudiantes mediante tupla y diccionario        #
#---------------------------------------------------------------#

# 1.Definir tupla de estudiantes

estudiante1 =('Santi Luque', 101, {'Python': 5, 'React': 5, 'Java': 0})
estudiante2 =('David Corral', 102, {'Python': 9, 'React': 0, 'Java': 10})
estudiante3 =('Pepito Grillo', 103, {'Python': 7, 'React': 6, 'Java': 5})

#2. Crear un diccionario para guardar estos estudiantes:

registro_estudiantes ={
    estudiante1[1]: estudiante1,
    estudiante2[1]: estudiante2,
    estudiante3[1]: estudiante3,
}

# 3.Calcular el promedio de cada estudiante:

promedios={}

for id_estudiante, estudiante in registro_estudiantes.items():
    nombre, id, calificaciones = estudiante
    promedio = sum(calificaciones.values()) / len(calificaciones)
    promedios[id] = promedio

# 4.Imprimir resultados
for id_estudiante, estudiante in registro_estudiantes.items():
    nombre, id, calificaciones = estudiante
    promedio = promedios[id]
    print(f"Estudiante: {nombre} (ID: {id})")
    print(f" Calificaciones: {calificaciones} ")
    print(f" Promedios: {promedio:.2f}")
    print()