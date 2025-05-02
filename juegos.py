import streamlit as st
from PIL import Image
import base64

# Configuración de página
st.set_page_config(page_title="Juegos del Agua", layout="wide")


# Título
st.markdown("<h1 style='text-align: center; color: black;'>🌊 Juegos para salvar agua 💧</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Elige un juego para comenzar</h3>", unsafe_allow_html=True)

# Botones grandes
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✅ Verdadero o Falso", use_container_width=True):
        st.session_state.juego = "vf"
with col2:
    if st.button("🧠 Quiz", use_container_width=True):
        st.session_state.juego = "quiz"
with col3:
    if st.button("🃏 Memory", use_container_width=True):
        st.session_state.juego = "memory"

        import streamlit as st
import time
import random

# ---------------- CONFIGURACIÓN INICIAL ----------------

if 'puntos_vf' not in st.session_state:
    st.session_state.puntos_vf = 0
if 'index_vf' not in st.session_state:
    st.session_state.index_vf = 0
if 'inicio_vf' not in st.session_state:
    st.session_state.inicio_vf = time.time()

# ---------------- PREGUNTAS ----------------

preguntas_vf = [
    {"pregunta": "Ducharse consume menos agua que bañarse.", "respuesta": True},
    {"pregunta": "Lavar el coche con manguera gasta menos que en un túnel de lavado.", "respuesta": False},
    {"pregunta": "Cerrar el grifo mientras te cepillas los dientes ahorra agua.", "respuesta": True},
    {"pregunta": "El lavavajillas siempre gasta más agua que lavar a mano.", "respuesta": False},
    {"pregunta": "Plantar cactus ayuda a ahorrar agua en jardinería.", "respuesta": True}
]

# Barajar preguntas
random.shuffle(preguntas_vf)

# ---------------- FUNCIÓN PARA MOSTRAR PREGUNTA ----------------

def mostrar_pregunta():
    pregunta_actual = preguntas_vf[st.session_state.index_vf]
    st.markdown(f"<h3 style='color:black'>{pregunta_actual['pregunta']}</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Verdadero"):
            verificar_respuesta(True)
    with col2:
        if st.button("❌ Falso"):
            verificar_respuesta(False)

# ---------------- VERIFICAR RESPUESTA ----------------

def verificar_respuesta(respuesta_usuario):
    correcta = preguntas_vf[st.session_state.index_vf]['respuesta']
    if respuesta_usuario == correcta:
        st.session_state.puntos_vf += 1
        st.success("¡Correcto!")
    else:
        st.error("Ups... Incorrecto.")
    st.session_state.index_vf += 1
    time.sleep(1)
    st.rerun()


# ---------------- MOSTRAR CRONÓMETRO ----------------

tiempo_transcurrido = int(time.time() - st.session_state.inicio_vf)
st.markdown(f"<h4 style='color:lightblue'>🕒 Tiempo: {tiempo_transcurrido} segundos</h4>", unsafe_allow_html=True)

# ---------------- MOSTRAR PUNTAJE Y PREGUNTAS ----------------

if st.session_state.index_vf < len(preguntas_vf):
    mostrar_pregunta()
else:
    st.balloons()
    st.markdown(f"<h2 style='color:lightgreen'>🎉 ¡Juego terminado!</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:black'>Puntuación final: {st.session_state.puntos_vf}/{len(preguntas_vf)}</h3>", unsafe_allow_html=True)

    if st.session_state.puntos_vf == len(preguntas_vf):
        st.success("🌟 ¡Eres un maestro del ahorro de agua!")
    elif st.session_state.puntos_vf >= 3:
        st.info("💧 ¡Buen trabajo! Pero aún puedes mejorar.")
    else:
        st.warning("🚿 ¡Sigue aprendiendo para salvar el agua!")

    if st.button("🔁 Volver a jugar"):
        st.session_state.puntos_vf = 0
        st.session_state.index_vf = 0
        st.session_state.inicio_vf = time.time()
        st.rerun()


