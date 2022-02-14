# nombre = input("Cual es su nombre: ")
# apellido = input("Inserte su apellido: ")

# print( nombre + " " + apellido )

# numero_uno = input("Inserte un número: ")
# numero_dos = input("Inserte numero dos: ")

# numero_uno = int(numero_uno)
# numero_dos = int(numero_dos)

# print(numero_uno + numero_dos)

# Tipos de datos
# int
# bool
# str
# float
# list / tuple
# dict

# Operadores de Comparación
# == es igual
# != es diferente
# < es menor
# > es mayor

operacion = input("Que operación desea realizar: ")

if operacion == "resta":
    numero_uno = int(input("Inserte el primer número: "))
    numero_dos = int(input("Inserte el segundo número: "))

    print(numero_uno - numero_dos)

elif operacion == "suma":
    numero_uno = int( input("Digame un número: ") )
    numero_dos = int( input("Digame otro número: ") )

    print( numero_uno + numero_dos )
elif operacion == "multiplicacion":
    numero_uno = int( input("Numero uno: ") )
    numero_dos = int( input("Numero dos: ") )

    print(numero_uno * numero_dos)
elif operacion == "division":
    numero_uno = int( input("Numero uno: ") )
    numero_dos = int( input("Numero dos: ") )

    print(numero_uno / numero_dos)
else:
    print("No es ni suma ni resta ni multiplicación ni división")


print("Esto se ejecuta al final")