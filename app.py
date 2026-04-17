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
    .pregunta {font-size: 22px; font-weight: bold;}
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
        st.success(f"✔ Correcto → Anota: {codigo}")
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
    ### 🎯 ¿Cómo jugar?

    Vas a resolver una serie de retos relacionados con:
    - 📐 Geometría
    - 🎨 Color
    - 🧠 Arte de Sonia Delaunay

    #### 🧩 En cada reto:
    - Elige una respuesta
    - Cada respuesta tiene un número
    - **Debes anotar ese número**

    #### 🔐 Reto final:
    - Tendrás varios números
    - Debes escribirlos en orden
    - Ese será el código final

    #### ⭐ Puntuación:
    ✔ +10 puntos → respuesta correcta  
    ❌ -2 puntos → respuesta incorrecta
    """)

    st.session_state.nombre = st.text_input("Nombre del jugador")
    st.session_state.nivel = st.radio("Nivel", ["Fácil","Medio","Difícil"])

    st.write(f"⭐ Puntos actuales: {st.session_state.puntos}")

    if st.button("🚀 Comenzar"):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    estilo()

    st.header("🗺️ Mapa del juego")
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    if st.button("🔵 1. Círculos"): ir("r1")
    if st.button("🔁 2. Patrones"): ir("r2")
    if st.button("🔺 3. Geometría"): ir("r3")
    if st.button("🌈 4. Color"): ir("r4")
    if st.button("🧠 5. Ritmo"): ir("r5")
    if st.button("📐 6. Simetría"): ir("r6")
    if st.button("🎨 7. Composición"): ir("r7")
    if st.button("🔐 Introducir código"): ir("final")

# ---------------- RETOS ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    r = st.radio("¿Qué línea representa el radio?", [
        "1 → Circunferencia completa",
        "2 → Diámetro",
        "3 → Del centro al borde"
    ])

    if st.button("Responder"):
        evaluar("3" in r, "3")

    nav()

def r2():
    estilo()
    st.header("🔁 Patrones")

    st.markdown("Observa el patrón:")
    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("¿Qué color continúa?", [
        "1 → Azul",
        "2 → Rojo",
        "3 → Amarillo"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "7")  # CORRECTO: AZUL

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

    r = st.radio("¿Cuáles son los colores primarios?", [
        "1 → Rojo, azul y amarillo",
        "2 → Verde, azul y rojo",
        "3 → Negro y blanco"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "5")

    nav()

def r5():
    estilo()
    st.header("🧠 Ritmo visual")

    r = st.radio("¿Qué crea ritmo visual?", [
        "1 → Repetición de formas",
        "2 → Un solo color",
        "3 → Texto"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "8")

    nav()

def r6():
    estilo()
    st.header("📐 Simetría")

    r = st.radio("¿Qué es la simetría?", [
        "1 → Partes iguales",
        "2 → Desorden",
        "3 → Aleatorio"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "6")

    nav()

def r7():
    estilo()
    st.header("🎨 Composición")

    r = st.radio("¿Qué mejora una obra artística?", [
        "1 → Organización visual",
        "2 → Caos",
        "3 → Nada"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "4")

    nav()

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Introduce el código final")

    st.markdown("""
    ### 📌 Instrucciones

    - Usa los números que has anotado  
    - Escríbelos en el orden de los retos  
    - Ejemplo: 3725...
    """)

    c = st.text_input("Código")

    if st.button("Comprobar"):
        if c == "".join(st.session_state.codigos):
            ir("ganar")
        else:
            ir("perder")

    nav()

# ---------------- RESULTADO ----------------

def ganar():
    estilo()
    st.title("🎉 ¡HAS GANADO!")
    st.balloons()
    st.write(f"⭐ Puntuación final: {st.session_state.puntos}")
    nav()

def perder():
    estilo()
    st.title("❌ Código incorrecto")
    st.write("Revisa los números que anotaste")
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
