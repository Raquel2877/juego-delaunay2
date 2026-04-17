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

if "respuestas" not in st.session_state:
    st.session_state.respuestas = []

if "inicio" not in st.session_state:
    st.session_state.inicio = datetime.datetime.now()

# ---------------- ESTILO DELAUNAY ----------------
def estilo():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    .stButton>button {
        background-color: #E63946;
        color: white;
        border-radius: 12px;
        font-size: 18px;
    }
    h1, h2, h3 {
        color: #FFD60A;
    }
    </style>
    """, unsafe_allow_html=True)

def ir(p):
    st.session_state.pantalla = p
    st.rerun()

# ---------------- IA INTERNA ----------------
def ayuda_ia(tipo):
    if tipo == "patron":
        st.info("Observa los colores: rojo y azul se alternan.")
    elif tipo == "radio":
        st.info("El radio va del centro al borde.")
    else:
        st.info("Piensa en la lógica del patrón.")

# ---------------- GUARDAR ----------------
def guardar(nombre):
    fin = datetime.datetime.now()

    df = pd.DataFrame([{
        "nombre": nombre,
        "puntos": st.session_state.puntos,
        "duracion": (fin - st.session_state.inicio).seconds
    }])

    os.makedirs("data", exist_ok=True)

    archivo = "data/resultados.csv"

    if os.path.exists(archivo):
        df.to_csv(archivo, mode="a", index=False, header=False)
    else:
        df.to_csv(archivo, index=False)

# ---------------- PANTALLAS ----------------

def inicio():
    estilo()

    st.title("🎨 El código secreto del color")

    st.markdown("""
    ### 🎯 MISIÓN
    
    Vas a resolver **7 retos**.
    
    Cada reto te dará **un número secreto**.
    
    🔐 Al final tendrás que formar el código en este orden:
    
    1. Círculos  
    2. Patrones  
    3. Geometría  
    4. Color  
    5. Ritmo  
    6. Simetría  
    7. Composición  
    
    👉 Ejemplo: 3 7 2 5 ...
    
    ⭐ Cada acierto suma puntos.
    """)

    nombre = st.text_input("Tu nombre")

    if st.button("🚀 Empezar"):
        st.session_state.nombre = nombre
        ir("mapa")

# ---------------- MAPA ----------------

def mapa():
    estilo()

    st.title("🗺️ Mapa del juego")
    st.write(f"⭐ Puntos: {st.session_state.puntos}")

    if st.button("🔵 Círculos"): ir("r1")
    if st.button("🔁 Patrones"): ir("r2")
    if st.button("🔺 Geometría"): ir("r3")
    if st.button("🌈 Color"): ir("r4")
    if st.button("🧠 Ritmo"): ir("r5")
    if st.button("📐 Simetría"): ir("r6")
    if st.button("🎨 Composición"): ir("r7")
    if st.button("🔐 Final"): ir("final")

# ---------------- FUNCION EVALUAR ----------------

def evaluar(correcta, codigo):
    if correcta:
        st.success(f"Correcto (+10) Código: {codigo}")
        st.session_state.puntos += 10
        if codigo not in st.session_state.codigos:
            st.session_state.codigos.append(codigo)
    else:
        st.error("Incorrecto (-2)")
        st.session_state.puntos -= 2

# ---------------- RETO 1 ----------------

def r1():
    estilo()
    st.header("🔵 Círculos")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    r = st.radio("¿Qué línea es el radio?", [
        "Centro-borde", "Diámetro", "Circunferencia"
    ])

    if st.button("Responder"):
        evaluar(r == "Centro-borde", "3")

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- RETO 2 (CORREGIDO) ----------------

def r2():
    estilo()
    st.header("🔁 Patrones")

    st.markdown("### Observa el patrón:")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("<div style='background:red;height:80px'></div>", unsafe_allow_html=True)
    col2.markdown("<div style='background:blue;height:80px'></div>", unsafe_allow_html=True)
    col3.markdown("<div style='background:red;height:80px'></div>", unsafe_allow_html=True)
    col4.markdown("<div style='background:blue;height:80px'></div>", unsafe_allow_html=True)

    st.write("¿Qué color continúa?")

    r = st.radio("Respuesta:", ["Rojo", "Azul", "Amarillo"])

    if st.button("Responder"):
        correcta = r == "Rojo"
        evaluar(correcta, "7")
        if not correcta:
            ayuda_ia("patron")

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- RESTO RETOS ----------------

def r3():
    estilo()
    st.header("🔺 Geometría")

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    r = st.radio("¿Qué tipo de formas ves?", [
        "Geométricas", "Naturales", "Texto"
    ])

    if st.button("Responder"):
        evaluar(r == "Geométricas", "2")

    if st.button("⬅ Volver"): ir("mapa")

def r4():
    estilo()
    st.header("🌈 Color")

    r = st.radio("¿Mayor contraste?", [
        "Colores opuestos", "Colores iguales", "Colores claros"
    ])

    if st.button("Responder"):
        evaluar(r == "Colores opuestos", "5")

    if st.button("⬅ Volver"): ir("mapa")

def r5():
    estilo()
    st.header("🧠 Ritmo")

    r = st.radio("¿Qué crea ritmo visual?", [
        "Repetición", "Un solo color", "Texto"
    ])

    if st.button("Responder"):
        evaluar(r == "Repetición", "8")

    if st.button("⬅ Volver"): ir("mapa")

def r6():
    estilo()
    st.header("📐 Simetría")

    r = st.radio("¿Qué es simetría?", [
        "Partes iguales", "Desorden", "Aleatorio"
    ])

    if st.button("Responder"):
        evaluar(r == "Partes iguales", "6")

    if st.button("⬅ Volver"): ir("mapa")

def r7():
    estilo()
    st.header("🎨 Composición")

    r = st.radio("¿Qué mejora una composición?", [
        "Organización", "Caos", "Nada"
    ])

    if st.button("Responder"):
        evaluar(r == "Organización", "4")

    if st.button("⬅ Volver"): ir("mapa")

# ---------------- FINAL ----------------

def final():
    estilo()
    st.header("🔐 Código final")

    st.write("Introduce los números en el orden de los retos")

    codigo = st.text_input("Código")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)

        if codigo == correcto:
            ir("ganar")
        else:
            ir("perder")

    if st.button("⬅ Volver"): ir("mapa")

def ganar():
    estilo()
    st.title("🎉 HAS GANADO")
    st.balloons()
    guardar(st.session_state.nombre)

def perder():
    estilo()
    st.title("❌ Intenta de nuevo")

    if st.button("Volver"):
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
