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

# ---------------- ESTILO DELAUNAY ----------------
def fondo_delaunay(color1, color2):
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {color1}, {color2});
        color: white;
    }}
    .stButton>button {{
        background-color: #E63946;
        color: white;
        border-radius: 12px;
        font-size: 18px;
    }}
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- INICIO ----------------

def inicio():
    fondo_delaunay("#111111", "#1D4ED8")

    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 MISIÓN
    
    Vas a resolver **7 retos**.
    
    👉 En cada reto:
    - Elige una respuesta
    - Cada respuesta tiene un **número**
    - **ANOTA ese número**
    
    🔐 Al final tendrás que escribir el código completo en este orden:
    
    1. Círculos  
    2. Patrones  
    3. Geometría  
    4. Color  
    5. Ritmo  
    6. Simetría  
    7. Composición  
    
    🧠 Ejemplo: 3-7-2-5...
    
    ⭐ IMPORTANTE: Guarda los números correctamente
    """)

    nombre = st.text_input("Tu nombre")

    if st.button("🚀 Empezar misión"):
        st.session_state.nombre = nombre
        ir("mapa")

# ---------------- MAPA ----------------

def mapa():
    fondo_delaunay("#E63946", "#FFD60A")

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

# ---------------- FUNCIÓN EVALUAR ----------------

def evaluar(correcta, codigo):
    if correcta:
        st.success(f"✔ Correcto → Anota el número: {codigo}")
        st.session_state.puntos += 10
        st.session_state.codigos.append(codigo)
    else:
        st.error("❌ Incorrecto (-2 puntos)")
        st.session_state.puntos -= 2

# ---------------- RETOS ----------------

def r1():
    fondo_delaunay("#1D4ED8", "#2A9D8F")
    st.header("🔵 Reto 1: Círculos")

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
    fondo_delaunay("#E63946", "#1D4ED8")
    st.header("🔁 Reto 2: Patrones")

    st.markdown("### Observa el patrón:")

    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("<div style='background:red;height:80px'></div>", unsafe_allow_html=True)
    col2.markdown("<div style='background:blue;height:80px'></div>", unsafe_allow_html=True)
    col3.markdown("<div style='background:red;height:80px'></div>", unsafe_allow_html=True)
    col4.markdown("<div style='background:blue;height:80px'></div>", unsafe_allow_html=True)

    r = st.radio("¿Qué color continúa?", [
        "1 → Azul",
        "2 → Rojo",
        "3 → Amarillo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "7")

    botones_nav()

def r3():
    fondo_delaunay("#FFD60A", "#E63946")
    st.header("🔺 Reto 3: Geometría")

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    r = st.radio("¿Qué tipo de formas predominan?", [
        "1 → Naturales",
        "2 → Geométricas",
        "3 → Texto"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "2")

    botones_nav()

def r4():
    fondo_delaunay("#2A9D8F", "#FFD60A")
    st.header("🌈 Reto 4: Color")

    r = st.radio("¿Qué combinación tiene más contraste?", [
        "1 → Colores similares",
        "2 → Colores opuestos",
        "3 → Colores claros"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "5")

    botones_nav()

def r5():
    fondo_delaunay("#E63946", "#2A9D8F")
    st.header("🧠 Reto 5: Ritmo")

    r = st.radio("¿Qué crea ritmo visual?", [
        "1 → Repetición",
        "2 → Un solo color",
        "3 → Texto"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "8")

    botones_nav()

def r6():
    fondo_delaunay("#1D4ED8", "#FFD60A")
    st.header("📐 Reto 6: Simetría")

    r = st.radio("¿Qué es simetría?", [
        "1 → Partes iguales",
        "2 → Caos",
        "3 → Aleatorio"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "6")

    botones_nav()

def r7():
    fondo_delaunay("#FFD60A", "#1D4ED8")
    st.header("🎨 Reto 7: Composición")

    r = st.radio("¿Qué mejora una composición?", [
        "1 → Organización visual",
        "2 → Desorden",
        "3 → Nada"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "4")

    botones_nav()

# ---------------- BOTONES NAVEGACIÓN ----------------

def botones_nav():
    col1, col2 = st.columns(2)

    if col1.button("⬅ Volver al mapa"):
        ir("mapa")

    if col2.button("🏠 Volver al inicio"):
        ir("inicio")

# ---------------- FINAL ----------------

def final():
    fondo_delaunay("#111111", "#E63946")

    st.header("🔐 INTRODUCE EL CÓDIGO FINAL")

    st.markdown("""
    ### 📌 ¿Qué tienes que hacer?
    
    - Usa los números que has ido anotando  
    - Escríbelos en el orden de los retos  
    - Sin espacios o separados por guiones
    
    👉 Ejemplo: 3725...
    """)

    codigo = st.text_input("Introduce el código")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)

        if codigo == correcto:
            ir("ganar")
        else:
            ir("perder")

    botones_nav()

# ---------------- GANAR / PERDER ----------------

def ganar():
    fondo_delaunay("#2A9D8F", "#FFD60A")
    st.title("🎉 ¡HAS GANADO!")
    st.balloons()

    st.write(f"⭐ Puntuación: {st.session_state.puntos}")

    if st.button("🏠 Volver al inicio"):
        ir("inicio")

def perder():
    fondo_delaunay("#E63946", "#111111")
    st.title("❌ Código incorrecto")

    st.write("Revisa los números que anotaste")

    if st.button("🔁 Intentar otra vez"):
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
