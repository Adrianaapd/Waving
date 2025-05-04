import streamlit as st
import random
from datetime import datetime, timedelta

import streamlit as st

# Si no existe la puntuación de los juegos, inicialízala
if "puntuacion_juegos" not in st.session_state:
    st.session_state.puntuacion_juegos = 0  # Empezamos con puntuación de 0

# Ejemplo de un juego (quiz, verdadero o falso, etc.)
# Simularemos que el usuario obtiene 10 puntos por acertar en el juego.
puntos_juego = 10  # Esto lo tendrías que actualizar con la lógica de tu juego

# Al final del juego, sumamos la puntuación obtenida al total de los juegos
st.session_state.puntuacion_juegos += puntos_juego

# Mostrar la puntuación del juego
st.write(f"Puntuación en los juegos: {st.session_state.puntuacion_juegos}")
# Inicializamos las variables de puntuación
if "puntuacion_juegos" not in st.session_state:
    st.session_state.puntuacion_juegos = 0

# --- JUEGO DE QUIZ ---
st.title("Juego de Quiz - Consumo de Agua")
st.write("Responde correctamente las siguientes preguntas para ganar puntos.")

# Lista de preguntas y respuestas correctas
preguntas = [
    {"pregunta": "¿Cuánto tiempo en minutos se recomienda que dure una ducha para ahorrar agua?", "opciones": ["5 minutos", "10 minutos", "15 minutos"], "respuesta_correcta": "5 minutos"},
    {"pregunta": "¿Qué dispositivo consume más agua en un hogar promedio?", "opciones": ["Ducha", "Lavadora", "Lavavajillas"], "respuesta_correcta": "Lavadora"},
    {"pregunta": "¿Cuántos litros de agua consume una manguera por minuto?", "opciones": ["10L", "15L", "20L"], "respuesta_correcta": "15L"}
]

# Variable para el puntaje del quiz
puntaje_quiz = 0

# Iterar sobre las preguntas y mostrar las opciones
for pregunta in preguntas:
    respuesta = st.radio(pregunta["pregunta"], pregunta["opciones"], key=pregunta["pregunta"])
    
    if respuesta == pregunta["respuesta_correcta"]:
        puntaje_quiz += 10
        st.success("¡Respuesta correcta! +10 puntos")
    elif respuesta:
        st.error("Respuesta incorrecta.")

# Mostrar puntuación del quiz
st.write(f"**Puntuación total en el Quiz:** 🌟 {puntaje_quiz} puntos")

# Botón para guardar progreso del quiz
if st.button("Guardar progreso del Quiz"):
    st.session_state.puntuacion_juegos += puntaje_quiz  # Sumar la puntuación del quiz al total
    st.success("Puntos del Quiz guardados correctamente.")

st.divider()

# --- JUEGO DE VERDADERO/FALSO ---
st.title("Juego de Verdadero o Falso")

# Lista de afirmaciones para el juego
afirmaciones = [
    {"afirmacion": "El agua potable es un recurso infinito.", "respuesta_correcta": "Falso"},
    {"afirmacion": "El grifo abierto consume más agua que la ducha.", "respuesta_correcta": "Falso"},
    {"afirmacion": "Una persona promedio consume 140 litros de agua al día.", "respuesta_correcta": "Verdadero"}
]

# Variable para la puntuación de verdadero/falso
puntaje_vf = 0

# Mostrar las afirmaciones y opciones
for afirmacion in afirmaciones:
    respuesta = st.radio(afirmacion["afirmacion"], ["Verdadero", "Falso"], key=afirmacion["afirmacion"])
    
    if respuesta == afirmacion["respuesta_correcta"]:
        puntaje_vf += 10
        st.success("¡Correcto! +10 puntos")
    elif respuesta:
        st.error("Incorrecto.")

# Mostrar puntuación de verdadero/falso
st.write(f"**Puntuación total en Verdadero/Falso:** 🌟 {puntaje_vf} puntos")

# Botón para guardar progreso de verdadero/falso
if st.button("Guardar progreso de Verdadero/Falso"):
    st.session_state.puntuacion_juegos += puntaje_vf  # Sumar la puntuación de verdadero/falso al total
    st.success("Puntos de Verdadero/Falso guardados correctamente.")

st.divider()

