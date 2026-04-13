import json

def cargar_ejercicios(ruta="Ejercicios.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["Ejercicios"]