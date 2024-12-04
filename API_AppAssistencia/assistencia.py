def usuari_schema(usuari) -> dict:
    return {
        "nuid": usuari[0],
        "idUsuari": usuari[1],
        "nomUsuari": usuari[2],
        "cognomUsuari": usuari[3],
        "correu": usuari[4],
        "contrassenya": usuari[5],
        "tipus": usuari[6],
        "estat": usuari[7]
    }

def assistencia_schema(assistencia) -> dict:
    return {
        "idUsuari": assistencia[0],
        "estat": assistencia[1],
        "hEntrada": assistencia[2],
        "hSortida": assistencia[3],
        "dia": assistencia[4]
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
        "idClasse": modul[2]
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