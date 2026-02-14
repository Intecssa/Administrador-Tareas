import sqlite3
import os
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data.db")

@st.cache_resource
def obtener_conexion():
    conexion = sqlite3.connect(db_path,check_same_thread=False)
    return conexion


def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tabla_tarea(realizador TEXT,nombre TEXT,estado TEXT,fecha_vencimiento DATE) ")

def ingresar_datos(realizador,nombre,estado,f_v):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tabla_tarea(realizador,nombre,estado,fecha_vencimiento) VALUES (?,?,?,?)",
                   (realizador,nombre,estado,f_v))
    conexion.commit()

#ingresar_datos("Mario","Nueva aplicación","Realizando","16/08/2024")
def ver_todas_tareas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tabla_tarea")
    datos = cursor.fetchall()

    return datos
#ver_todas_tareas()
def ver_tareas_nombre():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM tabla_tarea")
    datos = cursor.fetchall()

    return datos    
#ver_tareas_nombre()

def obtener_por_tarea(tarea):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM tabla_tarea WHERE nombre = '{tarea}'")
    datos = cursor.fetchall()
    return datos 

#obtener_por_tarea("Maquetado")

def obtener_por_realizador(realizador):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM tabla_tarea WHERE realizador = '{realizador}'")
    datos = cursor.fetchall()
    return datos 

# obtener_por_realizador("Mario")

def editar_tarea(realizador,nombre,estado,f_v,n_realizador,n_nombre,n_estado,n_f_v):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE tabla_tarea SET realizador=?,nombre=?,estado=?,fecha_vencimiento=? WHERE  realizador=? and nombre=? and estado=? and fecha_vencimiento=?",
                   (realizador,nombre,estado,f_v,n_realizador,n_nombre,n_estado,n_f_v))
    conexion.commit()
    datos = cursor.fetchall()
    return datos

# editar_tarea("Jose","Despliegue","Terminado","15/08/2024","Jose","Maquetado","Pendiente","15/08/2024")

def eliminar_tarea(nombre):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM tabla_tarea WHERE nombre = '{nombre}'")
    conexion.commit()

# eliminar_tarea("Despliegue")
# ver_todas_tareas()