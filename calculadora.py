import json
from pathlib import Path

RUTA_DATOS = Path(__file__).parent / "datos" / "tareas.json"
HORAS_JORNADA = 8
HORAS_SEMANA_LABORAL = 40


def cargar_datos():
    with open(RUTA_DATOS, encoding="utf-8") as archivo:
        return json.load(archivo)


def calcular_tiempo_liberado(tarea, horas_semana, datos):
    horas_liberadas = horas_semana * datos["semanas_laborables"] * tarea["automatizable"]

    return {
        "tarea": tarea["nombre"],
        "horas": round(horas_liberadas),
        "jornadas": round(horas_liberadas / HORAS_JORNADA),
        "semanas": round(horas_liberadas / HORAS_SEMANA_LABORAL, 1),
    }


def calcular_total(sector, selecciones, datos):
    resultados = []
    for tarea in sector["tareas"]:
        if tarea["nombre"] in selecciones:
            horas_semana = selecciones[tarea["nombre"]]
            resultados.append(calcular_tiempo_liberado(tarea, horas_semana, datos))

    resultados.sort(key=lambda r: r["horas"], reverse=True)

    total_horas = sum(r["horas"] for r in resultados)

    return {
        "tareas": resultados,
        "total_horas": total_horas,
        "total_jornadas": round(total_horas / HORAS_JORNADA),
        "total_semanas": round(total_horas / HORAS_SEMANA_LABORAL, 1),
        "horas_semana": round(total_horas / datos["semanas_laborables"], 1),
        "horas_mes": round(total_horas / 12),
    }


if __name__ == "__main__":
    datos = cargar_datos()
    logistica = datos["sectores"][1]

    selecciones = {
        "Pasar pedidos y órdenes de transporte al sistema": 8,
        "Crear y revisar albaranes": 15,
    }

    total = calcular_total(logistica, selecciones, datos)
    for r in total["tareas"]:
        print(r)
    print("TOTAL:", total["total_horas"], "horas")