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


    htmltext= """ <select class="selectpicker">
  <option>PWWPd</option>
  <option>Ketchup</option>
  <option>Relish</option>
</select>
"""

import streamlit.components.v1 as components
components.html(htmltext, width=None, height=None, scrolling=False)

with col2:

   

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

    opciones =Bloquelist # ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
    
    html_select = '<select name="opciones" id="opciones-select">\n'
    for opcion in opciones:
        print(opcion)
        html_select += '    <option value="{}">{}</option>\n'.format(opcion.lower().replace(' ', ''), opcion)
    html_select += '</select>'

    print(html_select)
    #width: 200px; /* Ancho del select */
    html_css="""<style>
    #opciones-select {
        background-color: #f0f0f0; /* Color de fondo */
        color: #333; /* Color del texto */
        padding: 10px; /* Espaciado interno */
        border: 2px solid #ccc; /* Borde del select */
        border-radius: 5px; /* Bordes redondeados */
        font-size: 16px; /* Tamaño del texto */
        width: 100%; /* Ancho del select */
        cursor: pointer; /* Cambiar el cursor a una mano al pasar sobre el select */
    }

    /* Cambiar la apariencia de las opciones al pasar el mouse */
    #opciones-select:hover {
        background-color: #e9e9e9;
    }

    /* Estilos para cuando el select está enfocado */
    #opciones-select:focus {
        outline: none; /* Eliminar el contorno predeterminado */
        border-color: #9ecaed;
        box-shadow: 0 0 10px #9ecaed;
    }
</style>
"""
   
    htmltext=html_select+html_css
    print(htmltext)
    st.components.v1.html(htmltext, width=None, height=None, scrolling=False)
    with st.container():
        st.dataframe(df_filtrado_columnas, hide_index=True,use_container_width=True)

