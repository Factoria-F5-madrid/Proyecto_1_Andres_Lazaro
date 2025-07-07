import streamlit as st
from core import Taximetro

st.set_page_config(page_title="Taxímetro F5", page_icon="🚕")
st.title("🚕 Taxímetro en Python - F5")

# Inicializar o recuperar el taxímetro desde session_state
if "taximetro" not in st.session_state:
    st.session_state.taximetro = Taximetro()

taxi = st.session_state.taximetro

# Configuración tarifas (solo si no hay viaje activo)
if not taxi.trip_active:
    st.subheader("⚙️ Configuración de tarifas")
    use_custom_prices = st.radio("¿Deseas configurar los precios manualmente?", 
                                ["No (usar valores predeterminados)", "Sí (ingresar manualmente)"])

    if use_custom_prices == "Sí (ingresar manualmente)":
        taxi.stop_rate = st.number_input("💵 Precio por segundo detenido:", min_value=0.0, value=taxi.stop_rate, step=0.01)
        taxi.move_rate = st.number_input("💰 Precio por segundo en movimiento:", min_value=0.0, value=taxi.move_rate, step=0.01)

# Botones para controlar el viaje
col1, col2, col3 = st.columns(3)

if col1.button("▶️ Iniciar") and not taxi.trip_active:
    taxi.start_trip()
    st.success("🚦 Viaje iniciado")

if col2.button("🛑 Detener") and taxi.trip_active:
    taxi.change_state("stop")
    st.info("🛑 Vehículo detenido")

if col3.button("🚗 Mover") and taxi.trip_active:
    taxi.change_state("moving")
    st.info("🚗 Vehículo en movimiento")

# Finalizar viaje y mostrar resumen
if st.button("✅ Finalizar viaje") and taxi.trip_active:
    resumen = taxi.stop_trip()
    st.subheader("🧾 Resumen del viaje:")
    st.write(f"⏱ Tiempo detenido: {resumen['stop_time']:.1f} segundos")
    st.write(f"🚙 Tiempo en movimiento: {resumen['moving_time']:.1f} segundos")
    st.write(f"💰 Total a pagar: **${resumen['fare']:.2f}**")

# Mostrar estado actual 
if taxi.trip_active:
    st.markdown(f"🟡 Estado actual: **{taxi.state.upper()}**")
    elapsed = taxi.elapsed_in_state()
    
