import streamlit as st
import pandas as pd
import datetime
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Juego Delaunay", layout="wide")

# ---------------- ESTADO ----------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "codigos" not in st.session_state:
    st.session_state.codigos = []

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "respuestas" not in st.session_state:
    st.session_state.respuestas = []

if "inicio" not in st.session_state:
    st.session_state.inicio = datetime.datetime.now()

# ---------------- ESTILO VISUAL ----------------
def estilo():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .stButton>button {
        background-color: #E63946;
        color: white;
        border-radius: 12px;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- IA INTERNA ----------------
def ayuda_ia(pregunta, correcta):
    st.markdown("### 🤖 Ayuda inteligente")

    if pregunta == "patron":
        st.info("Observa la secuencia: alterna colores rojo y azul.")
    elif pregunta == "radio":
        st.info("El radio siempre va del centro al borde.")
    elif pregunta == "error":
        st.warning("Parece que estás fallando varias veces. Prueba a fijarte en el patrón o pedir ayuda.")

# ---------------- GUARDAR DATOS ----------------
def guardar(nombre):
    fin = datetime.datetime.now()

    df = pd.DataFrame([{
        "nombre": nombre,
        "puntos": st.session_state.puntos,
        "duracion": (fin - st.session_state.inicio).seconds,
        "errores": sum([1 for r in st.session_state.respuestas if not r])
    }])

    os.makedirs("data", exist_ok=True)
    archivo = "data/resultados.csv"

    if os.path.exists(archivo):
        df.to_csv(archivo, mode="a", index=False, header=False)
    else:
        df.to_csv(archivo, index=False)

# ---------------- DASHBOARD DOCENTE ----------------
def dashboard():
    st.title("📊 Dashboard docente")

    try:
        df = pd.read_csv("data/resultados.csv")

        st.subheader("Resultados generales")
        st.dataframe(df)

        st.subheader("Media de puntuación")
        st.write(df["puntos"].mean())

        st.subheader("Errores medios")
        st.write(df["errores"].mean())

        st.bar_chart(df["puntos"])

    except:
        st.info("No hay datos aún")

# ---------------- PANTALLAS ----------------

def inicio():
    estilo()
    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 Objetivo

    Completa retos para conseguir números secretos.
    
    Al final tendrás que introducir el código en orden.
    """)

    nombre = st.text_input("Tu nombre")

    if st.button("🚀 Jugar"):
        st.session_state.nombre = nombre
        ir("mapa")

    if st.button("📊 Ver dashboard"):
        ir("dashboard")

# ---------------- MAPA ----------------

def mapa():
    estilo()
    st.title("🗺️ Mapa del juego")
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    if st.button("🔵 Círculos"): ir("r1")
    if st.button("🔁 Patrones"): ir("r2")
    if st.button("🔐 Final"): ir("final")

# ---------------- RETO 1 ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    r = st.radio("¿Qué es el radio?", [
        "Centro-borde", "Diámetro", "Circunferencia"
    ])

    if st.button("Responder"):
        correcta = r == "Centro-borde"
        st.session_state.respuestas.append(correcta)

        if correcta:
            st.success("Correcto +10")
            st.session_state.puntos += 10
            st.session_state.codigos.append("3")
        else:
            st.error("Incorrecto")
            ayuda_ia("radio", False)

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- RETO 2 (ARREGLADO) ----------------

def r2():
    estilo()
    st.header("🔁 Patrones visuales")

    st.markdown("### Observa el patrón:")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Red_square.svg/120px-Red_square.svg.png")
    col2.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Blue_square.svg/120px-Blue_square.svg.png")
    col3.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Red_square.svg/120px-Red_square.svg.png")
    col4.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Blue_square.svg/120px-Blue_square.svg.png")

    st.write("¿Cuál debería ser la siguiente figura?")

    r = st.radio("Selecciona:", ["Rojo", "Azul", "Amarillo"])

    if st.button("Responder"):
        correcta = r == "Rojo"
        st.session_state.respuestas.append(correcta)

        if correcta:
            st.success("Correcto +10")
            st.session_state.puntos += 10
            st.session_state.codigos.append("7")
        else:
            st.error("Incorrecto")
            ayuda_ia("patron", False)

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Introduce el código")

    codigo = st.text_input("Código")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)

        if codigo == correcto:
            ir("ganar")
        else:
            ir("perder")

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- GANAR / PERDER ----------------

def ganar():
    estilo()
    st.title("🎉 HAS GANADO")
    st.balloons()

    guardar(st.session_state.nombre)

    if st.button("📊 Ver resultados"):
        ir("dashboard")

def perder():
    estilo()
    st.title("❌ Intenta de nuevo")

    if st.button("Volver"):
        ir("mapa")

# ---------------- ROUTER ----------------

pantallas = {
    "inicio": inicio,
    "mapa": mapa,
    "r1": r1,
    "r2": r2,
    "final": final,
    "ganar": ganar,
    "perder": perder,
    "dashboard": dashboard
}

pantallas[st.session_state.pantalla]()
