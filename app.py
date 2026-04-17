import streamlit as st
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Juego Delaunay", layout="wide")

# ---------------- ESTADO ----------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "codigos" not in st.session_state:
    st.session_state.codigos = []

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

# ---------------- ESTILO ----------------
def estilo():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1D4ED8, #E63946, #FFD60A);
        color: white;
        font-family: Arial;
    }
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- NAV (CON KEYS) ----------------
def nav(id):
    col1, col2 = st.columns(2)

    if col1.button("🗺️ Mapa", key=f"mapa_{id}"):
        ir("mapa")

    if col2.button("🏠 Inicio", key=f"inicio_{id}"):
        ir("inicio")

# ---------------- EVALUAR ----------------
def evaluar(correcta, codigo, id):
    if correcta:
        st.success("✔ Correcto. Anota el número.")
        st.session_state.puntos += 10
        st.session_state.codigos.append(codigo)
    else:
        st.error("❌ Incorrecto")
        st.session_state.puntos -= 2

    nav(id)

# ---------------- INICIO ----------------
def inicio():
    estilo()

    st.title("🎨 El código secreto del color")

    st.markdown("""
    ## 🎯 Cómo jugar

    Vas a resolver varios retos relacionados con:
    - Geometría
    - Color
    - Arte de Sonia Delaunay

    ### 🧩 Importante

    - Cada respuesta tiene un número
    - Debes ANOTAR ese número
    - No se mostrará en pantalla

    ### 🔐 Código final

    - Al final tendrás varios números
    - Debes escribirlos en orden
    - Ejemplo: 3725

    ### ⭐ Puntuación

    ✔ +10 acierto  
    ❌ -2 error
    """)

    st.session_state.nombre = st.text_input("Nombre")
    st.session_state.nivel = st.radio("Nivel", ["Fácil","Medio","Difícil"])

    if st.button("🚀 Empezar", key="start"):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    estilo()

    st.header("🗺️ Mapa")

    if st.button("1 Círculos", key="r1_btn"): ir("r1")
    if st.button("2 Patrones", key="r2_btn"): ir("r2")
    if st.button("3 Geometría", key="r3_btn"): ir("r3")
    if st.button("4 Color", key="r4_btn"): ir("r4")
    if st.button("5 Ritmo", key="r5_btn"): ir("r5")
    if st.button("6 Simetría", key="r6_btn"): ir("r6")
    if st.button("7 Composición", key="r7_btn"): ir("r7")
    if st.button("Código final", key="final_btn"): ir("final")

# ---------------- RETOS ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    r = st.radio("¿Qué es el radio?", [
        "1 Circunferencia",
        "2 Diámetro",
        "3 Centro al borde"
    ], key="r1_radio")

    if st.button("Responder", key="r1_responder"):
        evaluar("3" in r, "3", "r1")

    nav("r1")

# ---------------- PATRÓN CORREGIDO ----------------

def r2():
    estilo()
    st.header("🔁 Patrones")

    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("¿Qué sigue?", [
        "1 Azul",
        "2 Rojo",
        "3 Amarillo"
    ], key="r2_radio")

    if st.button("Responder", key="r2_responder"):
        evaluar("1" in r, "7", "r2")  # AZUL CORRECTO

    nav("r2")

# ---------------- RESTO ----------------

def r3():
    estilo()
    st.header("🔺 Geometría")

    r = st.radio("¿Qué figura tiene 4 lados iguales?", [
        "1 Triángulo",
        "2 Cuadrado",
        "3 Círculo"
    ], key="r3_radio")

    if st.button("Responder", key="r3_responder"):
        evaluar("2" in r, "2", "r3")

    nav("r3")

def r4():
    estilo()
    st.header("🌈 Color")

    r = st.radio("Colores primarios", [
        "1 Rojo azul amarillo",
        "2 Verde azul rojo",
        "3 Blanco negro"
    ], key="r4_radio")

    if st.button("Responder", key="r4_responder"):
        evaluar("1" in r, "5", "r4")

    nav("r4")

def r5():
    estilo()
    st.header("🧠 Ritmo")

    r = st.radio("¿Qué crea ritmo?", [
        "1 Repetición",
        "2 Un color",
        "3 Texto"
    ], key="r5_radio")

    if st.button("Responder", key="r5_responder"):
        evaluar("1" in r, "8", "r5")

    nav("r5")

def r6():
    estilo()
    st.header("📐 Simetría")

    r = st.radio("¿Qué es simetría?", [
        "1 Partes iguales",
        "2 Caos",
        "3 Aleatorio"
    ], key="r6_radio")

    if st.button("Responder", key="r6_responder"):
        evaluar("1" in r, "6", "r6")

    nav("r6")

def r7():
    estilo()
    st.header("🎨 Composición")

    r = st.radio("¿Qué mejora una obra?", [
        "1 Organización",
        "2 Caos",
        "3 Nada"
    ], key="r7_radio")

    if st.button("Responder", key="r7_responder"):
        evaluar("1" in r, "4", "r7")

    nav("r7")

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Código final")

    c = st.text_input("Introduce el código", key="codigo_input")

    if st.button("Comprobar", key="check"):
        if c == "".join(st.session_state.codigos):
            ir("ganar")
        else:
            ir("perder")

    nav("final")

def ganar():
    estilo()
    st.title("🎉 GANASTE")
    st.balloons()
    nav("ganar")

def perder():
    estilo()
    st.title("❌ Código incorrecto")
    nav("perder")

# ---------------- ROUTER ----------------

pantallas = {
    "inicio": inicio,
    "mapa": mapa,
    "r1": r1,
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "r5": r5,
    "r6": r6,
    "r7": r7,
    "final": final,
    "ganar": ganar,
    "perder": perder
}

pantallas[st.session_state.pantalla]()
