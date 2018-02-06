#!/usr/bin/python3
# Rodrigo Pacheco Martinez-Atienza
# Doble Grado Ing. Tecnología de las Telecomunicaciones
# e Ing. Aeroespacial en Aeronavegación

import sys
import operator

operaciones = {'suma': operator.add,
               'resta': operator.sub,
               'multiplica': operator.mul,
               'divide': operator.truediv}
param = sys.argv

print("\nUso: python3 calculadora.py 'opción' valor1 valor2\n\n",
      "Opciones de calculadora:\n",
      "- Suma\n", "- Resta\n", "- Multiplica\n", "- Divide\n")

try:
    resultado = operaciones[param[1]](float(param[2]), float(param[3]))
    print("Resultado: ", resultado)
except IndexError:
    print("Número de parámetros incorrecto")
    sys.exit
except KeyError:
    print("Opción no soportada")
    sys.exit
except ZeroDivisionError:
    print("División por 0. Resultado es 0")
    sys.exit
except ValueError:
    print("Valor introducido erróneo. Debe ser número")
    sys.exit
