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
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        # Asegurarse de que la fila tenga exactamente 3 elementos
        if len(row) == 3:
            nombre, deporte, fundacion = row
            club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
            session.add(club)
        else:
            print(f"Línea ignorada en datos_clubs.txt: {row}")

# Leer los datos del archivo datos_jugadores.txt
with open('data/datos_jugadores.txt', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        # Asegurarse de que la fila tenga exactamente 4 elementos
        if len(row) == 4:
            club_nombre, posicion, dorsal, nombre = row
            # Buscar el club por nombre
            club = session.query(Club).filter_by(nombre=club_nombre).first()
            if club:
                jugador = Jugador(nombre=nombre, dorsal=int(dorsal), posicion=posicion, club_id=club.id)
                session.add(jugador)
            else:
                print(f"Club no encontrado para jugador: {row}")
        else:
            print(f"Línea ignorada en datos_jugadores.txt: {row}")

# Confirmar las transacciones
session.commit()

# Cerrar la sesión
session.close()

print("Datos ingresados correctamente.")
