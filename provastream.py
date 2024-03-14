import streamlit as st
import pandas as pd

# Datos de muestra para el DataFrame
data = {
    'Nombre': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Edad': [23, 34, 45, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid']
}
df = pd.DataFrame(data)

# Configura la página para usar un diseño más amplio
st.set_page_config(layout="wide")

# Crea columnas para las cajas de selección
col1, col2,col3= st.columns([1, 8, 1])

# Caja de selección para 'Nombre'
with col2:
    nombre_seleccionado = st.selectbox('Selecciona un nombre:', df['Nombre'].unique())
    ciudad_seleccionada = st.selectbox('Selecciona una ciudad:', df['Ciudad'].unique())

    
    # Filtrar el DataFrame según las selecciones
    df_filtrado = df[(df['Nombre'] == nombre_seleccionado) | (df['Ciudad'] == ciudad_seleccionada)]

    st.write("DataFrame Filtrado:")
    with st.container():
        st.dataframe(df_filtrado,use_container_width=True)

# Caja de selección para 'Ciudad'



# Mostrar el DataFrame filtrado en un contenedor

# Usar dos columnas para el DataFrame filtrado; se puede ajustar el tamaño relativo si es necesario
col_df1, col_df2 = st.columns(2)

# Mostrar el DataFrame filtrado en un contenedor que abarque dos columnas


