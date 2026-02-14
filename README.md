# App Lista de Tareas

Aplicación de gestión de tareas desarrollada con Python y Streamlit. Permite crear, leer, actualizar y eliminar tareas (CRUD), así como visualizar estadísticas básicas.

## Características

- **Home**: Visualización de todas las tareas y búsqueda por realizador o nombre de tarea.
- **Tareas**:
  - Añadir nuevas tareas con campos: Realizador, Nombre, Estado y Fecha de Vencimiento.
  - Editar tareas existentes.
- **Administrar**:
  - Eliminar tareas de la base de datos.
  - Analítica: Gráficos de pastel mostrando la distribución de tareas por realizador y por nombre.
- **Persistencia**: Utiliza SQLite para almacenar los datos localmente en `datos/data.db`.

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual (opcional pero recomendado).
3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando desde la raíz del proyecto:

```bash
streamlit run main.py
```

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación.
- `datos/`: Contiene la lógica de conexión a la base de datos (`base_datos.py`) y el archivo de base de datos SQLite.
- `vistas/`: Contiene los módulos para las diferentes páginas de la interfaz (`home.py`, `tareas.py`, `administrar.py`).
- `imagenes/`: Carpeta para recursos gráficos (logos).