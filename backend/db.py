import psycopg2


def create_user(nombre):
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
    cursor = connection.cursor() #Cursor para ingresar querys
    cursor.execute(f"INSERT INTO player (nombre) VALUES ({nombre})")

def create_team(estadio, nombre):
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO equipo(estadio, nombre) VALUES ({estadio, nombre})")

def create_players(nombre, edad):
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO jugadores(nombre, edad) VALUES ({nombre}, {edad})")

def connect_to_db():
    connection = psycopg2.connect( #Conexion con db utilizando modulo psycopg2 la funcion connect
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM player")
    partidos = cursor.fetchall()
    for partido in partidos:
        print(partido)


connect_to_db()