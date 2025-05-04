import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializamos Firebase (si aún no está inicializado)
if not firebase_admin._apps:
    cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "waving-000c",
  "private_key_id": "1506e3f50849d7bdcb3122b4effc35da6bd99559",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDlouZZaah93Lmy\nvFFGMbI5H7TyyW88rL388dkSVRSJSXdgz1mGsS7MWHzaDqAwvBBJY1B+yr4B3DSg\nd4IiQXq56uQScStY91cn/RDyoUpyr5gWTapw8vYYfqoGkJqsPvul5ioNq/9fGXpC\nMzkun/AUlcEltDcgfBBJO7Aa0c9532Df0VVjwG7T675GCqdJdyr4kLuHXcSr2Ji4\nkgq5K4RA+a0/leMkmQgZduMNiPYSriGJyBmI3qS7iQygGRtlP33kkCsL5BcC9AKL\nVFzT0PawXN3st4pmc1lXQ4DmSnZA2FaZmBakrTyZWZcXNMdT3DBXJW6M+WHN+sYk\nmMB3WtgDAgMBAAECggEALcbmBY//AywjpqJMz2HrxeBwuW93adCDxS9PFwz33ZBU\nKGvdTHD4w8qmBPAideSfmImgS85Nx2Am65A3VG3aMcLF+Xku63rPGI0lukB171va\nxSNxZTfB4EsryMg91TVvA/jYjEYrz8Dr8tN0RDuk5+2chdAhpyukMX0hE4+cvQ3u\ndy5YhTWY0hou2zKcX8mg3FgNLu8WaUpohS1OOWAY1aLHMAAzv3kFtK7aF075H7Io\njBow/e0qHM9hM0X0mKG4izNUYuTK6Ve6nVrIYgZEtdc6jqnwHSjc0jSyfQoJqs/s\na7EOwJVO0s+Ez26dq6FfmBBmU8T8bRTIYWRTLY57TQKBgQD4XSJX6owJ2IsQXL7I\nreGU+STdT+EhMHu05R2y4e3S5oo0ZQGrzobFU/14ILiH3G6JDw6V9+mbw2QZTwAl\nSs1bnpNTeVD18hSygpvTTwrMtUNSCxPbUc2CPH07Kjbd+DBSzJxKLaves2X5qw2e\nDV4UmlaCpDQRQmJYIvysrv6KJwKBgQDsslyyVcPAY50XgHQYzB8NZqPjzTeoOe24\njvGTx1LP6sLGNbLCkM/mCJsdqJKykOjLX12A3BxuISMtSS2T8ybHDM1IeZ3rig4s\n1HFzi+nclABeZL2LQkkEyghX3YPZ3xsIj2CHQJQszOmFZl0z1RDK8r5vM+vsRCDI\naiK5Oe44xQKBgQCrcOa/F1nZhg/gmJTdxCGeiyjmWDiIh4YtRabtj0Vyus8WAc9Y\ngHTJjAPAw519syzeEXW5EevBKOxVCBKKq4r8PodmLK01SQj+fGgCQmKrEkjJPnpT\nf7FDwGuVxrsfGC6LSVBtZ/9m+CFhabE5s/KIeE1VWvHSJCfsvSH8NcPhKwKBgD6L\n617ctvuR1yMsuIEM/2+lHc3Gntx/YkgQzdmFJGb43DtQWUp8xdM9lu/BafJxxHJp\nYuX4RDL94rPG0Jp1+FtFEMIEESz6sEA8azZjVIsLOQW4jTXNcEopsQa27G6YPCaI\n7LMQ55bnFxY/NIXL2cInXxc3mzI11ovfMAnOOxsZAoGBAIf9/vmOuBiBi1Z9yB5I\nc0f4k77J4Tszhnr/CCxUIQb2rdEYSTopmtImckfjnNebvO3VZOPedwL2WVtxnLP+\nkw6B+hWw+jAIPk3Zpk3JHZeOf01GODfX/J9/gz3VYV/VhHzC3H3d/5ZSELOpU2pv\nrWGGXUGdiJ+PoHB6f+Q7nw46\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@waving-000c.iam.gserviceaccount.com",
  "client_id": "102032473827559384613",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40waving-000c.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)

    firebase_admin.initialize_app(cred)

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
else:
    # Si no existe, inicializamos los datos del perfil
    st.session_state.puntuacion = 0
    st.session_state.objetivos = {}

# Si no existe la puntuación de los juegos, inicialízala
if "puntuacion_juegos" not in st.session_state:
    st.session_state.puntuacion_juegos = 0  # Empezamos con puntuación de 0

# Mostrar la puntuación de los objetivos
puntuacion_total = st.session_state.puntuacion + st.session_state.puntuacion_juegos

# Mostrar la puntuación total combinada en el perfil
st.title("Perfil del Usuario")
st.write(f"**Puntuación Total**: 🌟 {puntuacion_total} puntos")

# Aquí podrías añadir más información sobre el perfil, como nombre, correo, etc.
st.write(f"**Nombre de Usuario:** {perfil.get('nombre', 'No disponible')}")
st.write(f"**Correo:** {perfil.get('correo', 'No disponible')}")


# Aquí se pueden actualizar los datos del perfil, como nombre o correo.
nombre_usuario = st.text_input("Nombre de Usuario", value=perfil.get("nombre", ""))
correo_usuario = st.text_input("Correo Electrónico", value=perfil.get("correo", ""))

# Mostrar y actualizar la puntuación de los objetivos
st.write(f"**Puntuación en los objetivos:** {st.session_state.puntuacion}")
st.write(f"**Puntuación en los juegos:** {st.session_state.puntuacion_juegos}")

# Guardar el progreso (si cambia)
if st.button("Guardar progreso"):
    # Guardar la puntuación total combinada (juegos + objetivos) y los datos del perfil en Firebase
    datos_perfil = {
        "nombre": nombre_usuario,
        "correo": correo_usuario,
        "puntuacion": puntuacion_total,
        "objetivos": st.session_state.objetivos
    }
    guardar_perfil(usuario_id, datos_perfil)
    st.success("Progreso guardado correctamente.")

# --- CALCULADORA MEJORADA --- (Si deseas dejar la calculadora aquí)
st.subheader("🧮 Calculadora de consumo de agua")

opciones = {
    "Ducha (10 L/min)": 10,
    "Lavavajillas (12 L/uso)": 12,
    "Lavadora (50 L/uso)": 50,
    "Grifo abierto (9 L/min)": 9,
    "Manguera (15 L/min)": 15
}

fuente = st.selectbox("Selecciona una fuente de consumo de agua:", list(opciones.keys()))
cantidad = st.number_input("¿Cuántos minutos o usos hiciste?", min_value=0)

if st.button("Calcular consumo"):
    litros = opciones[fuente] * cantidad
    cubos = litros / 10
    piscinas = litros / 30000

    st.success(f"""
    💧 **Consumo estimado**:  
    - {litros:.1f} litros  
    - {cubos:.1f} cubos de agua (10 L c/u)  
    - {piscinas:.5f} piscinas olímpicas (30.000 L c/u)
    """)

st.divider()

# --- TEMPORIZADOR EN SEGUNDO PLANO --- (Si lo deseas dejar aquí también)
from datetime import datetime, timedelta

# Inicializar estado si no existe
if "temporizador_activo" not in st.session_state:
    st.session_state.temporizador_activo = False
if "fin_temporizador" not in st.session_state:
    st.session_state.fin_temporizador = None

# Iniciar temporizador
if not st.session_state.temporizador_activo:
    duracion_min = st.number_input("Duración del temporizador (min):", min_value=1, max_value=30, value=5)
    if st.button("Iniciar temporizador"):
        st.session_state.fin_temporizador = datetime.now() + timedelta(minutes=duracion_min)
        st.session_state.temporizador_activo = True
        st.success("🚿 Temporizador iniciado. Puedes seguir navegando.")

# Mostrar tiempo restante
if st.session_state.temporizador_activo:
    tiempo_restante = st.session_state.fin_temporizador - datetime.now()
    if tiempo_restante.total_seconds() > 0:
        minutos = int(tiempo_restante.total_seconds()) // 60
        segundos = int(tiempo_restante.total_seconds()) % 60
        st.info(f"⏳ Tiempo restante: {minutos:02d}:{segundos:02d}")
        st.button("🔁 Actualizar estado")  # para refrescar manualmente
    else:
        st.success("✅ ¡Tiempo terminado! ¡Buen trabajo ahorrando agua!")
        st.session_state.temporizador_activo = False
        st.session_state.fin_temporizador = None
