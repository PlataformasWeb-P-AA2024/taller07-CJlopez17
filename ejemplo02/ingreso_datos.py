from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from genera_tablas import Club, Jugador
import csv

# Crear una sesión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Leer los datos del archivo datos_clubs.txt
with open('data/datos_clubs.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Asegurarse de que la fila tenga exactamente 4 elementos
        id, nombre, deporte, fundacion = row
        club = Club(id=int(id), nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)

# Leer los datos del archivo datos_jugadores.txt
with open('data/datos_jugadores.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Asegurarse de que la fila tenga exactamente 5 elementos
        if len(row) == 5:
            id, nombre, dorsal, posicion, club_id = row
            jugador = Jugador(id=int(id), nombre=nombre, dorsal=int(dorsal), posicion=posicion, club_id=int(club_id))
            session.add(jugador)
        else:
            print(f"Línea ignorada en datos_jugadores.txt: {row}")

# Confirmar las transacciones
session.commit()

# Cerrar la sesión
session.close()

print("Datos ingresados correctamente.")
