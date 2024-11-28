from client import db_client
from mysql.connector import Error

def fetch_usuari_by_id(id):
    try:
        # Crear conexió a la base de dades
        conn = db_client()
        cur = conn.cursor(dictionary=True)  # Retorna los resultats com diccionaris

        # Consulta per obtenir l'usuari per ID
        query = "SELECT * FROM usuaris WHERE idUsuari = %s"
        cur.execute(query, (id,)) 

        # Obtenim el resultat
        result = cur.fetchone()
        return result

    except Error as e:
        print(f"Error en la base de dades: {e}")
        return None

    finally:
        if conn.is_connected():
            conn.close()
