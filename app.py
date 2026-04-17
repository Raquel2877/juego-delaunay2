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

# ---------------- SONIDOS ----------------
def sonido_acierto():
    st.audio("https://www.soundjay.com/buttons/sounds/button-4.mp3", autoplay=True)

def sonido_error():
    st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3", autoplay=True)

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
    .pregunta {font-size: 22px; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- NAV ----------------
def nav():
    col1, col2 = st.columns(2)
    if col1.button("🗺️ Mapa"):
        ir("mapa")
    if col2.button("🏠 Inicio"):
        ir("inicio")

# ---------------- EVALUAR ----------------
def evaluar(correcta, codigo):
    if correcta:
        sonido_acierto()
        st.success(f"✔ Correcto → Anota: {codigo}")
        st.session_state.puntos += 10
        st.session_state.codigos.append(codigo)
    else:
        sonido_error()
        st.error("❌ Incorrecto")
        st.session_state.puntos -= 2

    nav()

# ---------------- INICIO ----------------
def inicio():
    estilo()
    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 Cómo jugar

    - Elige una respuesta en cada reto  
    - Cada respuesta tiene un número  
    - **Anota ese número**  

    🔐 Al final tendrás que escribir el código completo  
    siguiendo el orden de los retos  

    ⭐ Puntuación:
    ✔ +10 acierto  
    ❌ -2 error  
    """)

    st.session_state.nombre = st.text_input("Nombre")
    st.session_state.nivel = st.radio("Nivel", ["Fácil","Medio","Difícil"])

    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    if st.button("🚀 Empezar"):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    estilo()
    st.header("🗺️ Mapa del juego")

    if st.button("🔵 Círculos"): ir("r1")
    if st.button("🔁 Patrones"): ir("r2")
    if st.button("🔺 Geometría"): ir("r3")
    if st.button("🌈 Color"): ir("r4")
    if st.button("🧠 Ritmo"): ir("r5")
    if st.button("📐 Simetría"): ir("r6")
    if st.button("🎨 Composición"): ir("r7")
    if st.button("🔐 Código final"): ir("final")

# ---------------- RETOS ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    r = st.radio("¿Qué es el radio?", [
        "1 → Circunferencia",
        "2 → Diámetro",
        "3 → Centro al borde"
    ])

    if st.button("Responder"):
        evaluar("3" in r, "3")

    nav()

def r2():
    estilo()
    st.header("🔁 Patrones")

    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("¿Qué color sigue?", [
        "1 → Rojo",
        "2 → Azul",
        "3 → Amarillo"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "7")  # CORRECTO

    nav()

def r3():
    estilo()
    st.header("🔺 Geometría")

    r = st.radio("¿Qué figura tiene 4 lados iguales?", [
        "1 → Triángulo",
        "2 → Cuadrado",
        "3 → Círculo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "2")

    nav()

def r4():
    estilo()
    st.header("🌈 Color")

    r = st.radio("Colores primarios", [
        "1 → Rojo, azul y amarillo",
        "2 → Verde, azul y rojo",
        "3 → Blanco y negro"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "5")

    nav()

def r5():
    estilo()
    st.header("🧠 Ritmo")

    r = st.radio("¿Qué crea ritmo?", [
        "1 → Repetición",
        "2 → Un solo color",
        "3 → Texto"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "8")

    nav()

def r6():
    estilo()
    st.header("📐 Simetría")

    r = st.radio("¿Qué es simetría?", [
        "1 → Partes iguales",
        "2 → Caos",
        "3 → Aleatorio"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "6")

    nav()

def r7():
    estilo()
    st.header("🎨 Composición")

    r = st.radio("¿Qué mejora una obra?", [
        "1 → Organización",
        "2 → Caos",
        "3 → Nada"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "4")

    nav()

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Código final")

    st.markdown("""
    Introduce los números que anotaste  
    en el orden de los retos  
    Ejemplo: 3725...
    """)

    c = st.text_input("Código")

    if st.button("Comprobar"):
        if c == "".join(st.session_state.codigos):
            ir("ganar")
        else:
            ir("perder")

    nav()

def ganar():
    estilo()
    st.title("🎉 GANASTE")
    st.balloons()
    nav()

def perder():
    estilo()
    st.title("❌ Intenta otra vez")
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
