import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="Juego Delaunay", layout="wide")

# ---------------- ESTADO ----------------
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "codigos" not in st.session_state:
    st.session_state.codigos = []

if "inicio" not in st.session_state:
    st.session_state.inicio = datetime.datetime.now()

# ---------------- FUNCIONES ----------------
def ir(p):
    st.session_state.pantalla = p
    st.rerun()

def fondo(color):
    st.markdown(f"""
    <style>
    .stApp {{background-color: {color}; color: white;}}
    </style>
    """, unsafe_allow_html=True)

def ayuda():
    st.markdown("[🤖 Abrir IA](https://chat.openai.com/)")

# ---------------- PANTALLAS ----------------
def inicio():
    fondo("#111111")
    st.title("🎨 El código secreto del color")
    if st.button("Comenzar"):
        ir("mapa")

def mapa():
    fondo("#111111")
    st.title("Mapa de retos")

    if st.button("🔵 Círculos"): ir("r1")
    if st.button("🔁 Patrones"): ir("r2")
    if st.button("🔺 Geometría"): ir("r3")
    if st.button("🌈 Color"): ir("r4")
    if st.button("🔐 Final"): ir("final")

    ayuda()

def r1():
    fondo("#1D4ED8")
    st.header("Círculos")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Circle_radii.svg")

    r = st.radio("¿Radio?", ["Línea completa","Centro-borde","Diámetro"])

    if st.button("Responder"):
        if r == "Centro-borde":
            st.success("Correcto")
            st.session_state.codigos.append("3")
        else:
            st.error("Incorrecto")

    if st.button("Volver"): ir("mapa")

def r2():
    fondo("#E63946")
    st.header("Patrones")

    r = st.radio("🔴🔵🔴🔵🔴 ?", ["🔴","🔵","🟡"])

    if st.button("Responder"):
        if r == "🔵":
            st.success("Correcto")
            st.session_state.codigos.append("7")
        else:
            st.error("Incorrecto")

    if st.button("Volver"): ir("mapa")

def r3():
    fondo("#FFD60A")
    st.header("Geometría")

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Sonia_Delaunay%2C_1914%2C_Electric_Prismes.jpg")

    r = st.radio("Formas?", ["Círculos","Triángulos","Ninguna"])

    if st.button("Responder"):
        if r == "Triángulos":
            st.success("Correcto")
            st.session_state.codigos.append("2")
        else:
            st.error("Incorrecto")

    if st.button("Volver"): ir("mapa")

def r4():
    fondo("#2A9D8F")
    st.header("Color")

    r = st.radio("Mayor contraste?", ["Azul+azul","Rojo+verde","Amarillo+naranja"])

    if st.button("Responder"):
        if r == "Rojo+verde":
            st.success("Correcto")
            st.session_state.codigos.append("5")
        else:
            st.error("Incorrecto")

    if st.button("Volver"): ir("mapa")

def final():
    fondo("#000000")
    st.header("Código final")

    c = st.text_input("Introduce código")

    if st.button("Comprobar"):
        correcto = "".join(st.session_state.codigos)
        if c == correcto:
            st.success("🎉 COMPLETADO")
        else:
            st.error("Incorrecto")

    if st.button("Volver"): ir("mapa")

# ---------------- ROUTER ----------------
pantallas = {
    "inicio": inicio,
    "mapa": mapa,
    "r1": r1,
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "final": final
}

pantallas[st.session_state.pantalla]()
