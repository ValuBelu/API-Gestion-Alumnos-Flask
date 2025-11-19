import sqlite3

DATABASE_NAME = "universidad.db"

def obtener_conexion():
    """
    Configura el formato de los datos.
    Devuelve una conexión a la base de datos.
    """
    conexion = sqlite3.connect(DATABASE_NAME)
    conexion.row_factory = sqlite3.Row
    return conexion

def ejecutar_consulta(sql, parametros=()):
    """
    Permite ejecutar INSERT/UPDATE/DELETE/SELECT.
    Abre y cierra la conexión automáticamente.
    """
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, parametros)
            if not sql.strip().upper().startswith("SELECT"):
                conexion.commit() 
            return cursor.fetchall() #Los resultados vuelven en una lista de diccionarios
    except sqlite3.Error as e:
        print(f"Error en la BBDD: {e}")
        return None