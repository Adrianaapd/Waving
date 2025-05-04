import streamlit as st
import openai

# Configurar la página
st.set_page_config(page_title="Chatbot Simple con IA", page_icon="🤖")

# Estilos CSS personalizados
st.markdown("""
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.assistant {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding-left: 1rem;
  padding-right: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# Título de la aplicación
st.title("Chatbot con IA")

# Inicializar el historial de chat en la sesión si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar para información y API key
with st.sidebar:
    st.title("Sobre este Chatbot")
    st.markdown("""
    Este es un chatbot simple creado con Streamlit y OpenAI.
    
    Para usarlo:
    1. Ingresa tu clave API de OpenAI abajo
    2. Escribe tu mensaje en el campo de texto
    3. Presiona Enter o haz clic en "Enviar"
    """)
    
    # Input para la API key
    openai_api_key = st.text_input("Ingresa tu clave API de OpenAI:", type="password")
    
    st.markdown("---")
    st.markdown("Creado con ❤️ usando Streamlit")

# Función para generar respuestas usando la API de OpenAI
def generate_response(prompt):
    try:
        if not openai_api_key:
            st.error("Por favor, ingresa tu clave API de OpenAI en el panel lateral.")
            return "Error: No se ha configurado la clave API."
        
        client = openai.OpenAI(api_key=openai_api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente amigable y útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Se produjo un error: {str(e)}"

# Función para mostrar mensajes del chat
def display_chat_message(role, content, avatar):
    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(avatar, width=60)
        with col2:
            st.markdown(f"**{role}**: {content}")

# Mostrar el historial de chat
if st.session_state.messages:
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        avatar = "https://api.dicebear.com/7.x/bottts/svg?seed=bot" if role == "Asistente" else "https://api.dicebear.com/7.x/personas/svg?seed=user"
        display_chat_message(role, content, avatar)

# Campo de entrada para el usuario
user_input = st.text_input("Escribe tu mensaje:", key="user_input", placeholder="¿En qué puedo ayudarte hoy?")

# Botón de envío
if st.button("Enviar") or (user_input and len(user_input.strip()) > 0):
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "Usuario", "content": user_input})
    
    # Generar respuesta
    response = generate_response(user_input)
    
    # Guardar respuesta del asistente
    st.session_state.messages.append({"role": "Asistente", "content": response})
    
    # Limpiar el campo de entrada y recargar
    st.session_state.user_input = ""
    st.experimental_rerun()
