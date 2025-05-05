import firebase_admin
from firebase_admin import credentials, firestore

# Verificamos si ya se ha inicializado la app de Firebase
if not firebase_admin._apps:
    # Si no está inicializada, lo hacemos con las credenciales
    cred = credentials.Certificate('.secrets/waving-000c-firebase-adminsdk-fbsvc-bfbe3112b5.json')  # Reemplaza con la ruta de tu archivo de credenciales
    firebase_admin.initialize_app(cred)
else:
    # Si ya está inicializada, no la volvemos a inicializar
    app = firebase_admin.get_app()

# Inicializamos la base de datos Firestore
db = firestore.client()
