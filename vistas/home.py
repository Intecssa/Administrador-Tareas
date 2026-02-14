import streamlit as st
from datos.base_datos import *
import pandas as pd


def pagina_home():
    st.header("Home")
    seleccion = st.sidebar.selectbox("Opciones", ["Mis tareas", "Buscar"])

    with st.expander("Ver todas las tareas"):
        resultado = ver_todas_tareas()
        df = pd.DataFrame(resultado, columns=[
                          "Realizador", "Nombre", "Estado", "Fecha de Vencimiento"])
        st.dataframe(df)

    if seleccion == "Mis tareas":
        st.subheader("Mis tareas")
        c1, c2 = st.columns([2, 3])
        with c1:
            st.info("Lista de tareas")
            lista = [i[0] for i in ver_tareas_nombre()]
            tarea_seleccionada = st.selectbox("Tareas", lista)
        with c2:
            st.info("Detalles")
            resultado_tarea = obtener_por_tarea(tarea_seleccionada)[0]
            print(resultado_tarea)
            realizador = resultado_tarea[0]
            nombre = resultado_tarea[1]
            estado = resultado_tarea[2]
            f_v = resultado_tarea[3]
            st.write(f"**Realizador:** {realizador}")
            st.write(f"**Nombre de tarea:** {nombre}")
            st.write(f"**Estado:** {estado}")
            st.write(f"**Fecha de vencimiento:** {f_v}")
    else:
        st.subheader("Buscar")
        busqueda = st.text_input("Buscar: ")
        modo = st.radio("Buscar tarea por: ",
                        ("Realizador", "Nombre de tarea"))
        if st.button("Buscar"):
            if modo == "Realizador":
                resultado_realizador = obtener_por_realizador(busqueda)
                st.write(resultado_realizador)
            else:
                resultado_busqueda_tarea = obtener_por_tarea(busqueda)
                st.write(resultado_busqueda_tarea)
