print("""
=========================
Conversor de monedas v1.0
=========================""")

def euroadolaramerica(x):
	"""(number)->number
	Devuelve la conversion de euros a dolares americanos
	>>>euroadolaramerica(45)
	32"""
	conversion = x * 1.35750
	return conversion

def euroalibra(x):
	conversion = x * 0.799786
	return conversion

def eurodoadolarcanada(x):
	conversion = x * 1.47280
	return conversion

cantidad = input("Introduce cantidad de euros a convertir: ")

print("Tu cantidad corresponde a", euroadolaramerica(int(cantidad)), "dolares americanos")

print("Tu cantidad corresponde a", eurodoadolarcanada(int(cantidad)), "dolares canadienses")

print("Tu cantidad corresponde a", euroalibra(int(cantidad)), "libras esterlinas")
