from fastapi import FastAPI, HTTPException
import utils
import database
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:8000/", "http://localhost"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
    )

db = database.create_connection()
database.seed(db)
db.close()


@app.get("/data/{org_id}")
def read_root(org_id, timestamp_start = None, timestamp_end = None, variable = None, digest_start = None, digest_end = None):
    rows = []
    connection = sqlite3.connect("newdata.db")
    cursor = connection.cursor()
    query_filter = ''
    args = [timestamp_start, timestamp_end, variable, digest_start, digest_end]
    query_filter = utils.filter_query(args, query_filter)
    try:
        data = cursor.execute(f"SELECT * from DATOS WHERE id_organizacion == {org_id}{query_filter}").fetchall()
        for vals in data:
            rows.append({"timestamp": vals[1], "variable": vals[2], "value": vals[4], "ingestionTime": vals[5]})
        return {"data": rows}
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"error detected:\n {err}")
        

@app.get("/orgs")
async def read_orgs2():
    rows = []
    connection = sqlite3.connect("newdata.db")
    cursor = connection.cursor()
    try:
        orgs = cursor.execute(f"SELECT * FROM organizacion").fetchall()
        for org in orgs:
            rows.append({"id": org[0], "organization": org[1], "zone_id": org[2], "polygon": org[3]})
        return {"data": rows}
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"error detected: {err}")


@app.get("/org/{id}")
def read_orgs(id):
    connection = sqlite3.connect("newdata.db")
    cursor = connection.cursor()
    try:
        org, = cursor.execute(f"SELECT id, nombre, id_zona, coordenadas FROM organizacion WHERE id == {id}").fetchall()
        final_coords = utils.replace_chars(org[3])
        return {"organization": org[1], "zone_id": org[2], "polygon": final_coords}
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"error detected: {err}")
