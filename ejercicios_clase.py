#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Emmanuel O. Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('\nIngrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    print ("\nLos Números Enteros Ingresados son:\nNúmero 1:", numero_1, "\nNúmero 2: ", numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    result = numero_1 + numero_2
    print ('\nEl resultado de Sumar', numero_1, 'y', numero_2, 'es:', result)
   
    # Resta
    result = numero_1 - numero_2
    print ('\nEl resultado de Restar', numero_1, 'y', numero_2, 'es:', result)

    # División
    result = numero_1 / numero_2
    print ('\nEl resultado de Dividir', numero_1, 'y', numero_2, 'es:', result)

    # Multiplicación
    result = numero_1 * numero_2
    print ('\nEl resultado de Multiplicar', numero_1, 'y', numero_2, 'es:', result)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('\n\nIngrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)
    print ('\n\nLos Números Reales Ingresados son:')
    print ('Número 1: ', numero_3)
    print ('Número 2: ', numero_4)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    result = numero_3 + numero_4
    print ('\nEl resultado de Sumar', numero_3, 'y', numero_4, 'es:', result)

    # Resta
    result = numero_3 - numero_4
    print ('\nEl resultado de Restar', numero_3, 'y', numero_4, 'es:', result)

    # División
    result = numero_3 / numero_4
    print ('\nEl resultado de Dividir', numero_3, 'y', numero_4, 'es:', result)

    # Multiplicación
    result = numero_3 * numero_4
    print ('\nEl resultado de Multiplicar', numero_3, 'y', numero_4, 'es:', result)


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('\n\nIngrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print ("\nSu Nombre Completo es:", nombre, apellido)

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    nombre_completo = nombre + ' ' + apellido

    # Imprimir la cantidad de letras que posee su nombre completo
    aux = 0 # Inicializo la Variable

    for k in range (0, len(nombre_completo)):       # Cuento la cant. de espacios que tiene mi nombre completo
        if nombre_completo[k] == ' ' :
            aux  = aux + 1
        
    print('\nLa Cantidad de letras que tiene su nombre completo es:', len(nombre_completo) - aux)


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('\n\nIngrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    print ('Ingrese palabra 4:')
    palabra_4 = str ( input ( ) )

    print ('Ingrese palabra 5:')
    palabra_5 = str ( input ( ) )

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    acronimo = palabra_1[0] + palabra_2[0] + palabra_3[0] + palabra_4[0] + palabra_5[0]

    # Imprimir el resultado en pantalla
    print('\nEl acrónimo obtenido de la combinación de la 1er letra de las palabras ingresadas es:', acronimo)


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('\n\nIngrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    prim_3_letras = palabra_1[0:3]

    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    ult_3_letras = palabra_2[-3:-1] + palabra_2[-1]

    # Formar una nueva palabra con los recortes solicitados
    palabra_nueva = prim_3_letras + ult_3_letras

    # Imprima en pantalla los resultados
    print ('\nLa Nueva Palabra formada con los Recortes Solicitados es:', palabra_nueva)
    print("\n\n\n")

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
