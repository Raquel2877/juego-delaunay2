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

if "inicio" not in st.session_state:
    st.session_state.inicio = datetime.datetime.now()

# ---------------- ESTILO ----------------
def estilo():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1D4ED8, #E63946, #FFD60A);
        color: white;
        font-family: Arial;
    }
    h1 {font-size: 45px; color: #FFD60A;}
    h2 {font-size: 30px;}
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- NAV ----------------
def nav():
    col1, col2 = st.columns(2)
    if col1.button("🗺️ Volver al mapa"):
        ir("mapa")
    if col2.button("🏠 Volver al inicio"):
        ir("inicio")

# ---------------- EVALUAR ----------------
def evaluar(correcta, codigo):
    if correcta:
        st.success("✔ Correcto. Anota el número de esta respuesta.")
        st.session_state.puntos += 10
        st.session_state.codigos.append(codigo)
    else:
        st.error("❌ Incorrecto")
        st.session_state.puntos -= 2

    nav()

# ---------------- INICIO ----------------
def inicio():
    estilo()
    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 Cómo jugar

    - Resuelve los retos  
    - Cada respuesta tiene un número  
    - **Debes anotarlo**  

    🔐 Al final:
    - Introduce el código en orden  

    ⭐ Puntuación:
    ✔ +10 / ❌ -2
    """)

    st.session_state.nombre = st.text_input("Nombre")
    st.session_state.nivel = st.radio("Nivel", ["Fácil","Medio","Difícil"])

    if st.button("🚀 Empezar"):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    estilo()
    st.header("🗺️ Mapa")

    if st.button("1. Círculos"): ir("r1")
    if st.button("2. Patrones"): ir("r2")
    if st.button("3. Geometría"): ir("r3")
    if st.button("4. Color"): ir("r4")
    if st.button("5. Ritmo"): ir("r5")
    if st.button("6. Simetría"): ir("r6")
    if st.button("7. Composición"): ir("r7")
    if st.button("Código final"): ir("final")

# ---------------- RETOS CON NIVELES ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    nivel = st.session_state.nivel

    if nivel == "Fácil":
        pregunta = "¿Qué línea va del centro al borde?"
        opciones = ["1 Circunferencia","2 Diámetro","3 Radio"]
        correcta = "3"
        codigo = "3"

    elif nivel == "Medio":
        pregunta = "¿Cómo se llama la línea que une dos puntos pasando por el centro?"
        opciones = ["1 Radio","2 Diámetro","3 Arco"]
        correcta = "2"
        codigo = "1"

    else:
        pregunta = "¿Qué relación tiene el diámetro con el radio?"
        opciones = ["1 Es igual","2 Es el doble","3 Es la mitad"]
        correcta = "2"
        codigo = "9"

    r = st.radio(pregunta, opciones)

    if st.button("Responder"):
        evaluar(correcta in r, codigo)

    nav()

# ---------------- PATRONES ----------------

def r2():
    estilo()
    st.header("🔁 Patrones")

    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("¿Qué color sigue?", [
        "1 Azul",
        "2 Rojo",
        "3 Amarillo"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "7")  # AZUL CORRECTO

    nav()

# ---------------- GEOMETRÍA ----------------

def r3():
    estilo()
    st.header("🔺 Geometría")

    nivel = st.session_state.nivel

    if nivel == "Fácil":
        pregunta = "¿Cuál tiene 4 lados iguales?"
        opciones = ["1 Triángulo","2 Cuadrado","3 Círculo"]
        correcta = "2"
        codigo = "2"

    elif nivel == "Medio":
        pregunta = "¿Cuántos lados tiene un pentágono?"
        opciones = ["1 4","2 5","3 6"]
        correcta = "2"
        codigo = "5"

    else:
        pregunta = "¿Cuánto mide un ángulo recto?"
        opciones = ["1 45°","2 90°","3 180°"]
        correcta = "2"
        codigo = "8"

    r = st.radio(pregunta, opciones)

    if st.button("Responder"):
        evaluar(correcta in r, codigo)

    nav()

# ---------------- COLOR ----------------

def r4():
    estilo()
    st.header("🌈 Color")

    nivel = st.session_state.nivel

    if nivel == "Fácil":
        pregunta = "¿Cuáles son los colores primarios?"
        opciones = ["1 Rojo azul amarillo","2 Verde azul rojo","3 Blanco negro"]
        correcta = "1"
        codigo = "5"

    elif nivel == "Medio":
        pregunta = "Rojo + amarillo = ?"
        opciones = ["1 Verde","2 Naranja","3 Azul"]
        correcta = "2"
        codigo = "4"

    else:
        pregunta = "¿Qué colores generan contraste?"
        opciones = ["1 Iguales","2 Opuestos","3 Claros"]
        correcta = "2"
        codigo = "6"

    r = st.radio(pregunta, opciones)

    if st.button("Responder"):
        evaluar(correcta in r, codigo)

    nav()

# ---------------- RESTO ----------------

def r5():
    estilo()
    st.header("🧠 Ritmo")
    r = st.radio("¿Qué crea ritmo visual?", ["1 Repetición","2 Un color","3 Texto"])
    if st.button("Responder"):
        evaluar("1" in r, "8")
    nav()

def r6():
    estilo()
    st.header("📐 Simetría")
    r = st.radio("¿Qué es simetría?", ["1 Partes iguales","2 Caos","3 Aleatorio"])
    if st.button("Responder"):
        evaluar("1" in r, "6")
    nav()

def r7():
    estilo()
    st.header("🎨 Composición")
    r = st.radio("¿Qué mejora una obra?", ["1 Organización","2 Caos","3 Nada"])
    if st.button("Responder"):
        evaluar("1" in r, "4")
    nav()

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Código final")

    c = st.text_input("Introduce el código")

    if st.button("Comprobar"):
        if c == "".join(st.session_state.codigos):
            ir("ganar")
        else:
            ir("perder")

    nav()

def ganar():
    estilo()
    st.title("🎉 ¡HAS GANADO!")
    st.balloons()
    nav()

def perder():
    estilo()
    st.title("❌ Código incorrecto")
    nav()

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
