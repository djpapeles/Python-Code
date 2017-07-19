print("""
=====================
Extractor de IVA v1.0
=====================
""")

porcentaje = input("Escriba el porcentaje de IVA a extraer: ")

cantidad = input("Ahora escriba la cantidad a sacarle el IVA: ")

def sacariva(x):
	resultado = x / ((int(porcentaje) / 100) + 1)
	return resultado

print("La cantidad sin IVA es: ")

print(sacariva(int(cantidad)))