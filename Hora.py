print(""" 
        ******************************************************************************
        HORAS EN EL MUNDO, SELECCIONA EN QUE LUGAR DEL MUNDO QUIERES SABER QUE HORA ES
        ****************************************************************************** """)
print('')

# Importamos los modulos necesarios para usar el tiempo
from datetime import datetime, date, time, timedelta
import calendar

# Importamos el modulo os para limpiar la pantalla
import os

# Declaramos la variables a usar para encontrarlas facilmente
choice=''
pausa=''
reloj=datetime.now() # Objeto datetime.now para usar despues

# Funcion para añadir o restar horas a la actual
def modificador(x):
    r=datetime.now()
    h=r+timedelta(hours=x)
    h=time(h.hour,h.minute,h.second)
    return h

while True:

    # Mostramos la hora local en pantalla
    print('La hora actual es ',time(reloj.hour,reloj.minute,reloj.second))
        
    print('')

    print('Elige del listado, en que lugar del mundo quieres saber la hora:')
	
	# con rjust(10) justificamos el texto a la derecha

    print('')
    print('---------------------------------------------------------------------------------------------------')
    print('EXIT: Salir'.rjust(10),'| SPA: España'.rjust(10),'| NZ: Nueva Zelanda'.rjust(10),
		  '| VE: Venezuela'.rjust(10),'| AL: Alemania'.rjust(10),'| FRA: Francia'.rjust(10))
    print('---------------------------------------------------------------------------------------------------')
    print('ING: Inglaterra'.rjust(10),'| MR: Marruecos'.rjust(10),'| NOR: Noruega'.rjust(10),
          '| BOL: Bolivia'.rjust(10), '| FIL: Filipinas'.rjust(10),'| NEP: Nepal'.rjust(10))
    print('---------------------------------------------------------------------------------------------------')
    print('RUS: Rusia'.rjust(10),'|SUE: Suecia'.rjust(10),'|PAK: Pakistan'.rjust(10),
          '|HON: Honduras'.rjust(10),'|LET: Letonia'.rjust(10),'|LAO: Laos'.rjust(10),'|SUI: Suiza'.rjust(10))
    print('---------------------------------------------------------------------------------------------------')
    print('')

    # Ofrecemos que el usuario elija un pais
    choice=input('Haz tu seleccion: ')
    # Segun la eleccion del usuario se mostrara la hora en un pais o en otro
    if choice=='NZ':
        print('La hora en Nueva Zelanda es ', modificador(-13))
    elif choice=='SPA':
        print('La hora en España es ', time(reloj.hour,reloj.minute,reloj.second))
    elif choice=='VE':
        print('La hora en Venezuela es ', modificador(-6))
    elif choice=='AL':
        print('La hora en Alemania es ', modificador(0))
    elif choice=='FRA':
        print('La hora en Francia es ', modificador(0))
    elif choice=='ING':
        print('La hora en Inglaterra es ', modificador(-1))
    elif choice=='MR':
        print('la hora en Marruecos es ', modificador(-1))
    elif choice=='NOR':
        print('la hora en Noruega es ', modificador(0))
    elif choice=='BOL':
        print('la hora en Bolivia es ', modificador(-6))
    elif choice=='FIL':
        print('la hora en Filipinas es ', modificador(-18))
    elif choice=='NEP':
        print('la hora en Nepal es ', modificador(+4))
    elif choice=='RUS':
        print('la hora en Rusia es ', modificador(+1))
    elif choice=='SUE':
        print('la hora en Suecia es ', modificador(0))
    elif choice=='PAK':
        print('la hora en Pakistan es ', modificador(+3))
    elif choice=='HON':
        print('la hora en Honduras es ', modificador(-8))
    elif choice=='LET':
        print('la hora en Letonia es ', modificador(+1))
    elif choice=='LAO':
        print('la hora en Laos es ', modificador(-19))
    elif choice=='SUI':
        print('la hora en Suiza es ', modificador(0))
    elif choice=='EXIT':
        break
    # Hacemos una pausa para continuar
    pausa=input('Pulsa una tecla')
    # Limpiamos la pantalla, en Windows es os.system('cls')
    os.system('cls')