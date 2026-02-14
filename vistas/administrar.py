import streamlit as st

from datos.base_datos import *

import pandas as pd

import plotly.express as px
def administrar():
    st.header("Administrar")

    seleccion = st.sidebar.selectbox("Opciones",["Eliminar tarea","Analítica"])

    if seleccion =="Eliminar tarea":
        st.subheader("Eliminar tarea")
        df = pd.DataFrame(ver_todas_tareas(),columns=["Realizador","Nombre","Estado","Fecha de Vencimiento"])
        st.dataframe(df)
        lista = [i[0] for i in ver_tareas_nombre()]
        tarea_a_eliminar = st.selectbox("Tarea a eliminar: ",lista)
        if st.button("Eliminar"):
            st.warning("Eliminando tarea")
            eliminar_tarea(tarea_a_eliminar)
            st.info("Tarea eliminada")

        with st.expander("Base de datos actualizada"):
            df = pd.DataFrame(ver_todas_tareas(),columns=["Realizador","Nombre","Estado","Fecha de Vencimiento"])
            st.dataframe(df)

    else:
        st.subheader("Analítica")
        with st.expander("Ver todas las tareas"):
            df = pd.DataFrame(ver_todas_tareas(),columns=["Realizador","Nombre","Estado","Fecha de Vencimiento"])
            st.dataframe(df)
        with st.expander("Estado de tareas por realizador"):
            conteo_realizador = df["Realizador"].value_counts().to_frame()
            conteo_realizador = conteo_realizador.reset_index()
            st.dataframe(conteo_realizador)
            p1 = px.pie(conteo_realizador,names="Realizador",values="count")
            st.plotly_chart(p1)
        with st.expander("Estado de tareas por nombre"):
            conteo_tarea = df["Nombre"].value_counts().to_frame().reset_index()
            st.dataframe(conteo_tarea)
            p2 = px.pie(conteo_tarea, names="Nombre",values="count")
            st.plotly_chart(p2)

        