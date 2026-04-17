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

# ---------------- ESTILO VISUAL ----------------
def estilo():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1D4ED8, #E63946, #FFD60A);
        color: white;
        font-family: 'Trebuchet MS', sans-serif;
    }

    h1 {
        font-size: 48px;
        color: #FFD60A;
        text-align: center;
    }

    h2 {
        font-size: 36px;
        color: #ffffff;
    }

    .pregunta {
        font-size: 24px;
        font-weight: bold;
        color: #FFD60A;
    }

    .explicacion {
        font-size: 18px;
        color: #ffffff;
    }

    .codigo-box {
        background-color: rgba(0,0,0,0.6);
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
    }

    .stButton>button {
        background-color: #E63946;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- SONIDOS ----------------
def sonido_acierto():
    st.audio("https://www.soundjay.com/buttons/sounds/button-4.mp3")

def sonido_error():
    st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")

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
        st.success(f"✔ Correcto → ANOTA: {codigo}")
        sonido_acierto()
        st.session_state.puntos += 10
        st.session_state.codigos.append(codigo)
    else:
        st.error("❌ Incorrecto")
        sonido_error()
        st.session_state.puntos -= 2

# ---------------- INICIO ----------------
def inicio():
    estilo()

    st.markdown("<h1>🎨 El código secreto del color</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class='explicacion'>
    
    <b>🎯 OBJETIVO DEL JUEGO</b><br><br>

    Vas a resolver <b>7 retos</b> relacionados con:
    <ul>
        <li>📐 Geometría</li>
        <li>🎨 Color</li>
        <li>🧠 Arte de Sonia Delaunay</li>
    </ul>

    <b>🧠 ¿Cómo funciona?</b><br><br>

    En cada reto:
    <ul>
        <li>Eliges una respuesta</li>
        <li>Cada respuesta tiene un número</li>
        <li><b>Debes ANOTAR ese número</b></li>
    </ul>

    <b>🔐 RETO FINAL: EL CÓDIGO</b><br><br>

    Al terminar:
    <ul>
        <li>Tendrás varios números</li>
        <li>Debes escribirlos en el orden de los retos</li>
    </ul>

    <div class='codigo-box'>
    Ejemplo:<br>
    Reto 1 → 3<br>
    Reto 2 → 7<br>
    Reto 3 → 2<br><br>
    Código final → <b>372...</b>
    </div>

    <br>
    <b>⭐ PUNTOS</b><br>
    ✔ Acierto: +10<br>
    ❌ Error: -2
    
    </div>
    """, unsafe_allow_html=True)

    st.session_state.nombre = st.text_input("Tu nombre")
    st.session_state.nivel = st.radio("Nivel", ["Fácil", "Medio", "Difícil"])

    st.write(f"⭐ Puntos actuales: {st.session_state.puntos}")

    if st.button("🚀 Empezar"):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    estilo()

    st.markdown("<h2>🗺️ Mapa del juego</h2>", unsafe_allow_html=True)
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

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
    st.markdown("<h2>🔵 Círculos</h2>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    st.markdown("<div class='pregunta'>¿Qué línea representa el radio?</div>", unsafe_allow_html=True)

    r = st.radio("", [
        "1 → Circunferencia",
        "2 → Diámetro",
        "3 → Del centro al borde"
    ])

    if st.button("Responder"):
        evaluar("3" in r, "3")

    nav()

def r2():
    estilo()
    st.markdown("<h2>🔁 Patrones</h2>", unsafe_allow_html=True)

    st.markdown("<div class='pregunta'>🔴 🔵 🔴 🔵 🔴 ?</div>", unsafe_allow_html=True)

    r = st.radio("", [
        "1 → Azul",
        "2 → Rojo",
        "3 → Amarillo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "7")

    nav()

def r3():
    estilo()
    st.markdown("<h2>🔺 Geometría</h2>", unsafe_allow_html=True)

    st.markdown("<div class='pregunta'>¿Qué figura tiene 4 lados iguales?</div>", unsafe_allow_html=True)

    r = st.radio("", [
        "1 → Triángulo",
        "2 → Cuadrado",
        "3 → Círculo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "2")

    nav()

def r4():
    estilo()
    st.markdown("<h2>🌈 Color</h2>", unsafe_allow_html=True)

    st.markdown("<div class='pregunta'>¿Cuáles son los colores primarios?</div>", unsafe_allow_html=True)

    r = st.radio("", [
        "1 → Rojo, azul y amarillo",
        "2 → Verde, azul y rojo",
        "3 → Negro, blanco y gris"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "5")

    nav()

def r5():
    estilo()
    st.markdown("<h2>🧠 Ritmo</h2>", unsafe_allow_html=True)

    st.markdown("<div class='pregunta'>¿Qué crea ritmo visual?</div>", unsafe_allow_html=True)

    r = st.radio("", [
        "1 → Repetición",
        "2 → Un solo color",
        "3 → Texto"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "8")

    nav()

def r6():
    estilo()
    st.markdown("<h2>📐 Simetría</h2>", unsafe_allow_html=True)

    st.markdown("<div class='pregunta'>¿Qué es la simetría?</div>", unsafe_allow_html=True)

    r = st.radio("", [
        "1 → Partes iguales",
        "2 → Desorden",
        "3 → Aleatorio"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "6")

    nav()

def r7():
    estilo()
    st.markdown("<h2>🎨 Composición</h2>", unsafe_allow_html=True)

    st.markdown("<div class='pregunta'>¿Qué mejora una obra?</div>", unsafe_allow_html=True)

    r = st.radio("", [
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

    st.markdown("<h2>🔐 Código final</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class='explicacion'>
    Escribe los números que has anotado en orden.<br><br>
    Ejemplo: 3725...
    </div>
    """, unsafe_allow_html=True)

    c = st.text_input("Código")

    if st.button("Comprobar"):
        if c == "".join(st.session_state.codigos):
            ir("ganar")
        else:
            ir("perder")

    nav()

# ---------------- FINAL ----------------

def ganar():
    estilo()
    st.markdown("<h1>🎉 ¡HAS GANADO!</h1>", unsafe_allow_html=True)
    st.balloons()

def perder():
    estilo()
    st.markdown("<h1>❌ Código incorrecto</h1>", unsafe_allow_html=True)

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
