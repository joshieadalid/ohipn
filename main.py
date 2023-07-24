import json
from datetime import datetime
from itertools import combinations
from operator import itemgetter

import networkx as nx


def cargar_datos():
    with open('horarios.json', 'r') as f:
        data = json.load(f)
    return data['materias']


def se_traslapan(clase1, clase2):
    if clase1['nombre'] == clase2['nombre']:
        return True
    for horario1 in clase1['horario']:
        for horario2 in clase2['horario']:
            if horario1['dia'] == horario2['dia']:
                inicio1 = datetime.strptime(horario1['hora_inicio'], "%H:%M")
                fin1 = datetime.strptime(horario1['hora_fin'], "%H:%M")
                inicio2 = datetime.strptime(horario2['hora_inicio'], "%H:%M")
                fin2 = datetime.strptime(horario2['hora_fin'], "%H:%M")
                if inicio1 < fin2 and inicio2 < fin1:
                    return True
    return False


def imprimir_horario(horario):
    for clase in horario:
        print(f"{clase['grupo']}: {clase['nombre']}")
        print(
            f"\tProfesor: {clase['profesor']}")  # for sesion in clase["horario"]:  #   print(f"  {sesion['dia']} {sesion['hora_inicio']} - {sesion['hora_fin']}")
    print()


# def imprimir_horario(horario):
#     dias = ["L", "M", "X", "J", "V"]
#     horario_por_dia = {dia: [] for dia in dias}
#
#     for clase in horario:
#         for sesion in clase["horario"]:
#             dia = sesion["dia"]
#             hora_inicio = sesion["hora_inicio"]
#             hora_fin = sesion["hora_fin"]
#             horario_por_dia[dia].append((hora_inicio, hora_fin, clase["grupo"], clase["nombre"], clase["profesor"]))
#
#     for dia in dias:
#         print(f"{dia}:")
#         horario_por_dia[dia].sort(key=lambda x: datetime.strptime(x[0], "%H:%M"))  # Ordenar por hora de inicio
#         for sesion in horario_por_dia[dia]:
#             hora_inicio, hora_fin, grupo, nombre, profesor = sesion
#             print(f"\t{hora_inicio} - {hora_fin}: Grupo {grupo} - {nombre} (Profesor: {profesor})")
#         print()

def calcular_fragmentacion(horario):
    dias = ["L", "M", "X", "J", "V"]

    fragmentacion = 0

    for dia in dias:
        clases_dia = [sesion for clase in horario for sesion in clase["horario"] if sesion["dia"] == dia]
        clases_dia.sort(key=lambda x: datetime.strptime(x['hora_inicio'], "%H:%M"))

        if clases_dia:
            inicio_dia = datetime.strptime(clases_dia[0]['hora_inicio'], "%H:%M").hour + datetime.strptime(
                clases_dia[0]['hora_inicio'], "%H:%M").minute / 60
            fin_dia = datetime.strptime(clases_dia[-1]['hora_fin'], "%H:%M").hour + datetime.strptime(
                clases_dia[-1]['hora_fin'], "%H:%M").minute / 60

            tiempo_clases = sum(
                datetime.strptime(sesion['hora_fin'], "%H:%M").hour + datetime.strptime(sesion['hora_fin'],
                                                                                        "%H:%M").minute / 60 - (
                        datetime.strptime(sesion['hora_inicio'], "%H:%M").hour + datetime.strptime(
                    sesion['hora_inicio'], "%H:%M").minute / 60) for sesion in clases_dia)

            tiempo_libre = (fin_dia - inicio_dia) - tiempo_clases
            fragmentacion += tiempo_libre  # sumar el tiempo libre del día a la fragmentación total

    return fragmentacion


def calcular_materias_diferentes(horario):
    materias_unicas = set()

    for clase in horario:
        materia_nombre = clase["nombre"]
        materias_unicas.add(materia_nombre)

    return len(materias_unicas)


def main():
    clases = cargar_datos()

    g = nx.Graph()
    for clase in clases:
        g.add_node(json.dumps(clase))

    for clase1, clase2 in combinations(clases, 2):
        if not se_traslapan(clase1, clase2):
            g.add_edge(json.dumps(clase1), json.dumps(clase2))

    cliques = list(nx.find_cliques(g))
    horarios = [[json.loads(clase) for clase in clique] for clique in cliques]

    horarios_fragmentacion_materias = []
    for i, horario in enumerate(horarios):
        horarios_fragmentacion_materias.append({'horario': horario, 'fragmentacion': calcular_fragmentacion(horario),
                                                'materias': calcular_materias_diferentes(horario)})

    horarios_ordenados = sorted(horarios_fragmentacion_materias, key=lambda x: (-x['materias'], x['fragmentacion']))
    horarios_filtrados = [horario for horario in horarios_ordenados if horario['materias'] <= 7]
    # Limitar la impresión a 25 horarios
    for i, horario in enumerate(horarios_filtrados[:100]):
        print(f'Horario {i + 1}:')
        imprimir_horario(horario['horario'])

        print(f'Fragmentación: {horario["fragmentacion"]}')
        print(f'Materias: {horario["materias"]}')
        print()



if __name__ == '__main__':
    main()
