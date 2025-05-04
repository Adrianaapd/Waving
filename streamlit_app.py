import streamlit as st
import os
import random
from PIL import Image


#definimos nuestro logo


sidebar_logo = "Diseño sin título (2).jpg" 
main_body_logo = "Diseño sin título (2).jpg" 

st.logo(sidebar_logo, icon_image=main_body_logo)

home  =st.Page("home.py", title="Inicio", icon=":material/home:")
perfil = st.Page("perfil.py", title="Perfil", icon=":material/face:")
objetivos = st.Page("objetivos.py", title="Objetivos", icon=":material/new_releases:")
chat =st.Page("chat.py", title="Chat", icon=":material/chat:")
juego =st.Page("juegos.py", title="Juegos", icon=":material/quiz:")
pg = st.navigation([home,perfil,objetivos,juego,chat])
pg.run()




# Cargar imágenes de la carpeta
carpeta = "imagenes_inicio"
imagenes = [img for img in os.listdir(carpeta) if img.endswith((".png", ".jpg", ".jpeg"))]

# Elegir una imagen aleatoria

# Mostrar la imagen

# Mensaje aleatorio opcional (puedes añadir más)
mensajes = [
    "Una ducha de 10 minutos consume más de 100 litros de agua.",
    "Más de 1.000 millones de personas no tienen acceso a agua potable.",
    "El 70% del agua dulce se usa en la agricultura.",
    "Cierra el grifo al lavarte los dientes y ahorrarás hasta 30 litros al día."
]

st.info(random.choice(mensajes))

