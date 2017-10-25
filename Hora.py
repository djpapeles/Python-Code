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

    # NZ: 13 horas menos que España | VE: 6 horas menos que España | AL: Igual que España
    # FRA: Igual que España         | ING: Una hora menos que Epaña| MR: Una hora menos que España

    print('')
    print('------------------------------------------------------------------------------')
    print('EXIT: Salir'.rjust(10),'| SPA: España'.rjust(10),'| NZ: Nueva Zelanda'.rjust(10),
      '| VE: Venezuela'.rjust(10),'| AL: Alemania'.rjust(10),'| FRA: Francia'.rjust(10))
    print('------------------------------------------------------------------------------')
    print('ING: Inglaterra'.rjust(10),'| MR: Marruecos'.rjust(10))
    print('------------------------------------------------------------------------------')
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
    elif choice=='EXIT':
        break
    # Hacemos una pausa para continuar
    pausa=input('Pulsa una tecla')
    # Limpiamos la pantalla, en Windows es os.system('cls')
    os.system('clear')
