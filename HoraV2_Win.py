print(""" 
        ******************************************************************************
        HORAS EN EL MUNDO, SELECCIONA EN QUE LUGAR DEL MUNDO QUIERES SABER QUE HORA ES
        ****************************************************************************** """)
print('')

# Importamos los modulos necesarios para usar el tiempo
from datetime import datetime, date, time, timedelta
import calendar

# Importamos el modulo para crear la tabla
from terminaltables import AsciiTable

# Importamos el modulo os para limpiar la pantalla
import os

# Declaramos la variables a usar para encontrarlas facilmente
choice=''
pausa=''
reloj=datetime.now() # Objeto datetime.now para usar despues

# Creamos el contenido de la tabla
table_data=[
    ['Codigo', 'Pais'],
    ['SPA', 'España'],
    ['NZ', 'Nueva Zelanda'],
    ['VE', 'Venezuela'],
    ['AL', 'Alemania'],
    ['FRA', 'Francia'],
    ['ING', 'Inglaterra'],
    ['MR', 'Marruecos'],
    ['NOR', 'Noruega'],
    ['BOL', 'Bolivia'],
    ['FIL', 'Filipinas'],
    ['NEP', 'Nepal'],
    ['EXIT', 'Salir']
]

# Instanciamos table como un tipo AsciiTable
table=AsciiTable(table_data)

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

    print('')
    
    # Imprimimos en pantalla la tabla previamente creada
    print(table.table)
    
    print('')

    # Ofrecemos que el usuario elija un pais
    choice=input('Haz tu seleccion: ')
    print('')
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
    print('')
    pausa=input('Pulsa una tecla')
    # Limpiamos la pantalla, en Windows es os.system('cls') y en Linux es os.system('clear')
    os.system('cls')
