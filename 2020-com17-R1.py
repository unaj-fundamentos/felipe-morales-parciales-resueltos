
# Ejercicio 2b
# Programe una función de nombre imprimir_menores_que, que reciba una lista de números y un número tope,
# la cual debe imprimir por pantalla aquellos números de la lista menores que el número tope ingresado 
# (10 puntos).
#Ejemplo: imprimir_menores_que([2, 4, -67, 9], 0) deberá imprimir -67.

#Lugar de definición de funciones
#def imprimir_menorestope_que(lista, tope):
#	lista_edad = []
#	for n in lista:
#		if n <= tope:
#			lista_edad.append(n)
#	return lista_edad

# programa o lugar de invocaciones	
#lista_numeros = [2,4,-67,9]
#limite = int(input("ingrese un numero "))
#print (imprimir_menores_que(lista_numeros, limite))

# Ejercicio 3
#Realice un programa para una plataforma online a través del cual pueda ingresar el nombre de las personas, curso a realizar y 
#su edad. La carga finaliza cuando se ingresa edad en -1.
def cargar_datos():
    lista = []
    edad = int(input("Ingrese la edad, y la carga finaliza cuando ingresa -1: "))
    while edad != -1:
        nombre = input("Ingrese el nombre: ")
        curso = input("Ingrese el curso: ")
        dato = [nombre, curso, edad]
        lista.append(dato)
        edad = int(input("Ingrese la edad, y la carga finaliza cuando ingresa -1: "))
    return lista    


#Luego, deberá imprimir las edades de las personas menores a 80 años.
def imprimir_edades(lista):
    for p in lista:
        edad = p[2]
        if edad <= 80:
            print(edad)

#Por último calcular el promedio de edades de las personas que cursen “Ventas ágiles”. (40 puntos).
def promedio_edades(lista):
    suma = 0
    cant = 0
    for p in lista:
        edad = p[2]
        curso = p[1]
        if curso == "Ventas ágiles":
            suma = suma + edad
            cant = cant + 1
    if cant != 0:
        promedio = suma/cant
    else:
        promedio = 0    
    return promedio

# Zona de invocaciones a las funciones previamente definidas
lista_personas = cargar_datos()
print(lista_personas)
imprimir_edades(lista_personas)
p = promedio_edades(lista_personas)
print("El promedio de mayores a 80 años es " + str(p))
