from functools import reduce

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


def GenerarEstructura(nom, n1, n2):
   lista_nombres = nom.replace("'","").replace(" ","").replace("\n","").lower().split(",")
   lista_alumnos = zip(lista_nombres,n1,n2)
   return lista_alumnos


def PromedioEstudiante(lista_alumnos):
   return list(map(lambda n: (n[1]+n[2])/2, lista_alumnos))


def PromedioCurso(lista_promedios):
   return reduce(lambda x,y: (x+y), lista_promedios)/len(lista_promedios)


def Promedio_Maximo (lista_alumnos):
   max = -1
   prom = 0
   nombre_max = " "
   for nombre, nota1 , nota2 in lista_alumnos:
      prom = ((nota1 + nota2) / 2)
      if (prom > max):
         max = prom
         nombre_max = nombre
   return (nombre_max,max)

def Nota_baja (lista_alumnos):
   min = 1000
   nombre_min = " "
   for nombre, nota1 , nota2 in lista_alumnos:
      if (nota1 < min):
         min = nota1
         nombre_min = nombre
      if (nota2 < min):
         min = nota2
         nombre_min = nombre
   return (nombre_min,min)


#Cada punto se tiene que hacer por separado porque se modifican las listas.

#Punto A: se genera la estructura con los 3 datos.
lista_alumnos = GenerarEstructura(nombres,notas_1,notas_2)
#Comento la siguientes lineas porque para utilizar las funciones no son necesarias.
"""print("Lista de tuplas con los tres datos (nombre, nota1, nota2): ")
print(list(lista_alumnos))"""

#Punto B: Creamos una lista con los promedios de cada alumno.
print("Lista con los promedios de cada alumnos: ")
print(PromedioEstudiante(tuple(lista_alumnos)))


#Punto C: Calculamos el promedio general del curso.
print("Promedio general del curso: ")
lista_promedios = PromedioEstudiante(tuple(lista_alumnos))
print(PromedioCurso(tuple(lista_promedios)))


#Punto D: Identificamos al estudiante con el promedio de notas mas alto.
print("El estudiante con promedio mas alto es (nombre, nota):")
print(Promedio_Maximo(lista_alumnos))

#Punto E: Identificamos al estudiante con la nota mas baja.
print("El estudiante con la nota mas baja es (nombre, nota):")
print(Nota_baja(lista_alumnos))
