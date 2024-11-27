def usuari_schema(usuari) -> dict:
    return {
        "idUsuari": usuari.idUsuari,
        "nomUsuari": usuari.nomUsuari,
        "cognomUsuari": usuari.cognomUsuari,
        "correu": usuari.correu,
        "contrassenya": usuari.contrassenya,
        "tipus": usuari.tipus,
        # "estat": assistencia_schema.estat
        "estat": usuari.estat
    }

def assistencia_schema(assistencia) -> dict:
    return {
        # "idUsuari": usuari_schema.idUsuari,
        "idUsuari": assistencia.idUsuari,
        "estat": assistencia.estat,
        "hEntrada": assistencia.horaEntrada,
        "hSortida": assistencia.horaSortida,
        "dia": assistencia.dia
    }

def grup_schema(grup) -> dict:
    return {
        "idGrup": grup.idGrup,
        "nomGrup": grup.nomGrup,
        "nomClasse": grup.nomClasse
    }

def classe_schema(classe) -> dict:
    return {
        "idClasse": classe.idClasse,
        "nomClasse": classe.nomClasse,
        # "nomGrup": grup_schema.nomGrup
        "nomGrup": classe.nomGrup
    }

def modul_schema(modul) -> dict:
    return {
        "idModul": modul.idModul,
        "nomModul": modul.nomModul,
        # "idClasse": classe_schema.idClasse
        "idClasse": modul.idClasse
    }
def usuaris_schema(usuaris) -> dict:
    return [usuari_schema(usuari) for usuari in usuaris]

def assistencies_schema(assistencies) -> dict:
    return [assistencia_schema(assistencia) for assistencia in assistencies]

def grups_schema(grups) -> dict:
    return [grup_schema(grup) for grup in grups]

def classes_schema(classes) -> dict:
    return [classe_schema(classe) for classe in classes]

def moduls_schema(moduls) -> dict:
    return [modul_schema(modul) for modul in moduls]