import csv
from datetime import datetime
from pathlib import Path

RUTA_ENVIOS = Path(__file__).parent / "datos" / "envios.csv"
COLUMNAS = ["fecha", "nombre", "empresa", "email", "sector", "tareas", "total_horas"]


def guardar_envio(nombre, empresa, email, sector, selecciones, total_horas):
    archivo_nuevo = not RUTA_ENVIOS.exists()

    with open(RUTA_ENVIOS, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if archivo_nuevo:
            escritor.writerow(COLUMNAS)

        tareas_texto = "; ".join(f"{t} ({v} h/semana)" for t, v in selecciones.items())
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        escritor.writerow([fecha, nombre, empresa, email, sector, tareas_texto, total_horas])