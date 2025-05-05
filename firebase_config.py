import firebase_admin
from firebase_admin import credentials, firestore

# Inicializamos Firebase (si aún no está inicializado)
# Verificamos si ya se ha inicializado la app de Firebase
if not firebase_admin._apps:
    # Si no está inicializada, lo hacemos con las credenciales
    cred = credentials.Certificate('.secrets/waving-000c-firebase-adminsdk-fbsvc-970bb4c6d4.json')  # Reemplaza con la ruta de tu archivo de credenciales
    firebase_admin.initialize_app(cred)
else:
    # Si ya está inicializada, no la volvemos a inicializar
    app = firebase_admin.get_app()

# Conectamos a Firestore
db = firestore.client()
