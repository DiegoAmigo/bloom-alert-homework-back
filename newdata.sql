DROP TABLE IF EXISTS zona;
DROP TABLE IF EXISTS organizacion;
DROP TABLE IF EXISTS datos;

CREATE TABLE zona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NULL
);

CREATE TABLE organizacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NULL,
    id_zona INTEGER NULL,
    coordenadas TEXT NULL,
    FOREIGN KEY (id_zona) REFERENCES zona (id)
);

CREATE TABLE datos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NULL,
    nombre_variable TEXT NULL,
    id_organizacion INTEGER NULL,
    valor REAL NULL,
    tiempo_ingreso DATETIME NULL,
    FOREIGN KEY (id_organizacion) REFERENCES organizacion (id)
);