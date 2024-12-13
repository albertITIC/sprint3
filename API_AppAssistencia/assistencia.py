def usuari_schema(usuari) -> dict:
    return {
        "idUsuari": usuari[0],
        "nomUsuari": usuari[1],
        "cognomUsuari": usuari[2],
        "correu": usuari[3],
        "contrassenya": usuari[4],
        "tipus": usuari[5],
        "estat": usuari[6],
        "nuid": usuari[7]
    }

def assistencia_schema(assistencia) -> dict:
    return {
        "idAssistencia": assistencia[0],
        "idUsuari": assistencia[1],
        "estat": assistencia[2],
        "hEntrada": assistencia[3],
        "hSortida": assistencia[4],
        "dia": assistencia[5]
    }

def grup_schema(grup) -> dict:
    return {
        "idGrup": grup[0],
        "nomGrup": grup[1],
        "nomClasse": grup[2]
    }

def classe_schema(classe) -> dict:
    return {
        "idClasse": classe[0],
        "nomClasse": classe[1],
        "nomGrup": classe[2]
    }

def modul_schema(modul) -> dict:
    return {
        "idModul": modul[0],
        "nomModul": modul[1],
        "nomClasse": modul[2]
    }

def usuaris_schema(usuaris) -> list[dict]:
    return [usuari_schema(usuari) for usuari in usuaris]

def assistencies_schema(assistencies) -> list[dict]:
    return [assistencia_schema(assistencia) for assistencia in assistencies]

def grups_schema(grups) -> dict:
    return [grup_schema(grup) for grup in grups]

def classes_schema(classes) -> dict:
    return [classe_schema(classe) for classe in classes]

def moduls_schema(moduls) -> dict:
    return [modul_schema(modul) for modul in moduls]