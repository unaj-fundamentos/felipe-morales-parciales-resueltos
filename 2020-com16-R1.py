# ¡SE RECOMIENDA LEER EL EXAMEN COMPLETO Y LUEGO ELABORAR UNA ESTRATEGIA PARA SU RESOLUCIÓN!

# 1) Programar en Python (20 puntos):
print("Ejercicio 1a")
# a) Pedir el ingreso de los 4 números de una tarjeta de débito y/o de crédito e imprimir dicha información
#    con el siguiente formato: **** **** **** 9999 (9999 representa al último número ingresado). 
#    Por ejemplo si ingresa 1256 8956 7825 2589, deberá imprimir **** **** **** 2589. 
#    En caso que algunos de los números no tenga 4 dígitos, imprimir el cartel “Los números ingresados no 
#    se pueden procesar.”

#num1 = input("Ingrese el primer numero: ")
#num2 = input("Ingrese el segundo numero: ")
#num3 = input("Ingrese el tercer numero: ")
#num4 = input("Ingrese el cuarto numero: ")
#if len(num1)==4 and len(num2)==4 and len(num3)==4 and len(num4)==4:
#    numero = "**** **** **** " + num4
#    print(numero)
#else:
#    print("Los números ingresados no se pueden procesar.")    


# b) Ingresar por teclado el alto, largo y ancho de una habitación, y calcular la superficie total para 
#    pintar sus paredes y techo. Además dicha habitación tiene ocupado 5m2 en aberturas, las cuales 
#    NO se deben pintar. Deberá controlar que la superficie sea mayor que 5m2 para poder pintar, 
#    si no imprimir “No se puede determinar la superficie a pintar”.


#def superficie_habitacion_a_pintar(alto, largo, ancho, sup_aberturas):
#    sup_techo = largo * ancho
#    sup_piso = largo * ancho
#    sup_paredes_largas = alto * largo * 2
#    sup_paredes_cortas = alto * ancho * 2
#    sup_pintar = sup_techo + sup_piso + sup_paredes_largas + sup_paredes_cortas - sup_aberturas
#    if sup_pintar > 0:
##        return sup_pintar 
#    else:
#        return -1

#v_alto = int(input("Ingrese alto: "))
#v_ancho = int(input("Ingrese ancho: "))
#v_largo = int(input("Ingrese largo: "))
##sp = superficie_habitacion_a_pintar(v_alto, v_largo, v_ancho, 6)
#if sp != -1:
#    print("Usted puede pintar la siguiente superficie: " + str(sp))
#else:
#    print("No se puede determinar la superficie a pintar")    


# 2) Programar en Python las siguientes funciones con sus respectivas invocaciones (40 puntos):
# a) Programe una función de nombre superficie_habitacion_a_pintar, que recibe por parámetros el alto, largo, 
#    ancho y superficie de aberturas -no pintar-. La función debe devolver los metros totales para pintar 
#    sus paredes y techo. En caso de que la superficie a pintar esté por debajo de la superficie a omitir, 
#    devolver -1. (30 puntos)
#    Ejemplo: superficie_habitacion_a_pintar(3, 10, 5, 200) deberá devolver -1.
#print("Ejercicio 2a")
#print(superficie_habitacion_a_pintar(3, 10, 5, 200))

# b) Programe una función de nombre imprimir_mayores_que, que reciba una lista de números y un número tope,
#    la cual debe imprimir por pantalla aquellos números de la lista mayores que el número tope ingresado 
#    (10 puntos).
#    Ejemplo: imprimir_mayores_que([2, 4, -67, 9], 0) deberá imprimir 2, 4 ,9.

print("Ejercicio 2b")
def imprimir_mayores_que(lista, tope):
    for x in lista:
        if x >= tope:
            print(x)

imprimir_mayores_que([2, 4, -67, 9], 0) 

print("Ejercicio 3")
# 3) Realice un programa para una plataforma online a través del cual pueda ingresar el nombre de las 
#    personas, curso a realizar y su edad. La carga finaliza cuando se ingresa el nombre ‘ZZZ’. 
lista_personas = []
nombre = input("Ingrese nombre de la persona, la carga termina con ZZZ: ")
while nombre != "ZZZ":
    curso = input("Ingrese el curso: ")
    edad = int(input("Ingrese edad: "))
    dato = [nombre, curso, edad]
    lista_personas.append(dato)
    nombre = input("Ingrese nombre de la persona, la carga termina con ZZZ: ")
print(lista_personas)


#    Luego, deberá imprimir las edades mayores a 18.
lista_edades = []
for x in lista_personas:
    lista_edades.append(x[2])

imprimir_mayores_que(lista_edades, 18)


#    Por último calcular el promedio de edades de las personas que cursen “Machine Learning”. (40 puntos).
#    Nota: Se recomienda utilizar funciones!
suma = 0
cant = 0
for x in lista_personas:
    curso = x[1]
    edad = x[2]
    if curso == "Machine Learning":
        suma = suma + edad
        cant = cant + 1
if cant != 0:        
    print("El promedio de las edades es de " + str(suma/cant))
else:
    print ("No hay datos para procesar")    



