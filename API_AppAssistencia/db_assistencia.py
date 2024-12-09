from fastapi import Query
from client import db_client
from typing import Optional

def fetch_all_usuaris():
    try:
        conn = db_client()
        cur = conn.cursor()
        
        query = "SELECT * FROM usuari"

        cur.execute(query)
        usuaris = cur.fetchall()

        usuaris_list = []
        for usuari in usuaris:
            usuaris_list.append({
                "idUsuari": usuari[0],
                "nomUsuari": usuari[1],
                "cognomUsuari": usuari[2],
                "correu": usuari[3],
                "contrassenya": usuari[4],
                "tipus": usuari[5],
                "estat": usuari[6],
                "NUID": usuari[7]
            })
        
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return usuaris_list

def fetch_usuari_by_id(id_usuari: int):
    try:
        conn = db_client()
        cur = conn.cursor()
        
        query = "SELECT * FROM usuari WHERE idUsuari = %s"
        cur.execute(query, (id_usuari,))
        usuari = cur.fetchone()

        if usuari is None:
            return {"status": -1, "message": "Usuari no trobat" }

        usuari_list = {
            "idUsuari": usuari[0],
            "nomUsuari": usuari[1],
            "cognomUsuari": usuari[2],
            "correu": usuari[3],
            "contrassenya": usuari[4],
            "tipus": usuari[5],
            "estat": usuari[6],
            "NUID": usuari[7],
            }
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return usuari_list