import streamlit as st

st.set_page_config(page_title="Mis Objetivos de Agua", layout="centered")

st.title("🌱 Objetivos para reducir tu consumo de agua")
st.write("Selecciona lo que vas logrando cada día y haz pequeños cambios que marcan una gran diferencia.")

# --- Objetivos diarios
st.header("📅 Objetivos Diarios")
diarios = {
    "Ducha rápida (menos de 5 minutos)": False,
    "Cerrar el grifo al cepillarme los dientes": False,
    "Usar solo una carga completa en el lavavajillas": False,
    "No regar plantas en horas de sol fuerte": False
}

progreso_diario = 0
for objetivo in diarios:
    if st.checkbox(objetivo, key=objetivo):
        progreso_diario += 1

# --- Objetivos semanales
st.header("📆 Objetivos Semanales")
semanales = {
    "Revisar que no haya grifos goteando": False,
    "Usar lavadora solo con carga completa": False,
    "Recolectar agua de lluvia para regar (si es posible)": False,
    "Informar a mi familia sobre cómo ahorrar agua": False
}

progreso_semanal = 0
for objetivo in semanales:
    if st.checkbox(objetivo, key=objetivo + "_sem"):
        progreso_semanal += 1

# --- Objetivos mensuales
st.header("📅 Objetivos Mensuales")
mensuales = {
    "Instalar reductores de caudal en los grifos": False,
    "Analizar mi factura de agua y buscar formas de mejorar": False,
    "Crear un plan personal de ahorro de agua": False,
    "Desarrollar un hábito sostenible nuevo (a elegir)": False
}

progreso_mensual = 0
for objetivo in mensuales:
    if st.checkbox(objetivo, key=objetivo + "_mes"):
        progreso_mensual += 1

# --- Progreso total
total_objetivos = len(diarios) + len(semanales) + len(mensuales)
completados = progreso_diario + progreso_semanal + progreso_mensual

st.markdown("---")
st.subheader("📊 Tu progreso total")
st.progress(completados / total_objetivos)

st.success(f"Has completado {completados} de {total_objetivos} objetivos. ¡Sigue así!")

st.caption("Pequeños pasos diarios pueden tener un gran impacto en el planeta 🌍")

