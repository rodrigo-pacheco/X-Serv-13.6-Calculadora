#!/usr/bin/python3
# Rodrigo Pacheco Martinez-Atienza
# Doble Grado Ing. Tecnología de las Telecomunicaciones e Ing. Aeroespacial en Aeronavegación

from sys import argv

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

operaciones = {'suma': sumar, 'resta': restar, 'multiplica': multiplicar, 'divide': dividir}
param = argv

print("Opciones de calculadora:\n", "- Suma\n", "- Resta\n", "- Multiplica\n", "- Divide\n")

try:
    resultado = operaciones[param[1]](int(param[2]), int(param[3]))
    print("Resultado: ", resultado)
except IndexError:
    print("Número de parámetros incorrecto")
except KeyError:
    print("Opción no soportada")

