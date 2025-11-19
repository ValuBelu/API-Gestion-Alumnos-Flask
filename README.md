# API REST de Gestión de Alumnos con Flask

## Resumen del Proyecto

Este proyecto es un servicio de Backend (API REST) desarrollado en Python con el framework Flask, utilizando SQLite como base de datos para persistencia. Demuestra un manejo del ciclo CRUD (Crear, Leer, Actualizar y Eliminar) y la integración asíncrona con un Frontend simple en HTML.

**Habilidades Expuestas:**
* **Backend:** Python, Flask, Modularización.
* **Base de Datos:** SQLite, Consultas SQL Seguras (Placeholders).
* **Arquitectura:** Diseño de Endpoints RESTful, manejo de peticiones HTTP (GET, POST, PUT, DELETE).
* **Frontend Integration:** Manejo de asincronía (JavaScript `fetch`) y resolución de problemas de CORS.

---

## ⚙️ Tecnologías

* **Lenguaje:** Python 3.x
* **Framework Web:** Flask
* **Base de Datos:** SQLite 3
* **Manejo de Dependencias:** `pip` / `venv`
* **Integración Web:** HTML / JavaScript ES6

---

## 🧭 Endpoints de la API

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **`GET`** | `/alumnos` | Lista todos los alumnos. |
| **`GET`** | `/alumnos/<id>` | Muestra un alumno específico. (Devuelve **404** si no existe). |
| **`POST`**| `/alumnos` | Crea un nuevo alumno. (Requiere JSON con `nombre` y `materia`. El campo `nota` es opcional y autocompleta con 0). |
| **`PUT`** | `/alumnos/<id>` | Modifica un alumno existente. (Devuelve **404** si no existe). |
| **`DELETE`**| `/alumnos/<id>` | Elimina un alumno. (Devuelve **404** si no existe). |

---

## Guía de Instalación y Uso

Para levantar la API y probar la interfaz web:

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/ValuBelu/API-Gestion-Alumnos-Flask
    cd API-Gestion-Alumnos-Flask
    ```

2.  **Crear y Activar el Entorno Virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Iniciar la API:**
    ```bash
    python web_app.py
    ```
    *(La API se ejecutará en `http://127.0.0.1:5000`)*

5.  **Probar la Interfaz:** Abre el archivo `index.html` en un navegador para interactuar con la API (agregar y eliminar alumnos).

---