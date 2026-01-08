import streamlit as st
import requests
import pandas as pd

# URL de la API (Nombre del servicio en Docker)
API_URL = "http://api:8000"

st.set_page_config(page_title="Inventario Docker", layout="wide")

st.title("Sistema de Gestión de Inventario")

# --- SECCIÓN DE CARGA DE DATOS (AHORA EN EL CENTRO) ---
# Usamos un 'expander' para que el formulario sea visible pero ordenado
with st.expander(" Agregar Nuevo Producto (Clic para desplegar)", expanded=True):
    with st.form("add_product_form"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre del Producto")
            precio = st.number_input("Precio ($)", min_value=0.0, step=0.01)
        with col2:
            desc = st.text_input("Descripción Corta")
            stock = st.number_input("Stock Inicial", min_value=0, step=1)
        
        submitted = st.form_submit_button("💾 Guardar en Base de Datos")
        
        if submitted:
            payload = {
                "nombre": nombre,
                "descripcion": desc,
                "precio": precio,
                "stock": stock
            }
            try:
                # Enviamos los datos a la API (Backend)
                response = requests.post(f"{API_URL}/productos/", json=payload)
                if response.status_code == 200:
                    st.success(f"✅ Producto '{nombre}' guardado exitosamente!")
                else:
                    st.error(f"Error del servidor: {response.text}")
            except Exception as e:
                st.error(f" Error de conexión con la API: {e}")

st.markdown("---")

# --- SECCIÓN DE LISTADO ---
st.header("Inventario Actual")

col_refresh, col_space = st.columns([1, 6])
with col_refresh:
    if st.button("Refrescar Datos"):
        st.rerun()

try:
    # Solicitamos los datos a la API
    response = requests.get(f"{API_URL}/productos/")
    if response.status_code == 200:
        productos = response.json()
        
        if productos:
            df = pd.DataFrame(productos)
            # Reordenamos las columnas si existen
            cols_to_show = ["id", "nombre", "descripcion", "precio", "stock"]
            # Filtramos solo las columnas que realmente llegaron para evitar errores
            cols_existentes = [c for c in cols_to_show if c in df.columns]
            df = df[cols_existentes]
            
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "precio": st.column_config.NumberColumn(format="$%.2f"),
                    "stock": st.column_config.NumberColumn(format="%d u."),
                    "id": st.column_config.NumberColumn(format="#%d")
                }
            )
            
            # Métricas rápidas
            m1, m2 = st.columns(2)
            m1.metric("Total de Ítems", len(df))
            if "precio" in df.columns and "stock" in df.columns:
                m2.metric("Valor Total del Inventario", f"${(df['precio'] * df['stock']).sum():,.2f}")
            
        else:
            st.info("La base de datos está vacía. ¡Usa el formulario de arriba para agregar tu primer producto!")
    else:
        st.error(f"Error al obtener datos: {response.status_code}")

except Exception as e:
    st.warning("No se puede conectar con el Backend.")
    st.info("Asegúrate de que el contenedor 'api' esté corriendo y que no haya errores en los logs.")