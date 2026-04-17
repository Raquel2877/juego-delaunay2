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

if "errores" not in st.session_state:
    st.session_state.errores = 0

# ---------------- SONIDOS ----------------
def sonido_acierto():
    st.audio("https://www.soundjay.com/buttons/sounds/button-4.mp3")

def sonido_error():
    st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")

# ---------------- ESTILO DELAUNAY ----------------
def fondo(c1, c2):
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {c1}, {c2});
        color: white;
    }}
    .stButton>button {{
        background-color: #E63946;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }}
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- NAV ----------------
def botones_nav():
    col1, col2 = st.columns(2)

    if col1.button("🗺️ Mapa"):
        ir("mapa")

    if col2.button("🏠 Inicio"):
        ir("inicio")

# ---------------- INICIO ----------------
def inicio():
    fondo("#111111", "#1D4ED8")

    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 ¿Cómo se juega?

    - Introduce tu nombre  
    - Elige un nivel  
    - Resuelve los retos  

    🧠 En cada reto:
    - Elige una respuesta
    - Cada respuesta tiene un número
    - **Anota ese número**

    🔐 Al final:
    - Introduce el código con todos los números
    - En el orden de los retos

    ⭐ Sistema de puntos:
    - Acierto: +10
    - Error: -2
    """)

    st.session_state.nombre = st.text_input("Tu nombre")

    st.session_state.nivel = st.radio("Nivel", ["Fácil", "Medio", "Difícil"])

    st.write(f"⭐ Puntos actuales: {st.session_state.puntos}")

    if st.button("🚀 Comenzar"):
        ir("mapa")

# ---------------- MAPA ----------------
def mapa():
    fondo("#E63946", "#FFD60A")

    st.title("🗺️ Mapa del juego")
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    if st.button("🔵 1. Círculos"): ir("r1")
    if st.button("🔁 2. Patrones"): ir("r2")
    if st.button("🔺 3. Geometría"): ir("r3")
    if st.button("🌈 4. Color"): ir("r4")
    if st.button("🧠 5. Ritmo"): ir("r5")
    if st.button("📐 6. Simetría"): ir("r6")
    if st.button("🎨 7. Composición"): ir("r7")
    if st.button("🔐 Introducir código"): ir("final")

# ---------------- EVALUAR ----------------
def evaluar(correcta, codigo):
    if correcta:
        st.success(f"✔ Correcto → Anota el número: {codigo}")
        sonido_acierto()
        st.session_state.puntos += 10
        st.session_state.codigos.append(codigo)
    else:
        st.error("❌ Incorrecto")
        sonido_error()
        st.session_state.puntos -= 2
        st.session_state.errores += 1

# ---------------- RETOS ----------------

def r1():
    fondo("#1D4ED8", "#2A9D8F")
    st.header("🔵 Círculos en la obra de Delaunay")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    r = st.radio("¿Qué línea representa el radio?", [
        "1 → Circunferencia completa",
        "2 → Diámetro",
        "3 → Del centro al borde"
    ])

    if st.button("Responder"):
        evaluar("3" in r, "3")

    botones_nav()

def r2():
    fondo("#E63946", "#1D4ED8")
    st.header("🔁 Patrones en el arte")

    st.markdown("Observa la repetición de colores:")

    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("¿Qué color sigue?", [
        "1 → Azul",
        "2 → Rojo",
        "3 → Amarillo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "7")

    botones_nav()

def r3():
    fondo("#FFD60A", "#E63946")
    st.header("🔺 Formas geométricas")

    r = st.radio("¿Qué figura tiene 4 lados iguales?", [
        "1 → Triángulo",
        "2 → Cuadrado",
        "3 → Círculo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "2")

    botones_nav()

def r4():
    fondo("#2A9D8F", "#FFD60A")
    st.header("🌈 Colores")

    r = st.radio("¿Cuáles son los colores primarios?", [
        "1 → Rojo, azul y amarillo",
        "2 → Verde, azul y rojo",
        "3 → Negro, blanco y gris"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "5")

    botones_nav()

def r5():
    fondo("#E63946", "#2A9D8F")
    st.header("🧠 Ritmo visual")

    r = st.radio("¿Qué crea ritmo visual?", [
        "1 → Repetición de formas",
        "2 → Un solo color",
        "3 → Texto"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "8")

    botones_nav()

def r6():
    fondo("#1D4ED8", "#FFD60A")
    st.header("📐 Simetría")

    r = st.radio("¿Qué es simetría?", [
        "1 → Partes iguales",
        "2 → Desorden",
        "3 → Aleatorio"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "6")

    botones_nav()

def r7():
    fondo("#FFD60A", "#1D4ED8")
    st.header("🎨 Composición artística")

    r = st.radio("¿Qué mejora una obra?", [
        "1 → Organización visual",
        "2 → Caos",
        "3 → Nada"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "4")

    botones_nav()

# ---------------- FINAL ----------------

def final():
    fondo("#111111", "#E63946")

    st.header("🔐 Código final")

    st.markdown("""
    ### 📌 ¿Qué debes hacer?

    - Usa los números que anotaste  
    - Escríbelos en orden  
    - Ejemplo: 3725...
    """)

    codigo = st.text_input("Código")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)

        if codigo == correcto:
            ir("ganar")
        else:
            ir("perder")

    botones_nav()

# ---------------- GANAR / PERDER ----------------

def ganar():
    fondo("#2A9D8F", "#FFD60A")
    st.title("🎉 ¡HAS GANADO!")
    st.balloons()
    st.write(f"⭐ Puntuación final: {st.session_state.puntos}")

    if st.button("🏠 Inicio"):
        ir("inicio")

def perder():
    fondo("#E63946", "#111111")
    st.title("❌ Código incorrecto")
    st.write("Revisa los números que anotaste")

    if st.button("🔁 Reintentar"):
        ir("mapa")

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
