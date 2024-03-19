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


#https://stackoverflow.com/questions/69492406/streamlit-how-to-display-buttons-in-a-single-line

import streamlit.components.v1 as components
#components.html(htmltext, width=None, height=None, scrolling=False)     Select Option

#st.title('ESTRATEGIAS TLP')
# Usar Markdown con HTML para centrar el texto
st.markdown("<h5 style='text-align: center'>ESTRATEGIAS TLP</h1>", unsafe_allow_html=True)
col1, col2,col3= st.columns([1, 8, 1])

Bloquelist= df['Bloque'].unique()
             
#with col2:

Bloque_selected = st.selectbox('Selecciona un Bloque: ',Bloquelist,key='Bloque')
df_filtrado_bloque = df[df['Bloque'] ==Bloque_selected]
Accioneslist=df_filtrado_bloque['Acciones'].unique()

#Con st.radio:

Acciones_selected= st.radio("Selecciona una Acción",Accioneslist,key='acciones',horizontal=True,label_visibility="collapsed")


df_filtrado_acciones = df[df['Bloque'] ==Bloque_selected]


# Filtrar el DataFrame basado en las selecciones y Seleccionar y mostrar solo ciertas columnas
columnas_a_mostrar = ['Acciones','Descripcion']
df_filtrado = df[(df['Bloque'] == Bloque_selected) & (df['Acciones'] == Acciones_selected)]
df_filtrado_columnas=df_filtrado[columnas_a_mostrar]
    
#with st.container():
st.dataframe(df_filtrado_columnas, hide_index=True,use_container_width=True)


_=""" with col1:


    #https://stackoverflow.com/questions/69492406/streamlit-how-to-display-buttons-in-a-single-line

    import streamlit.components.v1 as components
    #components.html(htmltext, width=None, height=None, scrolling=False)     Select Option

with col2:
   

    #st.title('ESTRATEGIAS TLP')
    # Usar Markdown con HTML para centrar el texto
    st.markdown("<h5 style='text-align: center'>ESTRATEGIAS TLP</h1>", unsafe_allow_html=True)

    Bloquelist= df['Bloque'].unique()
    Bloque_selected = st.selectbox('Selecciona un Bloque: ', Bloquelist)
    df_filtrado_bloque = df[df['Bloque'] ==Bloque_selected]

    Accioneslist=df_filtrado_bloque['Acciones'].unique()

    #Con st.radio:

    Acciones_selected= st.radio("Selecciona una Acción",
    Accioneslist,horizontal=True,label_visibility="collapsed")

    
    df_filtrado_acciones = df[df['Bloque'] ==Bloque_selected]


    # Filtrar el DataFrame basado en las selecciones y Seleccionar y mostrar solo ciertas columnas
    columnas_a_mostrar = ['Acciones','Descripcion']
    df_filtrado = df[(df['Bloque'] == Bloque_selected) & (df['Acciones'] == Acciones_selected)]
    df_filtrado_columnas=df_filtrado[columnas_a_mostrar]
    
    with st.container():
        st.dataframe(df_filtrado_columnas, hide_index=True,use_container_width=True) """