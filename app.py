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

# ---------------- IA ----------------
def ayuda_ia():
    st.markdown("### 🤖 ¿Necesitas ayuda?")
    st.markdown("[Abrir asistente IA](https://chat.openai.com/)")

# ---------------- GUARDAR ----------------
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

# ---------------- RANKING ----------------
def ranking():
    st.subheader("🏆 Ranking")

    try:
        df = pd.read_csv("data/resultados.csv")
        df = df.sort_values(by="puntos", ascending=False)
        st.dataframe(df.head(10))
    except:
        st.info("Aún no hay partidas registradas")

# ---------------- PANTALLAS ----------------

def inicio():
    estilo()
    st.title("🎨 El código secreto del color")

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    st.markdown("""
    ### 🎯 OBJETIVO DEL JUEGO
    
    Debes completar retos para conseguir números secretos.
    
    🧩 Cada reto te da un número.
    
    🔐 Al final tendrás que introducir el código en este orden:
    
    1. Círculos  
    2. Patrones  
    3. Geometría  
    4. Color  
    5. + Retos extra
    
    ⭐ Cuantos más aciertos, más puntos.
    """)

    nombre = st.text_input("Introduce tu nombre")

    if st.button("🚀 Comenzar misión"):
        st.session_state.nombre = nombre
        ir("mapa")

    ranking()
    ayuda_ia()

# ---------------- MAPA ----------------

def mapa():
    estilo()
    st.title("🗺️ Mapa del juego")
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    if st.button("🔵 Círculos"): ir("r1")
    if st.button("🔁 Patrones"): ir("r2")
    if st.button("🔺 Geometría"): ir("r3")
    if st.button("🌈 Color"): ir("r4")
    if st.button("🧠 Ritmo visual"): ir("r5")
    if st.button("📐 Simetría"): ir("r6")
    if st.button("🎨 Composición"): ir("r7")
    if st.button("🔐 Final"): ir("final")

    ayuda_ia()

# ---------------- RETOS ----------------

def evaluar(correcta, codigo):
    if correcta:
        st.success(f"Correcto +10 puntos (Código: {codigo})")
        st.session_state.puntos += 10
        if codigo not in st.session_state.codigos:
            st.session_state.codigos.append(codigo)
    else:
        st.error("Incorrecto -2 puntos")
        st.session_state.puntos -= 2

# 1
def r1():
    estilo()
    st.header("🔵 Círculos")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    r = st.radio("¿Qué línea representa el radio?", [
        "Toda la circunferencia",
        "Del centro al borde",
        "El diámetro"
    ])

    if st.button("Responder"):
        evaluar(r == "Del centro al borde", "3")

    if st.button("⬅ Volver"): ir("mapa")

# 2
def r2():
    estilo()
    st.header("🔁 Patrones")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Pattern_examples.svg")

    r = st.radio("¿Qué color continúa el patrón?", ["🔴","🔵","🟡"])

    if st.button("Responder"):
        evaluar(r == "🔵", "7")

    if st.button("⬅ Volver"): ir("mapa")

# 3
def r3():
    estilo()
    st.header("🔺 Geometría")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    r = st.radio("¿Qué tipo de formas predominan?", [
        "Formas geométricas",
        "Figuras realistas",
        "Letras"
    ])

    if st.button("Responder"):
        evaluar(r == "Formas geométricas", "2")

    if st.button("⬅ Volver"): ir("mapa")

# 4
def r4():
    estilo()
    st.header("🌈 Color")
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/Color_wheel.svg")

    r = st.radio("¿Qué combinación genera más contraste?", [
        "Colores similares",
        "Colores opuestos",
        "Colores claros"
    ])

    if st.button("Responder"):
        evaluar(r == "Colores opuestos", "5")

    if st.button("⬅ Volver"): ir("mapa")

# NUEVOS RETOS
def r5():
    estilo()
    st.header("🧠 Ritmo visual")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    r = st.radio("¿Qué crea el ritmo visual?", [
        "Repetición de formas",
        "Un solo color",
        "Texto"
    ])

    if st.button("Responder"):
        evaluar(r == "Repetición de formas", "8")

    if st.button("⬅ Volver"): ir("mapa")

def r6():
    estilo()
    st.header("📐 Simetría")

    r = st.radio("¿Qué es la simetría?", [
        "Partes iguales",
        "Colores diferentes",
        "Formas aleatorias"
    ])

    if st.button("Responder"):
        evaluar(r == "Partes iguales", "6")

    if st.button("⬅ Volver"): ir("mapa")

def r7():
    estilo()
    st.header("🎨 Composición")

    r = st.radio("¿Qué mejora una composición?", [
        "Organización visual",
        "Desorden total",
        "Un solo elemento"
    ])

    if st.button("Responder"):
        evaluar(r == "Organización visual", "4")

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Introduce el código final")

    st.write("Ordena los números según el orden de los retos.")

    codigo = st.text_input("Código")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)

        if codigo == correcto:
            ir("ganar")
        else:
            ir("perder")

    if st.button("⬅ Volver"):
        ir("mapa")

# ---------------- GANAR / PERDER ----------------

def ganar():
    estilo()
    st.title("🎉 ¡HAS GANADO!")
    st.balloons()

    st.write(f"⭐ Puntuación: {st.session_state.puntos}")

    guardar(st.session_state.nombre)

    if st.button("Ver ranking"):
        ranking()

def perder():
    estilo()
    st.title("❌ Has fallado")

    st.write("Vuelve a intentarlo revisando los retos")

    if st.button("Reintentar"):
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
