def estado_agua(grados):
    """(number)->float
Ingresa la temperatura del agua en grados centigrados y nos dice su estado.
>>>estado_agua(45)
liquido
>>>estado_agua(-10)
solido
>>>estado_agua(120)
gaseoso"""

# Un primer if nos comparara el tipo de dato

    if type(grados) == int or type(grados) == float:
        
        if grados <= 0:
            return "Estado Solido"
        elif grados >= 1 and grados <= 99:
            return "Estado Liquido"
        elif grados >= 100:
            return "Estado Gaseoso"
    else:
        return "Valor introducido no valido"
