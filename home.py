import streamlit as st
import os
import random
from PIL import Image

st.set_page_config(page_title="Inicio - Waving", layout="centered")

st.title("💧 Bienvenido a Waving")
st.subheader("Bienvenido a nuestra app para salvar el planeta, una gota a la vez. 🌍")


# Cargar imágenes de la carpeta
carpeta = "imagenes_inicio"
imagenes = [img for img in os.listdir(carpeta) if img.endswith((".png", ".jpg", ".jpeg"))]

# Elegir una imagen aleatoria
imagen_seleccionada = random.choice(imagenes)
ruta_imagen = os.path.join(carpeta, imagen_seleccionada)

# Mostrar la imagen
st.image(Image.open(ruta_imagen), use_container_width=True, caption="Reflexiona sobre el uso del agua")

# Mensaje aleatorio opcional (puedes añadir más)
mensajes = [
    "Una ducha de 10 minutos consume más de 100 litros de agua.",
    "Más de 1.000 millones de personas no tienen acceso a agua potable.",
    "El 70% del agua dulce se usa en la agricultura.",
    "Cierra el grifo al lavarte los dientes y ahorrarás hasta 30 litros al día."
]

st.info(random.choice(mensajes))
