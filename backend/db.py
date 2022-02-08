import psycopg2


class User:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pk = None

    def create_user(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO player (nombre) VALUES ('{self.nombre}') RETURNING pk")
        self.pk = cursor.fetchone()[0]
        connection.commit()

    def retrieve_user(self):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM player WHERE pk = {self.pk}")
            users = cursor.fetchall()
            return users


    def update_user(self, new_name):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )

        cursor = connection.cursor()
        self.nombre = new_name
        cursor.execute(f"UPDATE player SET nombre = '{new_name}' WHERE pk = {self.pk}")
        connection.commit()



    def delete_user(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM player WHERE pk = {self.pk}")
        connection.commit()
        self.pk = None

    def list_users(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM player")
        users = cursor.fetchall()
        return users


# -------------------------------------------------------------------------------------

class Team:
    def __init__(self, nombre, estadio):
        self.nombre = nombre
        self.estadio = estadio
        self.pk = None

    def create_team(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO equipo (nombre, estadio) VALUES ('{self.nombre}', '{self.estadio}') RETURNING pk")
        self.pk = cursor.fetchone()[0]
        connection.commit()

    def retrieve_team(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM equipo WHERE pk = {self.pk}")
        team = cursor.fetchall()
        return team

    def update_team(self, new_name, new_stadium):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            self.nombre = new_name
            self.estadio = new_stadium
            cursor.execute(f"UPDATE equipo SET nombre = '{new_name}', estadio = '{new_stadium}' WHERE pk = {self.pk} ")
            connection.commit()

    def delete_team(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM equipo WHERE pk = {self.pk}")
        connection.commit()
        self.pk = None

    def list_teams(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM equipo")
        teams = cursor.fetchall()
        return teams


## --------------------------------------------------------------------------------------------


class Player:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.pk = None

    def create_player(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes")

        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO jugadores (nombre, edad) VALUES ('{self.nombre}', {self.edad}) RETURNING pk")
        self.pk = cursor.fetchone()[0]
        connection.commit()

    def retrieve_player(self):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM jugadores WHERE pk = {self.pk}")
            players = cursor.fetchall()
            return players

    def update_player(self, new_name, new_edad):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )

            cursor = connection.cursor()
            self.nombre = new_name
            self.edad = new_edad
            cursor.execute(f"UPDATE jugadores SET nombre = '{new_name}', edad={new_edad} WHERE pk = {self.pk}")
            connection.commit()

    def delete_players(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM jugadores WHERE pk = {self.pk}")
        connection.commit()
        self.pk = None

    @staticmethod
    def list_players(cls):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM jugadores")
        players = cursor.fetchall()
        return players

# -------------------------------------------------------------------------------------

class Game:
    def __init__(self, duracion):
        self.duracion = duracion
        self.pk = None

    def create_game(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO partido(duracion) VALUES ('{self.duracion}') RETURNING pk")
        self.pk = cursor.fetchone()[0]
        connection.commit()

    def retrieve_game(self):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM partido WHERE pk = {self.pk}")
            game = cursor.fetchall()
            return game

    def update_game(self, new_duracion):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )

        cursor = connection.cursor()
        self.duracion = new_duracion
        cursor.execute(f"UPDATE partido SET duracion = {new_duracion} WHERE pk = {self.pk}")
        connection.commit()


    def delete_game(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM partido WHERE pk = {self.pk}")
        connection.commit()
        self.pk = None

    def list_games(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM partido")
        games = cursor.fetchall()
        return games


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
        connection.commit()

    def retrieve_usergame(self, pk_player):
        if pk_player is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM player_partido WHERE fk_player = {pk_player} ")
            usergame = cursor.fetchall()
            return usergame

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_usergame(self, new_fkpartido, new_fkplayer, pk_player):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )

    #    cursor = connection.cursor()
    #    self.fk_partido = new_fkpartido
    #    self.fk_player = new_fkplayer
    #    cursor.execute(f"UPDATE player_partido SET fk_partido = {new_fkpartido} , fk_player = {new_fkplayer} WHERE fk_player = {pk_player}")

    def delete_usergame(self,pk_player):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM player_partido WHERE fk_player = {pk_player}")
        connection.commit()

    def list_usersgames(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM player_partido")
        games = cursor.fetchall()
        return games

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
        connection.commit()

    def retrieve_playerteam(self, pk_equipo):
        if pk_equipo is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM jugadores_equipo WHERE fk_equipo = {pk_equipo}")
            playerteam = cursor.fetchall()
            return playerteam

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_playerteam(self, new_fkjugadores, new_fkequipo, pk_equipo):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )

    #    cursor = connection.cursor()
    #    self.fk_equipo = new_fkequipo
    #    self.fk_jugadores = new_fkjugadores
    #    cursor.execute(f"UPDATE jugadores_equipo SET fk_jugadores = {new_fkjugadores} , fk_equipo = {new_fkequipo} WHERE fk_equipo = {pk_equipo}")
    #    connection.commit()


    def delete_playerteam(self, pk_equipo):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM jugadores_equipo WHERE fk_equipo = {pk_equipo}")
        connection.commit()

    def list_playersteams(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM jugadores_equipo")
        playersteam = cursor.fetchall()
        return playersteam

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
        connection.commit()

    def retrieve_teamgame(self, pk_equipo):
        if pk_equipo is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM equipo_partido WHERE fk_equipo = {pk_equipo}")
            teamgame = cursor.fetchall()
            return teamgame

    # NO SÉ SI ESTA BIEN QUE UNA TABLA QUE SOLO TIENE FK SE PUEDA ACTUALIZAR

    #def update_teamgame(self, new_fkequipo, new_fkpartido, pk_equipo):
    #    connection = psycopg2.connect(
    #        host="127.0.0.1",
    #        database="pes",
    #        user="pes",
    #        password="pes"
    #    )

    #    cursor = connection.cursor()
    #    self.fk_equipo = new_fkequipo
    #    self.fk_partido = new_fkpartido
    #    cursor.execute(f"UPDATE equipo_partido SET fk_equipo = {new_fkequipo} , fk_partido = {new_fkpartido} WHERE fk_equipo = {pk_equipo}")}
    #    connection.commit()


    def delete_teamgame(self, pk_equipo):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM equipo_partido WHERE fk_equipo = {pk_equipo}")
        connection.commit()


# -------------------------------------------------------------------------------------

class Goal:
    def __init__(self, fk_partido):
        self.fk_partido = fk_partido
        self.pk = None

    def create_goal(self, pk_partido):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO goles (fk_partido) VALUES ({pk_partido}) RETURNING pk")
        self.pk = cursor.fetchone()[0]
        connection.commit()

    def retrieve_goal(self):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM goles WHERE pk = {self.pk}")
            goals = cursor.fetchall()
            return goals


    def update_goal(self, new_fkpartido):
        if self.pk is not None:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="pes",
                user="pes",
                password="pes"
            )
            cursor = connection.cursor()
            self.fk_partido = new_fkpartido
            cursor.execute(f"UPDATE goles SET fk_partido = {new_fkpartido} WHERE pk = {self.pk} ")
            connection.commit()


    def delete_goal(self):
        connection = psycopg2.connect(
            host="127.0.0.1",
            database="pes",
            user="pes",
            password="pes"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM goles WHERE pk = {self.pk}")
        connection.commit()
        self.pk = None


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

## +++ Iniciando Test de CRUD's +++ ##

#player = Player("Juan Carlos", 101)
#import ipdb; ipdb.set_trace()
