// La URL base de tu API Flask
const API_URL = 'http://127.0.0.1:5000/alumnos';
const tablaBody = document.getElementById('tabla-alumnos-body');

async function eliminarAlumno(id) {
    try {
        const respuesta = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE' 
        });

        if (respuesta.status === 204) {
            alert(`Alumno ID ${id} eliminado con éxito.`);
            cargarAlumnos();
        } else if (respuesta.status === 404) {
            alert("Error: Alumno no encontrado.");
        } else {
            throw new Error(`Error en el servidor: ${respuesta.status}`);
        }

    } catch (error) {
        console.error("Error al eliminar:", error);
    }
}

function setupListeners() {
    tablaBody.addEventListener('click', (e) => {
        if (e.target.classList.contains('btn-eliminar')) {
            const id = e.target.getAttribute('data-id');
            if (confirm(`¿Estás seguro de eliminar al alumno con ID ${id}?`)) {
                eliminarAlumno(id);
            }
        }
    });
}

const formulario = document.getElementById('formulario-alumno');

async function manejarEnvio(event) {
    event.preventDefault(); 
    const nuevoAlumno = {
        nombre: document.getElementById('nombre').value,
        materia: document.getElementById('materia').value,
        nota: parseFloat(document.getElementById('nota').value)
    };

    try {
        const respuesta = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevoAlumno) 
        });
        
        const resultado = await respuesta.json();

        if (respuesta.status === 201) { 
            alert(resultado.mensaje);
            formulario.reset(); 
            cargarAlumnos(); 
        } else {
            alert(`Error: ${resultado.error || resultado.mensaje}`);
        }

    } catch (error) {
        console.error("Error al enviar el formulario:", error);
        alert("Error de conexión con el servidor.");
    }
}

formulario.addEventListener('submit', manejarEnvio); 

async function cargarAlumnos() {
    try {
        const respuesta = await fetch(API_URL);
        if (!respuesta.ok) {
            throw new Error(`Error HTTP: ${respuesta.status}`);
        }
        
        const alumnos = await respuesta.json();
        tablaBody.innerHTML = '';
        
        alumnos.forEach(alumno => {
            const fila = document.createElement('tr');
            fila.innerHTML = `
                <td>${alumno.id}</td>
                <td>${alumno.nombre}</td>
                <td>${alumno.materia}</td>
                <td>${alumno.nota}</td>
                <td><button class="btn-eliminar" data-id="${alumno.id}">Eliminar</button></td>
            `;
            tablaBody.appendChild(fila);
        });
        
    } catch (error) {
        console.error("Error al cargar los datos de la API:", error);
        tablaBody.innerHTML = '<tr><td colspan="5">Error al conectar con la API. Asegúrese de que el servidor Flask esté corriendo.</td></tr>';
    }
}
setupListeners();
cargarAlumnos();