import sqlite3
import csv
import click

def create_connection():
    connection = sqlite3.connect("newdata.db", check_same_thread=False)
    with open("newdata.sql") as f:
        connection.executescript(f.read())
    return connection

def close_connection(db):
    db.close()

def seed(connection):
    cursor = connection.cursor()
    with open('./organization_and_zones_dataset.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute(f"INSERT INTO zona (id, nombre) VALUES ({row[1]}, '{row[2]}')")
            cursor.execute(f"INSERT INTO organizacion (nombre, id_zona, coordenadas) VALUES ('{row[0]}',{row[1]},'{row[3]}')")
    connection.commit()
    with open('./timeseries_dataset.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            org, = cursor.execute(f"SELECT id FROM organizacion WHERE nombre == '{row[2]}'").fetchone()
            row[2] = org
            cursor.execute("INSERT INTO datos (timestamp, nombre_variable, id_organizacion, valor, tiempo_ingreso) VALUES (?,?,?,?,?)", row)
    
    connection.commit()