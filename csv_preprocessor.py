import json
import numpy as np
import pandas as pd

def create():
    # Leer el archivo CSV
    df = pd.read_csv('materias.csv')

    # Asegurarse de que todas las columnas de días de la semana estén presentes
    for dia in ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]:
        if dia not in df.columns:
            df[dia] = np.nan

    # Crear una lista vacía para almacenar las materias
    materias = []

    # Recorrer las filas del dataframe
    for _, row in df.iterrows():
        # Crear un diccionario para almacenar la información de la materia
        materia = {
            "nombre": row['Asignatura'],
            "grupo": row['Grupo'],
            "profesor": row['Profesor'],
            "fijada": row['fijada'],  # Añadido el atributo fijada
            "horario": []
        }

        # Añadir los horarios para cada día de la semana
        for dia, abreviatura in zip(["Lun", "Mar", "Mie", "Jue", "Vie", "Sab"], ["L", "M", "X", "J", "V", "S"]):
            if pd.notna(row[dia]) and isinstance(row[dia], str) and '-' in row[dia]:
                horario = {
                    "dia": abreviatura,
                    "hora_inicio": row[dia].split('-')[0].strip(),
                    "hora_fin": row[dia].split('-')[1].strip()
                }
                materia["horario"].append(horario)

        materias.append(materia)

    # Crear un diccionario para el archivo JSON
    datos = {"materias": materias}

    # Escribir el archivo JSON
    with open('materias.json', 'w') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


# Llamar a la función para crear el archivo JSON
create()
