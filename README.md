# ⏱️ Calculadora de tiempo liberado

Herramienta web que estima cuánto tiempo podría liberar una empresa automatizando sus tareas repetitivas: pasar pedidos al sistema, revisar albaranes, introducir facturas o preparar informes.

El enfoque no es recortar plantilla, sino **devolver tiempo al equipo** para que lo dedique a tareas de más valor.

![Captura de la calculadora](docs/captura.png)

---

## ¿Qué hace?

1. El usuario elige el **sector** de su empresa.
2. Marca las **tareas repetitivas** que hace su equipo.
3. Indica con una barra cuántas **horas a la semana** les dedica. Si no lo sabe, se usa una estimación media.
4. La herramienta muestra:
   - El **tiempo liberable al año**, en horas, jornadas y semanas de trabajo.
   - El **equivalente semanal y mensual**.
   - Las **tareas ordenadas** de mayor a menor impacto, para saber por dónde empezar.
5. Si quiere, deja sus datos de contacto para un diagnóstico personalizado. Los datos solo se guardan con su consentimiento.

**Sectores incluidos:** industria y metal, logística y transporte, construcción e ingeniería, y asesorías y despachos. Cada uno tiene 6 tareas típicas.

---

## Cómo se calcula

Para cada tarea marcada:

```
horas liberadas al año = horas semanales × 46 semanas laborables × % automatizable
```

Después se suman todas las tareas y el total se expresa en jornadas de 8 horas y semanas de 40 horas.

**Ejemplo:** 8 horas a la semana × 46 semanas × 50 % automatizable = 184 horas al año.

### Supuestos y fuentes

- **Horas semanales por defecto:** estimación propia del tiempo medio que se dedica a cada tarea. El usuario puede ajustarlas.
- **Porcentaje automatizable:** estimación prudente por tipo de tarea, del 20 % al 60 %. Se sitúa por debajo del potencial técnico que señala el estudio de McKinsey Global Institute *A Future That Works* (2017), que estima alrededor de un 64–69 % para las actividades de recogida y procesamiento de datos. Se ha elegido un valor más bajo a propósito, para reflejar lo que suele conseguirse en la práctica.
- **46 semanas laborables**, descontando vacaciones y festivos.

Los resultados son **orientativos**: cada empresa trabaja de forma distinta.

---

## Estructura del proyecto

```
calculadora_ahorro/
├── app.py              # Interfaz web (Streamlit)
├── calculadora.py      # Lógica de cálculo
├── guardar.py          # Guardado de los contactos en CSV
├── datos/
│   └── tareas.json     # Sectores, tareas, horas y porcentajes
├── .streamlit/
│   └── config.toml     # Tema visual
├── requirements.txt    # Dependencias
└── README.md
```

La lógica está separada en capas:
- **Datos** (`tareas.json`): se pueden cambiar las tareas o los porcentajes sin tocar el código.
- **Cálculo** (`calculadora.py`): funciones independientes de la interfaz, que se pueden probar por separado.
- **Interfaz** (`app.py`): solo muestra los datos y recoge lo que introduce el usuario.

---

## Instalación y uso

Requisitos: Python 3.10 o superior.

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/calculadora-ahorro.git
cd calculadora-ahorro

# 2. Crear y activar un entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac / Linux

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Lanzar la aplicación
streamlit run app.py
```

Se abrirá en el navegador, en `http://localhost:8501`.

Para probar solo la lógica de cálculo, sin la interfaz:
```bash
python calculadora.py
```

---

## Privacidad

- Los datos de contacto solo se guardan si el usuario marca la casilla de consentimiento.
- Se guardan en `datos/envios.csv`, que está excluido del repositorio mediante `.gitignore`.
- Esta versión es una demostración. Para usarla en producción haría falta un almacenamiento seguro y una política de privacidad conforme al RGPD.

---

## Próximos pasos

- [ ] Publicar la aplicación en la web.
- [ ] Guardar los contactos en una base de datos segura en lugar de un CSV.
- [ ] Añadir más sectores y tareas.
- [ ] Afinar las estimaciones con datos de proyectos reales.
- [ ] Generar un informe descargable en PDF.

---

## Tecnologías

- **Python**
- **Streamlit**, para la interfaz web.
- **JSON** y **CSV**, para los datos.

---

## Autor

**Pablo de Dios Pérez**, analytics y data science, especializado en IA y automatización de procesos.

[LinkedIn](https://www.linkedin.com/in/TU_PERFIL) · [GitHub](https://github.com/TU_USUARIO)
