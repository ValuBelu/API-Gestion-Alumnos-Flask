from flask import Flask, jsonify, request
from database import ejecutar_consulta

app = Flask(__name__)

@app.route('/')
def inicio():
    """Ruta de bienvenida."""
    return "<h1>Bienvenido a la API REST de la Universidad</h1>"

@app.route('/alumnos', methods=['GET', 'POST']) 
def alumnos():
    if request.method == 'GET':
        sql_select = "SELECT id, nombre, materia, nota FROM alumnos"
        alumnos_data = ejecutar_consulta(sql_select)
        alumnos_list = [dict(row) for row in alumnos_data]
        return jsonify(alumnos_list) 

    if request.method == 'POST':
        datos = request.get_json()
        if not datos or 'nombre' not in datos or 'materia' not in datos:
            return jsonify({"error": "Faltan campos requeridos (nombre y materia)"}), 400
        
        nota = datos.get('nota', 0.0)        
        parametros = (datos['nombre'], datos['materia'], nota)
        sql_insert = "INSERT INTO alumnos (nombre, materia, nota) VALUES (?, ?, ?)"
        ejecutar_consulta(sql_insert, parametros)
        return jsonify({"mensaje": "Alumno creado con éxito"}), 201
    
@app.route('/alumnos/<int:id_alumno>', methods=['GET'])
def obtener_alumno(id_alumno):
    """Busca un alumno por su ID."""
    sql_select = "SELECT id, nombre, materia, nota FROM alumnos WHERE id = ?"
    alumno_data = ejecutar_consulta(sql_select, (id_alumno,))

    if not alumno_data:
        return jsonify({"error": "Alumno no encontrado"}), 404

    alumno = dict(alumno_data[0]) 
    return jsonify(alumno)

@app.route('/alumnos/<int:id_alumno>', methods=['PUT'])
def modificar_alumno(id_alumno):
    """Busca un alumno por ID y actualiza sus datos con el JSON recibido."""
    #Verificar si el id_alumno existe 
    sql_check = "SELECT COUNT(*) FROM alumnos WHERE id = ?"
    resultado_check = ejecutar_consulta(sql_check, (id_alumno,))[0]['COUNT(*)']

    if resultado_check == 0:
        return jsonify({"error": f"Alumno con ID {id_alumno} no encontrado para actualizar."}), 404
    datos = request.get_json()

    if not datos or ('nombre' not in datos and 'materia' not in datos and 'nota' not in datos):
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

    campos = []
    valores = []

    if 'nombre' in datos:
        campos.append("nombre = ?")
        valores.append(datos['nombre'])
    if 'materia' in datos:
        campos.append("materia = ?")
        valores.append(datos['materia'])
    if 'nota' in datos:
        campos.append("nota = ?")
        valores.append(datos['nota'])

    sql_update = f"UPDATE alumnos SET {', '.join(campos)} WHERE id = ?"
    valores.append(id_alumno)
    ejecutar_consulta(sql_update, tuple(valores))

    return jsonify({"mensaje": f"Alumno con ID {id_alumno} actualizado con éxito"}), 200

@app.route('/alumnos/<int:id_alumno>', methods=['DELETE'])
def eliminar_alumno(id_alumno):
    """Elimina el registro del alumno según su ID."""
    sql_check = "SELECT COUNT(*) FROM alumnos WHERE id = ?"
    resultado_check = ejecutar_consulta(sql_check, (id_alumno,))[0]['COUNT(*)']

    if resultado_check == 0:
        return jsonify({"error": f"Alumno con ID {id_alumno} no encontrado para eliminar."}), 404
        
    sql_delete = "DELETE FROM alumnos WHERE id = ?"
    ejecutar_consulta(sql_delete, (id_alumno,)) 
    return jsonify({"mensaje": f"Alumno con ID {id_alumno} eliminado con éxito"}), 204

if __name__ == '__main__':
    app.run(debug=True)