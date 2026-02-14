import streamlit as st

# Secciones
from vistas.home import pagina_home
from vistas.tareas import pagina_tareas
from vistas.administrar import administrar

def main():
    st.set_page_config("App Lista de Tareas")
    st.logo("imagenes/logo.png",icon_image="imagenes/logo_1.png")
    with st.sidebar:
        st.title("App Lista de Tareas")
        menu = ["Home","Tareas","Administrar","Acerca de"]
        seleccion = st.selectbox("Menú",menu)

    if seleccion == "Home":
        # st.subheader("Sección de Home")
        pagina_home()
    elif seleccion == "Tareas":
        #st.subheader("Sección de Tareas")
        pagina_tareas()
    elif seleccion == "Administrar":
        administrar()
    elif seleccion == "Acerca de":
        st.subheader("Acerca de...")
main()