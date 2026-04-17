import streamlit as st
import pandas as pd
import datetime
import os

# (Opcional IA)
try:
    from openai import OpenAI
    client = OpenAI()
    IA_ACTIVA = True
except:
    IA_ACTIVA = False

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

if "nivel" not in st.session_state:
    st.session_state.nivel = "facil"

if "errores_tipo" not in st.session_state:
    st.session_state.errores_tipo = {
        "geometria": 0,
        "color": 0,
        "patrones": 0
    }

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

# ---------------- IA ----------------
def generar_pregunta(tema):
    if not IA_ACTIVA:
        st.warning("IA no configurada")
        return

    prompt = f"""
    Genera una pregunta tipo test para 1º ESO.
    Tema: {tema}
    Nivel: {st.session_state.nivel}
    3 opciones numeradas y respuesta correcta.
    """

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    st.write(r.choices[0].message.content)

# ---------------- ADAPTACIÓN ----------------
def adaptar(tipo):
    st.session_state.errores_tipo[tipo] += 1

    if st.session_state.errores_tipo[tipo] >= 2:
        st.warning("💡 Pista adaptativa:")
        if tipo == "geometria":
            st.info("El radio va del centro al borde.")
        if tipo == "color":
            st.info("Los colores opuestos contrastan.")
        if tipo == "patrones":
            st.info("Observa la repetición.")

# ---------------- GUARDAR ----------------
def guardar():
    fin = datetime.datetime.now()

    df = pd.DataFrame([{
        "puntos": st.session_state.puntos,
        "duracion": (fin - st.session_state.inicio).seconds,
        "geo": st.session_state.errores_tipo["geometria"],
        "color": st.session_state.errores_tipo["color"],
        "patrones": st.session_state.errores_tipo["patrones"]
    }])

    os.makedirs("data", exist_ok=True)

    archivo = "data/resultados.csv"
    if os.path.exists(archivo):
        df.to_csv(archivo, mode="a", index=False, header=False)
    else:
        df.to_csv(archivo, index=False)

# ---------------- DASHBOARD ----------------
def dashboard():
    st.title("📊 Analítica docente")

    try:
        df = pd.read_csv("data/resultados.csv")
        st.dataframe(df)
        st.bar_chart(df[["geo","color","patrones"]])
    except:
        st.info("Sin datos")

# ---------------- INICIO ----------------
def inicio():
    fondo("#111","#1D4ED8")

    st.title("🎨 Código secreto del color")

    st.markdown("""
    Resuelve retos y **anota los números correctos**.
    Al final introduce el código en orden.
    """)

    st.session_state.nivel = st.radio("Nivel", ["facil","medio","dificil"])

    if st.button("Jugar"):
        ir("mapa")

    if st.button("Dashboard docente"):
        ir("dashboard")

# ---------------- MAPA ----------------
def mapa():
    fondo("#E63946","#FFD60A")

    st.write(f"⭐ {st.session_state.puntos} puntos")

    if st.button("Círculos"): ir("r1")
    if st.button("Patrones"): ir("r2")
    if st.button("Geometría"): ir("r3")
    if st.button("Color"): ir("r4")
    if st.button("Extra IA"): ir("ia")
    if st.button("Final"): ir("final")

# ---------------- RETOS ----------------
def evaluar(ok, codigo, tipo):
    if ok:
        st.success(f"✔ Correcto → {codigo}")
        st.session_state.codigos.append(codigo)
        st.session_state.puntos += 10
    else:
        st.error("❌ Incorrecto")
        st.session_state.puntos -= 2
        adaptar(tipo)

def r1():
    fondo("#1D4ED8","#2A9D8F")
    st.header("Círculos")

    r = st.radio("¿Qué es el radio?", [
        "1 circunferencia",
        "2 diámetro",
        "3 centro-borde"
    ])

    if st.button("Responder"):
        evaluar("3" in r, "3", "geometria")

    nav()

def r2():
    fondo("#E63946","#1D4ED8")
    st.header("Patrones")

    st.markdown("🔴 🔵 🔴 🔵 🔴 ?")

    r = st.radio("Respuesta", [
        "1 azul",
        "2 rojo",
        "3 amarillo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "7", "patrones")

    nav()

def r3():
    fondo("#FFD60A","#E63946")
    st.header("Geometría")

    r = st.radio("¿Qué forma tiene 4 lados iguales?", [
        "1 triángulo",
        "2 cuadrado",
        "3 círculo"
    ])

    if st.button("Responder"):
        evaluar("2" in r, "2", "geometria")

    nav()

def r4():
    fondo("#2A9D8F","#FFD60A")
    st.header("Color")

    r = st.radio("Colores primarios", [
        "1 rojo azul amarillo",
        "2 verde azul rojo",
        "3 blanco negro"
    ])

    if st.button("Responder"):
        evaluar("1" in r, "5", "color")

    nav()

# ---------------- IA ----------------
def ia():
    fondo("#111","#E63946")
    st.header("🤖 Generador de retos")

    tema = st.selectbox("Tema", ["geometria","color","patrones"])

    if st.button("Generar pregunta"):
        generar_pregunta(tema)

    nav()

# ---------------- FINAL ----------------
def final():
    fondo("#111","#000")

    st.header("Código final")

    c = st.text_input("Código")

    if st.button("Comprobar"):
        if c == "".join(st.session_state.codigos):
            ir("ganar")
        else:
            ir("perder")

    nav()

# ---------------- GANAR/PERDER ----------------
def ganar():
    fondo("#2A9D8F","#FFD60A")
    st.title("🎉 Ganaste")
    guardar()

def perder():
    fondo("#E63946","#111")
    st.title("❌ Intenta de nuevo")

# ---------------- NAV ----------------
def nav():
    if st.button("Mapa"):
        ir("mapa")
    if st.button("Inicio"):
        ir("inicio")

# ---------------- ROUTER ----------------
pantallas = {
    "inicio": inicio,
    "mapa": mapa,
    "r1": r1,
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "ia": ia,
    "final": final,
    "ganar": ganar,
    "perder": perder,
    "dashboard": dashboard
}

pantallas[st.session_state.pantalla]()
