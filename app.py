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

if "inicio" not in st.session_state:
    st.session_state.inicio = datetime.datetime.now()

# ---------------- ESTILO ----------------
def estilo():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #111111, #1D4ED8);
        color: white;
    }
    .stButton>button {
        background-color: #E63946;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- GUARDAR RESULTADOS ----------------
def guardar(nombre):
    fin = datetime.datetime.now()

    df = pd.DataFrame([{
        "nombre": nombre,
        "puntos": st.session_state.puntos,
        "codigo": "".join(st.session_state.codigos),
        "duracion": (fin - st.session_state.inicio).seconds
    }])

    os.makedirs("data", exist_ok=True)

    archivo = "data/resultados.csv"

    if os.path.exists(archivo):
        df.to_csv(archivo, mode="a", index=False, header=False)
    else:
        df.to_csv(archivo, index=False)

# ---------------- LEADERBOARD ----------------
def ranking():
    st.subheader("🏆 Ranking")

    try:
        df = pd.read_csv("data/resultados.csv")
        df = df.sort_values(by="puntos", ascending=False)
        st.dataframe(df.head(10))
    except:
        st.info("Aún no hay datos")

# ---------------- PANTALLAS ----------------

def inicio():
    estilo()
    st.title("🎨 El código secreto del color")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    nombre = st.text_input("Introduce tu nombre")

    if st.button("🚀 Comenzar"):
        st.session_state.nombre = nombre
        ir("mapa")

    ranking()

# ---------------- MAPA ----------------
def mapa():
    estilo()
    st.title("🗺️ Mapa del juego")
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    col1, col2 = st.columns(2)

    if col1.button("🔵 Círculos"):
        ir("r1")

    if col2.button("🔁 Patrones"):
        ir("r2")

    if col1.button("🔺 Geometría"):
        ir("r3")

    if col2.button("🌈 Color"):
        ir("r4")

    if st.button("🔐 Final"):
        ir("final")

# ---------------- RETOS ----------------

def r1():
    estilo()
    st.header("🔵 Reto 1: Círculos")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    r = st.radio("¿Qué es el radio?", [
        "Toda la línea",
        "Del centro al borde",
        "El diámetro"
    ])

    if st.button("Responder"):
        if r == "Del centro al borde":
            st.success("Correcto +10 puntos")
            st.session_state.puntos += 10
            if "3" not in st.session_state.codigos:
                st.session_state.codigos.append("3")
        else:
            st.error("Incorrecto -2 puntos")
            st.session_state.puntos -= 2

    if st.button("⬅ Volver"):
        ir("mapa")

def r2():
    estilo()
    st.header("🔁 Reto 2: Patrones")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Pattern_examples.svg")

    r = st.radio("🔴 🔵 🔴 🔵 🔴 ?", ["🔴", "🔵", "🟡"])

    if st.button("Responder"):
        if r == "🔵":
            st.success("Correcto +10 puntos")
            st.session_state.puntos += 10
            if "7" not in st.session_state.codigos:
                st.session_state.codigos.append("7")
        else:
            st.error("Incorrecto -2 puntos")
            st.session_state.puntos -= 2

    if st.button("⬅ Volver"):
        ir("mapa")

def r3():
    estilo()
    st.header("🔺 Reto 3: Geometría")

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    r = st.radio("¿Qué formas aparecen?", [
        "Círculos",
        "Triángulos",
        "Ninguna"
    ])

    if st.button("Responder"):
        if r == "Triángulos":
            st.success("Correcto +10 puntos")
            st.session_state.puntos += 10
            if "2" not in st.session_state.codigos:
                st.session_state.codigos.append("2")
        else:
            st.error("Incorrecto -2 puntos")
            st.session_state.puntos -= 2

    if st.button("⬅ Volver"):
        ir("mapa")

def r4():
    estilo()
    st.header("🌈 Reto 4: Color")

    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/Color_wheel.svg")

    r = st.radio("¿Mayor contraste?", [
        "Azul + azul claro",
        "Rojo + verde",
        "Amarillo + naranja"
    ])

    if st.button("Responder"):
        if r == "Rojo + verde":
            st.success("Correcto +10 puntos")
            st.session_state.puntos += 10
            if "5" not in st.session_state.codigos:
                st.session_state.codigos.append("5")
        else:
            st.error("Incorrecto -2 puntos")
            st.session_state.puntos -= 2

    if st.button("⬅ Volver"):
        ir("mapa")

# ---------------- FINAL MEJORADO ----------------

def final():
    estilo()
    st.header("🔐 Desbloquea la obra final")

    st.write("Has conseguido piezas del código en cada reto.")

    st.write("📌 Ordena los números en el orden de los retos:")

    st.write("🔵 Círculos → 🔁 Patrones → 🔺 Geometría → 🌈 Color")

    codigo = st.text_input("Introduce el código final")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)

        if codigo == correcto:
            st.success("🎉 ¡HAS GANADO!")
            st.balloons()
            guardar(st.session_state.nombre)
        else:
            st.error("Código incorrecto")

    if st.button("⬅ Volver"):
        ir("mapa")

# ---------------- ROUTER ----------------

pantallas = {
    "inicio": inicio,
    "mapa": mapa,
    "r1": r1,
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "final": final
}

pantallas[st.session_state.pantalla]()
