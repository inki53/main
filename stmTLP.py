import sqlite3
import streamlit as st
import pandas as pd

#streamlit run C:\temp\streamlitTLP\stmTLP.py 
#.\stremlitenv\Scripts\activate.bat stremlitenv         Activate Environment

st.set_page_config(layout="wide")




try:
    # Conectar a la base de datos, si no existe se creará
    conn = sqlite3.connect('TLP4.db')
    print('Hola')
    # Crear un objeto cursor para ejecutar sentencias SQL
    cur = conn.cursor()
    cur.execute('SELECT * From Bloques3 ORDER BY Bloque')
except sqlite3.Error as e:
    print('error ',e)
# Recuperar todos los resultados

resultados = [list(row) for row in cur.fetchall()]

# Cerrar la conexión a la base de datos
conn.close()

# Ahora 'resultados' contiene los resultados de la consulta como una lista de listas

df= pd.DataFrame(resultados)
df.columns = ['Id', 'Bloque','Acciones','Descripcion']

col1, col2,col3= st.columns([1, 8, 1])

with col1:


    htmltext= """ <select name='select'>
            <option value='value1'>Value 1</option>
            <option value='value2' selected>Value 2</option>
            <option value='value3'>Value 3</option>
    </select>   """
st.components.v1.html(htmltext, width=None, height=None, scrolling=False)

with col2:

    htmltext= """ <select name='select'>
                <option value='value1'>Value 1</option>
                <option value='value2' selected>Value 2</option>
                <option value='value3'>Value 3</option>
        </select>   """
    st.components.v1.html(htmltext, width=None, height=None, scrolling=False)
    
    #st.title('ESTRATEGIAS TLP')
    # Usar Markdown con HTML para centrar el texto
    st.markdown("<h1 style='text-align: center'>ESTRATEGIAS TLP</h1>", unsafe_allow_html=True)

    Bloquelist= df['Bloque'].unique()
    Bloque_selected = st.selectbox('Selecciona un Bloque: ', Bloquelist)
    df_filtrado_bloque = df[df['Bloque'] ==Bloque_selected]

    Accioneslist=df_filtrado_bloque['Acciones'].unique()
    Acciones_selected=st.selectbox('Selecciona una Acción: ', Accioneslist)
    df_filtrado_acciones = df[df['Bloque'] ==Bloque_selected]


    # Filtrar el DataFrame basado en las selecciones y Seleccionar y mostrar solo ciertas columnas
    columnas_a_mostrar = ['Acciones','Descripcion']
    df_filtrado = df[(df['Bloque'] == Bloque_selected) & (df['Acciones'] == Acciones_selected)]
    df_filtrado_columnas=df_filtrado[columnas_a_mostrar]
    
    with st.container():
        st.dataframe(df_filtrado_columnas, hide_index=True,use_container_width=True)

