import streamlit as st
from datos.base_datos import *

def pagina_tareas():
    st.header("Tareas")
    crear_tabla()
    seleccion = st.sidebar.selectbox("Opciones",["Añadir tarea","Editar tarea"])

    if seleccion == "Añadir tarea":
        st.subheader("Añadir tarea")
        col1,col2 = st.columns(2)
        
        with col1:
            realizador = st.text_input("Realizador")
            nombre_tarea = st.text_area("Nombre de tarea: ")
        with col2:
            estado_tarea = st.selectbox("Estado: ",["Pendiente","Terminado","En proceso","Indefinido"])
            fecha_ven = st.date_input("Fecha de vencimiento: ")

        if st.button("Añadir tarea"):
            ingresar_datos(realizador,nombre_tarea,estado_tarea,fecha_ven)
            st.success(f"Añadido: {nombre_tarea}")
    else: 
        st.subheader("Editar tarea")
        lista = [i[0] for i in ver_tareas_nombre()]
        tarea_seleccionada = st.selectbox("Tareas",lista)
        tarea_resultante = obtener_por_tarea(tarea_seleccionada)[0]
        st.write(tarea_resultante)
        if tarea_resultante:
            realizador_r = tarea_resultante[0]
            nombre = tarea_resultante[1]
            estado = tarea_resultante[2]
            f_v = tarea_resultante[3]
        
            col1,col2 = st.columns(2)
        
            with col1:
                realizador = st.text_input("Realizador",realizador_r)
                nombre_tarea = st.text_area("Nombre de tarea: ",nombre)
            with col2:
                estado_tarea = st.selectbox(f"Estado: {estado}",["Pendiente","Terminado","En proceso","Indefinido"])
                fecha_ven = st.date_input(f"Fecha de vencimiento: {f_v}")

            if st.button("Actualizar"):
                editar_tarea(realizador,nombre_tarea,estado_tarea,fecha_ven,realizador_r,nombre,estado,f_v)
                st.success(f"Actualizado: {nombre}")
