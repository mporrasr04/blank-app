import json

def cargar_ejercicios(ruta="Ejercicios.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["Ejercicios"]

def filtrar_ejercicios(ejercicios, nivel="1", dificultad="1"):
    return [
        ejercicio for ejercicio in ejercicios
        if str(ejercicio.get("Nivel")) == str(nivel)
        and str(ejercicio.get("Dificultad")) == str(dificultad)
    ]