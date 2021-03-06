#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Emmanuel Torres Molina"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('\n\nNuestra primera calculadora:\n\n')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''

    # Desarrollo de la Función:

    # Ingreso de Datos:
    print ('Ingrese el 1er Número Real: ')
    nro_1 = float (input ( ))

    print ('\nIngrese el 2do Número Real: ')
    nro_2 = float ( input ( ))

    # Suma:
    suma = nro_1 + nro_2

    # Resta:
    resta = nro_1 - nro_2

    # Multiplicación:
    producto = nro_1 * nro_2

    # División:
    division = nro_1 / nro_2

    # Exponente / Potencia:
    potencia = nro_1 ** nro_2

    print ('\nLa Suma entre', nro_1, 'y', nro_2, 'es:', suma)
    print ('\nLa Resta entre', nro_1, 'y', nro_2, 'es:', resta)
    print ('\nEl Producto entre', nro_1, 'y', nro_2, 'es:', producto)
    print ('\nLa División entre', nro_1, 'y', nro_2, 'es:', division)
    print ('\nLa Potencia entre', nro_1, '(base) y', nro_2, '(exponente) es:', potencia)


def ej2():
    print('\n\nEjercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''

    # Desarrollo de la función:
    
    # Ingreso de Datos:
    print ('\nIngrese Su Nombre Completo (Nombre y Apellido):')
    nombre_apellido = str ( input ( ) )

    print ('\nIngrese su DNI:')
    dni = int ( input ( ) )

    print ('\nIngrese su Edad:')
    edad = int ( input ( ) )

    print ("\nIngrese su Altura:")
    altura = float ( input ( ) )


    # Impresión de Datos por Consola:
    print ('\n\nNombre Completo:', nombre_apellido, '  DNI:', dni)
    print('\nNombre Completo:', nombre_apellido, '  Edad:', edad, '  Altura:', altura)



def ej3():
    print('\n\nEjercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''

    # Desarrollo de la Función:

    # Ingreso de Datos:
    print ('\nIngrese el Nombre Completo del Padre/Madre:')
    padre_1 = str ( input ( ) )

    print ('\nIngrese el Nombre Completo del Padre/Madre:')
    padre_2 = str ( input ( ) )

    print('\nAhora Ingrese sólo el/los Nombres del Hijo/a:')
    nombre_hijo = str ( input ( ) )

    apellido_hijo = str( padre_1.split (sep = ' ')[1] ) + ' ' + str( padre_2.split(sep = ' ')[1] )

    nombre_completo_hijo = nombre_hijo + ' ' + apellido_hijo

    print ('\nEl Nombre Completo del Hijo/a es:', nombre_completo_hijo)


def ej4():
    # Ejercicios de práctica con cadenas
    print('\nComencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''

    # Desarrollo de la Función:

    #Ingreso de los Datos:
    print('\n\nIngrese Nombre y Apellido de la 1er Persona: Formato: [Nombre Apellido]:')
    persona_1 = str ( input ( ) )

    print("\nIngrese Nombre y Apellido de la 2da Persona: Formato: [Nombre Apellido]:")
    persona_2 = str (input ())

    apellido_persona_2 = str ( persona_2.split (sep = ' ')[1] )

    if ( apellido_persona_2 in persona_1 ):
      print ('\n\n', persona_2, 'SI es pariente de', persona_1)

    else:
      print ('\n\n', persona_2, 'NO es pariente de', persona_1)


def ej5():
    # Ejercicios de práctica con cadenas
    print('\n\nAhora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

    # Desarrollo de la Función:

    # Ingreso de Datos:
    print('\nIngrese su Nombre Completo. (Nombre y Apellido):')
    nombre_completo = str ( input ( ) )

    print ('\nSu Nombre Completo es:', nombre_completo) 

    print('\n\nSu Nombre Completo con Todas las Letras en Minúscula es:', nombre_completo.lower( ) )
    print('\nSu Nombre Completo con Todas las Letras en Mayúscula es:', nombre_completo.upper( ) )
    print('\nSu Nombre Completo con la 1er Letra en Mayúscula es:', nombre_completo.capitalize( ) )
    print('\n\n')



if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
