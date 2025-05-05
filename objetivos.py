import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta

# Inicializamos Firebase (si aún no está inicializado)
# Verificamos si ya se ha inicializado la app de Firebase
if not firebase_admin._apps:
    # Si no está inicializada, lo hacemos con las credenciales
    cred = credentials.Certificate('.secrets/waving-000c-firebase-adminsdk-fbsvc-bfbe3112b5.json')  # Reemplaza con la ruta de tu archivo de credenciales
    firebase_admin.initialize_app(cred)
else:
    # Si ya está inicializada, no la volvemos a inicializar
    app = firebase_admin.get_app()

# Conectamos a Firestore
db = firestore.client()

# Función para cargar los datos de perfil desde Firebase
def cargar_perfil(usuario_id):
    doc_ref = db.collection('usuarios').document(usuario_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

# Función para guardar datos del perfil en Firebase
def guardar_perfil(usuario_id, datos):
    db.collection('usuarios').document(usuario_id).set(datos, merge=True)

# Suponiendo que el usuario tiene un ID único (debes adaptar esto a tu sistema de autenticación)
usuario_id = "usuario_123"  # Este valor debe ser dinámico basado en el usuario autenticado

# Cargar los datos del perfil
perfil = cargar_perfil(usuario_id)

# Si el perfil existe en Firebase, lo cargamos en la sesión
if perfil:
    st.session_state.puntuacion = perfil.get("puntuacion", 0)
    st.session_state.objetivos = perfil.get("objetivos", {})
    st.session_state.nombre = perfil.get("nombre", "")
    st.session_state.correo = perfil.get("correo", "")
else:
    # Si no existe, inicializamos los datos del perfil
    st.session_state.puntuacion = 0
    st.session_state.objetivos = {}
    st.session_state.nombre = ""
    st.session_state.correo = ""

# Mostrar el formulario para que el usuario ingrese su nombre y correo
st.title("OBJETIVOS")
st.write("Poque cada pequeña gota cuenta")

# Campos de entrada para el nombre y correo
st.session_state.nombre = st.text_input("Nombre de usuario", value=st.session_state.nombre)
st.session_state.correo = st.text_input("Correo electrónico", value=st.session_state.correo)

# Mostrar la puntuación y los objetivos
st.write(f"Puntuación: {st.session_state.puntuacion}")

# Mostrar objetivos y permitir marcar progreso
st.subheader("Objetivos")

# Ejemplo de objetivos
objetivos = {
    "diarios": {
        "Ahorrar 10L de agua hoy": False,
        "No usar el lavavajillas más de 3 veces al día": False,
    },
    "semanales": {
        "Ahorrar 50L de agua esta semana": False,
        "No dejar el grifo abierto más de 15 minutos al día": False,
    },
    "mensuales": {
        "Ahorrar 200L de agua este mes": False,
        "Reducir el consumo de manguera en un 50%": False,
    }
}

# Mostrar los objetivos y permitir marcar los completados
for tipo, objetivos_lista in objetivos.items():
    st.subheader(tipo.capitalize())
    for objetivo, completado in objetivos_lista.items():
        objetivo_completado = st.checkbox(objetivo, value=completado, key=f"{tipo}_{objetivo}")
        if objetivo_completado:
            st.session_state.objetivos[objetivo] = True
            st.session_state.puntuacion += 10  # Incrementar la puntuación al completar el objetivo

# Botón para guardar la puntuación (si cambia algo)
if st.button("Guardar Progreso"):
    datos_perfil = {
        "nombre": st.session_state.nombre,
        "correo": st.session_state.correo,
        "puntuacion": st.session_state.puntuacion,
        "objetivos": st.session_state.objetivos
    }
    guardar_perfil(usuario_id, datos_perfil)
    st.success("Progreso guardado correctamente.")

# Mostrar la puntuación del usuario
st.write(f"**Puntuación total:** 🌟 {st.session_state.puntuacion} puntos")

# Opcional: Mostrar un mensaje de bienvenida y progreso
st.write("Tu progreso se guarda automáticamente.")
