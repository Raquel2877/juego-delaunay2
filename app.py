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

if "uid" not in st.session_state:
    st.session_state.uid = 0

# ---------------- UTILS ----------------
def new_key(base):
    st.session_state.uid += 1
    return f"{base}_{st.session_state.uid}"

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

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

# ---------------- NAV ----------------
def nav(id):
    col1, col2 = st.columns(2)

    if col1.button("🗺️ Mapa", key=new_key(f"mapa_{id}")):
        ir("mapa")

    if col2.button("🏠 Inicio", key=new_key(f"inicio_{id}")):
        ir("inicio")

# ---------------- EVALUAR ----------------
def evaluar(correcta, codigo, id):
    if correcta:
        st.success(f"✔ Correcto → NÚMERO: {codigo}")
        st.session_state.codigos.append(codigo)
        st.session_state.puntos += 10
    else:
        st.error("❌ Incorrecto")
        st.session_state.puntos -= 2

    nav(id)

# ---------------- INICIO ----------------
def inicio():
    estilo()

    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 Cómo jugar

    - Resuelve los retos
    - Cada respuesta correcta te da un número
    - **Anota ese número**

    🔐 Código final:
    - Introduce los números en orden
    - Ejemplo: 3725
    """)

    st.session_state.nombre = st.text_input("Nombre", key=new_key("nombre"))
    st.session_state.nivel = st.radio("Nivel", ["Fácil","Medio","Difícil"], key=new_key("nivel"))

    if st.button("🚀 Empezar", key=new_key("start")):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    estilo()

    st.header("🗺️ Mapa")

    if st.button("1 Círculos", key=new_key("r1")): ir("r1")
    if st.button("2 Patrones", key=new_key("r2")): ir("r2")
    if st.button("3 Geometría", key=new_key("r3")): ir("r3")
    if st.button("4 Color", key=new_key("r4")): ir("r4")
    if st.button("5 Ritmo", key=new_key("r5")): ir("r5")
    if st.button("6 Simetría", key=new_key("r6")): ir("r6")
    if st.button("7 Composición", key=new_key("r7")): ir("r7")
    if st.button("Código final", key=new_key("final")): ir("final")

# ---------------- RETOS ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    r = st.radio("¿Qué es el radio?", [
        "1 Circunferencia",
        "2 Diámetro",
        "3 Centro al borde"
    ], key=new_key("r1_radio"))

    if st.button("Responder", key=new_key("r1_btn")):
        evaluar("3" in r, "3", "r1")

    nav("r1")

def r2():
    estilo()
    st.header("🔁 Patrones")

    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("¿Qué sigue?", [
        "1 Azul",
        "2 Rojo",
        "3 Amarillo"
    ], key=new_key("r2_radio"))

    if st.button("Responder", key=new_key("r2_btn")):
        evaluar("1" in r, "7", "r2")  # azul

    nav("r2")

def r3():
    estilo()
    st.header("🔺 Geometría")

    r = st.radio("¿Qué figura tiene 4 lados iguales?", [
        "1 Triángulo",
        "2 Cuadrado",
        "3 Círculo"
    ], key=new_key("r3_radio"))

    if st.button("Responder", key=new_key("r3_btn")):
        evaluar("2" in r, "2", "r3")

    nav("r3")

def r4():
    estilo()
    st.header("🌈 Color")

    r = st.radio("Colores primarios", [
        "1 Rojo azul amarillo",
        "2 Verde azul rojo",
        "3 Blanco negro"
    ], key=new_key("r4_radio"))

    if st.button("Responder", key=new_key("r4_btn")):
        evaluar("1" in r, "5", "r4")

    nav("r4")

def r5():
    estilo()
    st.header("🧠 Ritmo")

    r = st.radio("¿Qué crea ritmo?", [
        "1 Repetición",
        "2 Un color",
        "3 Texto"
    ], key=new_key("r5_radio"))

    if st.button("Responder", key=new_key("r5_btn")):
        evaluar("1" in r, "8", "r5")

    nav("r5")

def r6():
    estilo()
    st.header("📐 Simetría")

    r = st.radio("¿Qué es simetría?", [
        "1 Partes iguales",
        "2 Caos",
        "3 Aleatorio"
    ], key=new_key("r6_radio"))

    if st.button("Responder", key=new_key("r6_btn")):
        evaluar("1" in r, "6", "r6")

    nav("r6")

def r7():
    estilo()
    st.header("🎨 Composición")

    r = st.radio("¿Qué mejora una obra?", [
        "1 Organización",
        "2 Caos",
        "3 Nada"
    ], key=new_key("r7_radio"))

    if st.button("Responder", key=new_key("r7_btn")):
        evaluar("1" in r, "4", "r7")

    nav("r7")

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Código final")

    c = st.text_input("Introduce el código", key=new_key("codigo"))

    if st.button("Comprobar", key=new_key("check")):
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
