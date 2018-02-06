#!/usr/bin/python3
# Rodrigo Pacheco Martinez-Atienza
# Doble Grado Ing. Tecnología de las Telecomunicaciones
# e Ing. Aeroespacial en Aeronavegación

import sys
import operator

NUM_ARGS = 4

operaciones = {'suma': operator.add,
               'resta': operator.sub,
               'multiplica': operator.mul,
               'divide': operator.truediv}
param = sys.argv

if param != NUM_ARGS:
    sys.exit("Usage error: [operator] [number1] [number2]")

print("\nUso: python3 calculadora.py 'opción' valor1 valor2\n\n",
      "Opciones de calculadora:\n",
      "- Suma\n", "- Resta\n", "- Multiplica\n", "- Divide\n")

try:
    resultado = operaciones[param[1]](float(param[2]), float(param[3]))
    print("Resultado: ", resultado)
except IndexError:
    sys.exit("Usage error: [operator] [number1] [number2]")
except KeyError:
    sys.exit("Opción no soportada")
except ZeroDivisionError:
    sys.exit("División por 0. Resultado es 0")
except ValueError:
    sys.exit("Valor introducido erróneo. Debe ser número")
