import psycopg2
from psycopg2 import extras # Necesario para devolver Diccionarios

# 🚨 CAMBIAR ESTOS VALORES POR TUS PROPIAS CREDENCIALES
DB_HOST = "localhost"
DB_NAME = "universidad_db"
DB_USER = "postgres"
DB_PASS = "admin3000"

def obtener_conexion():
    """Configura y devuelve una conexión a la base de datos PostgreSQL."""
    # Usamos un bloque try/except para manejar fallos de conexión
    try:
        conexion = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conexion
    except psycopg2.OperationalError as e:
        print(f"Error de Conexión a PostgreSQL: {e}")
        # En una app real, aquí lanzaríamos una excepción más amigable
        return None

def ejecutar_consulta(sql, parametros=None):
    """
    Función genérica para ejecutar SQL (SELECT/INSERT/UPDATE/DELETE).
    Abre y cierra la conexión automáticamente.
    """
    if parametros is None:
        parametros = tuple() # Aseguramos que sea una tupla vacía si no hay parámetros

    try:
        with obtener_conexion() as conexion:
            # Usamos RealDictCursor (psycopg2) para devolver Diccionarios (ROW_FACTORY en SQLite)
            with conexion.cursor(cursor_factory=extras.RealDictCursor) as cursor:
                
                # Ejecutamos la consulta. psycopg2 usa %s como placeholder, no ?.
                cursor.execute(sql, parametros)
                
                # Guardamos cambios si no es un SELECT
                if not sql.strip().upper().startswith("SELECT"):
                    conexion.commit() 
                
                # Devolvemos los resultados (serán una lista de diccionarios)
                return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Error en la BBDD: {e}")
        return None