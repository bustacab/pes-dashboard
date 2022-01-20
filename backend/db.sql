CREATE TABLE player(
pk serial PRIMARY KEY,
nombre varchar(100) NOT NULL
);

CREATE TABLE equipo(
pk serial PRIMARY KEY,
estadio varchar(100),
nombre varchar(100) NOT NULL
);


CREATE TABLE jugadores(
pk serial PRIMARY KEY,
nombre varchar(100) NOT NULL,
edad int
);


CREATE TABLE partido(
pk serial PRIMARY KEY
);

CREATE TABLE goles(
pk serial PRIMARY KEY,
fk_partido serial,
  
FOREIGN KEY (fk_partido)
  REFERENCES partido(pk)
  ON DELETE restrict
  ON UPDATE cascade

);


CREATE TABLE player_partido(
fk_partido serial,
fk_player serial,

FOREIGN KEY (fk_partido)
  REFERENCES partido(pk)
  ON DELETE restrict
  ON UPDATE cascade,
FOREIGN KEY (fk_player)
  REFERENCES player(pk)
  ON DELETE restrict
  ON UPDATE cascade
);


CREATE TABLE jugadores_equipo(
fk_jugadores serial,
fk_equipo serial,
  
FOREIGN KEY (fk_jugadores)
  REFERENCES jugadores(pk)
  ON DELETE cascade
  ON UPDATE cascade,
FOREIGN KEY (fk_equipo)
  REFERENCES equipo(pk)
  ON DELETE restrict
  ON UPDATE cascade
);


CREATE TABLE equipo_partido(
fk_equipo serial,
fk_partido serial,

FOREIGN KEY (fk_equipo)
  REFERENCES equipo(pk)
  ON DELETE restrict
  ON UPDATE cascade,
FOREIGN KEY (fk_partido)
  REFERENCES partido(pk)
  ON DELETE restrict
  ON UPDATE cascade
  
);