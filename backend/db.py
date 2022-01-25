import psycopg2

class User:
    def __init__(self, nombre):
        self.nombre = nombre
    

    def create_user(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        cursor = connection.cursor() 
        cursor.execute(f"INSERT INTO player (nombre) VALUES ({self.nombre})")

    def update_user(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        id = input("Ingrese su ID: ")
        new_name = input("Ingrese su nuevo nombre: ")
        cursor = connection.cursor() 
        cursor.execute(f"UPDATE player SET nombre = {new_name} WHERE pk = {id} ")

    def show_user(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        cursor = connection.cursor() 
        print (cursor.execute(f"SELECT * FROM player WHERE nombre = {self.nombre}"))

##-------------------------------------------------------------------------------------

class Team:
    def __init__(self, nombre, estadio):
        self.nombre = nombre
        self.estadio = estadio

    def create_team(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        cursor = connection.cursor() 
        cursor.execute(f"INSERT INTO equipo (nombre, estadio) VALUES ({self.nombre}, {self.estadio})")


    def update_team(self): #IGUAL QUE UPDATE PLAYERS, PREGUNTAR
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        ur_pk = input ("ID de equipo a modificar: ")
        new_name = input("Nuevo nombre de equipo: ")
        new_stadium = input ("Nuevo Estadio: ")
        
        cursor = connection.cursor() 
        cursor.execute(f"UPDATE equipo SET nombre = {new_name}, estadio={new_stadium} WHERE pk = {ur_pk} ")

    def show_team(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        cursor = connection.cursor()  #PREGUNTAR SI HACE FALTA PRINT PARA QUE SE VEA EN PANTALLA
        print (cursor.execute(f"SELECT * FROM equipo WHERE nombre = {self.nombre}"))

## --------------------------------------------------------------------------------------------


class Players:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def create_players(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes")
        
        cursor = connection.cursor() 
        cursor.execute(f"INSERT INTO jugadores (nombre, edad) VALUES ({self.nombre}, {self.edad})")

    def update_players(self, new_name, new_edad, ur_pk): #IGUAL QUE UPDATE TEAM, PREGUNTAR. ARGUMENTOS DESDE FUERA O INPUT DENTRO QUE ES MEJOR
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
     
        cursor = connection.cursor() 
        cursor.execute(f"UPDATE jugadores SET nombre = {new_name}, edad={new_edad} WHERE pk = {ur_pk}")


    def show_players(self):
        connection = psycopg2.connect(
        host="127.0.0.1",
        database="pes",
        user="pes",
        password="pes"
    )
        cursor = connection.cursor() 
        cursor.execute(f"SELECT * FROM jugadores WHERE nombre = {self.nombre}")

## -------------------------------------------------------------------------------------

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