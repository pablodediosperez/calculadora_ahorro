import streamlit as st
from calculadora import cargar_datos, calcular_total
from guardar import guardar_envio

st.set_page_config(page_title="Calculadora de tiempo liberado", page_icon="⏱️")

TEXTO_EXPLICACION = """
**¿Qué significa esto para tu empresa?**

Ese tiempo es el que tu equipo dedica hoy a tareas repetitivas que una herramienta puede hacer por él. No se trata de prescindir de nadie, sino de que tu gente pueda dedicarse a lo que de verdad aporta valor: atender mejor a los clientes, hacer crecer el negocio y trabajar con menos carga.

Este cálculo es una primera estimación. Cada empresa trabaja de forma distinta, y el tiempo real que puedes liberar depende de tus procesos, tu equipo y las herramientas que ya usáis.

**Te ayudamos a descubrirlo.** Analizamos tu caso, te decimos por dónde empezar y lo ponemos en marcha contigo y con tu equipo.
"""
datos = cargar_datos()

st.title("Calculadora de tiempo liberado")
st.write("Descubre cuánto tiempo podría ganar tu equipo automatizando tareas repetitivas.")

nombres_sectores = [sector["nombre"] for sector in datos["sectores"]]
nombre_elegido = st.selectbox("¿A qué sector pertenece tu empresa?", nombres_sectores)

for s in datos["sectores"]:
    if s["nombre"] == nombre_elegido:
        sector = s

st.subheader("¿Qué tareas hace tu equipo?")
st.write("Marca las que hacéis e indica cuántas horas a la semana les dedica el equipo. Si no lo sabes, deja el valor que aparece: es una estimación media.")

selecciones = {}

selecciones = {}
for tarea in sector["tareas"]:
    marcada = st.checkbox(tarea["nombre"])
    if marcada:
        horas = st.slider(
            "Horas a la semana que le dedica tu equipo",
            min_value=0.0,
            max_value=40.0,
            value=float(tarea["horas_semana"]["medio"]),
            step=0.5,
            key=tarea["nombre"],
        )
        selecciones[tarea["nombre"]] = horas

if selecciones:
    total = calcular_total(sector, selecciones, datos)

    st.subheader("Tiempo que podrías liberar al año")
    caja = st.container(border=True)
    col1, col2, col3 = caja.columns(3)
    col1.metric("Horas", total["total_horas"])
    col2.metric("Jornadas", total["total_jornadas"])
    col3.metric("Semanas", total["total_semanas"])

    st.subheader("En el día a día")
    caja2 = st.container(border=True)
    c1, c2 = caja2.columns(2)
    c1.metric("Horas a la semana", total["horas_semana"])
    c2.metric("Horas al mes", total["horas_mes"])

    st.subheader("Por dónde empezar")
    for i, r in enumerate(total["tareas"], start=1):
        st.write(f"{i}. **{r['tarea']}**: {r['horas']} horas al año ({r['semanas']} semanas)")

    st.markdown(TEXTO_EXPLICACION)
    st.divider()
    st.subheader("¿Quieres saber cuánto tiempo podrías liberar de verdad?")
    st.write("Déjanos tus datos y te contactamos para estudiar tu caso.")

    with st.form("contacto"):
        nombre = st.text_input("Nombre")
        empresa = st.text_input("Empresa")
        email = st.text_input("Correo electrónico")
        acepto = st.checkbox("Acepto que se guarden mis datos para que me contactéis.")
        enviado = st.form_submit_button("Enviar")

    if enviado:
        if not (nombre and empresa and email):
            st.error("Rellena tu nombre, empresa y correo.")
        elif not acepto:
            st.error("Necesitamos tu consentimiento para guardar tus datos.")
        else:
            guardar_envio(nombre, empresa, email, sector["nombre"], selecciones, total["total_horas"])
            st.success("¡Gracias! Hemos recibido tus datos. Nos pondremos en contacto contigo en los próximos días.")
else:
    st.info("Marca al menos una tarea para ver el resultado.")