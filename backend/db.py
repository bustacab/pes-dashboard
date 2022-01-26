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

    def update_user(self, ur_pk, new_name):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"UPDATE player SET nombre = {new_name} WHERE pk = {ur_pk} ")

    def show_user(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM player WHERE nombre = {ur_pk}")
        users = cursor.fetchall()
        print(users)

    def delete_user(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM player WHERE pk = {ur_pk}")


# -------------------------------------------------------------------------------------

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

    def update_team(self, ur_pk, new_name, new_stadium):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"UPDATE equipo SET nombre = {new_name}, estadio={new_stadium} WHERE pk = {ur_pk} ")

    def show_team(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM equipo WHERE pk = {ur_pk}")
        teams = cursor.fetchall()
        print(teams)

    def delete_team(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM equipo WHERE pk = {ur_pk}")


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

    def update_players(self, new_name, new_edad, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )

        cursor = connection.cursor()
        cursor.execute(f"UPDATE jugadores SET nombre = {new_name}, edad={new_edad} WHERE pk = {ur_pk}")

    def show_players(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM jugadores WHERE pk = {ur_pk}")
        players = cursor.fetchall()
        print(players)

    def delete_players(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM jugadores WHERE pk = {ur_pk}")


# -------------------------------------------------------------------------------------

class Game:
    def __init__(self, duracion):
        self.duracion = duracion

    def create_game(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO partido(duracion) VALUES ({self.duracion})")

    def update_game(self, ur_pk, new_duracion):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )

        cursor = connection.cursor()
        cursor.execute(f"UPDATE partido SET duracion = {new_duracion} WHERE pk = {ur_pk}")

    def show_game(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM partido WHERE pk = {ur_pk}")
        games = cursor.fetchall()
        print(games)

    def delete_game(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM partido WHERE pk = {ur_pk}")


# -------------------------------------------------------------------------------------
class UserGame:
    def __init__(self, fk_partido, fk_player):
        self.fk_partido = fk_partido
        self.fk_player = fk_player

    def create_usergame(self, pk_partido, pk_player):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO player_partido(fk_partido, fk_player) VALUES ({pk_partido}, {pk_player})")

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_usergame(self, new_fkpartido, new_fkplayer, ur_pk):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )

    #    cursor = connection.cursor()
    #    cursor.execute(f"UPDATE player_partido SET fk_partido = {new_fkpartido} , fk_player = {new_fkplayer} WHERE fk_partido = {ur_pk}")

    def show_usergame(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM player_partido WHERE pk = {ur_pk}")
        usergame = cursor.fetchall()
        print(usergame)

    def delete_usergame(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM player_partido WHERE pk = {ur_pk}")


# -------------------------------------------------------------------------------------

class PlayersTeam:
    def __init__(self, fk_jugadores, fk_equipo):
        self.fk_jugadores = fk_jugadores
        self.fk_equipo = fk_equipo

    def create_playerteam(self, pk_jugadores, pk_equipo):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO jugadores_equipo(fk_jugadores, fk_equipo) VALUES ({pk_jugadores}, {pk_equipo})")

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_playerteam(self, new_fkjugadores, new_fkequipo, ur_pk):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )

    #    cursor = connection.cursor()
    #    cursor.execute(f"UPDATE jugadores_equipo SET fk_jugadores = {new_fkjugadores} , fk_equipo = {new_fkequipo} WHERE fk_jugadores = {ur_pk}")

    def show_playerteam(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM jugadores_equipo WHERE pk = {ur_pk}")
        playerteam = cursor.fetchall()
        print(playerteam)

    def delete_playerteam(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM jugadores_equipo WHERE pk = {ur_pk}")


# -------------------------------------------------------------------------------------

class TeamGame:
    def __init__(self, fk_equipo, fk_partido):
        self.fk_equipo = fk_equipo
        self.fk_partido = fk_partido

    def create_teamgame(self, pk_equipo, pk_partido):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO equipo_partido(fk_equipo, fk_partido) VALUES ({pk_equipo}, {pk_partido})")

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_teamgame(self, new_equipo, new_fkpartido, ur_pk):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )

    #    cursor = connection.cursor()
    #    cursor.execute(f"UPDATE equipo_partido SET fk_equipo = {new_fkequipo} , fk_partido = {new_fkpartido} WHERE fk_equipo = {ur_pk}")

    def show_teamgame(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM equipo_partido WHERE pk = {ur_pk}")
        teamgame = cursor.fetchall()
        print(teamgame)

    def delete_teamgame(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM equipo_partido WHERE pk = {ur_pk}")

# -------------------------------------------------------------------------------------

class Goal:
    def __init__(self, fk_partido):
        self.fk_partido = fk_partido

    def create_goal(self, pk_partido):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO goles (fk_partido) VALUES ({pk_partido})")

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_goal(self, new_fkpartido, ur_pk):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )
    #    cursor = connection.cursor()
    #    cursor.execute(f"UPDATE goles SET fk_partido = {new_fkpartido} WHERE pk = {ur_pk} ")

    def show_goal(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM goles WHERE fk_partido = {ur_pk}")
        goals = cursor.fetchall()
        print(goals)

    def delete_goal(self, ur_pk):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM goles WHERE pk = {ur_pk}")

# -------------------------------------------------------------------------------------

def connect_to_db():
    connection = psycopg2.connect(
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
