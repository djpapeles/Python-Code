import os

print("""
=======================
Calculadora de IVA v1.0
=======================
""")

porcentaje = input("Escribe el porcentaje de IVA a calcular: ")

print("Has elegido el " + porcentaje + " por ciento")

cantidad = input("Ahora escribe la cantidad para calcular: ")

def IVA(x):
	resultado = ((x * 21) / 100) + x
	return resultado

def soloiva(x):
	resultado = (x * 21) / 100
	return resultado

print("==================================")

print("El IVA es: ")

print(soloiva(int(cantidad)))

print("")

print("La cantidad con IVA es: ")

print(IVA(int(cantidad)))

print("==================================")

os.system("pause")