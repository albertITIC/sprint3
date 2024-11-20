from fastapi import Query
from client import db_client
from typing import Optional

def fetch_all_usuaris():
    try:
        conn = db_client()
        cur = conn.cursor()
    except Exception as e:
        return {"status": -2, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return assistencia_list