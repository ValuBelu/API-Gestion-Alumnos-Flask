# API REST de Gestión de Alumnos

## Resumen del Proyecto

Este proyecto es un servicio de **Backend (API REST)** desarrollado en Python con el framework **Flask**, utilizando **PostgreSQL** como base de datos para la persistencia. La arquitectura maneja el ciclo **CRUD (Crear, Leer, Actualizar y Eliminar)** y cuenta con una integración asíncrona robusta con un Frontend simple en HTML.

**Habilidades Expuestas:**
* **Backend:** Python, Flask, Modularización.
* **Base de Datos:** **PostgreSQL**, Consultas SQL Seguras (`%s` Placeholders), y **Migración de BBDD industrial**. Originalmente este proyecto fue planteado en **SQLite**, pero fue migrado a **PostgreSQL**
* **Arquitectura:** Diseño de Endpoints RESTful, manejo de peticiones HTTP (GET, POST, PUT, DELETE).
* **Frontend Integration:** Manejo de asincronía (JavaScript `fetch`) y resolución de problemas de CORS.

---

## ⚙️ Tecnologías

* **Lenguaje:** Python 3.14.0
* **Framework Web:** Flask
* **Base de Datos:** **PostgreSQL**
* **Conector DB:** **Psycopg2**
* **Manejo de Dependencias:** `pip` / `venv`
* **Integración Web:** HTML / JavaScript ES6

---

## 🧭 Endpoints de la API

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **`GET`** | `/alumnos` | Lista todos los alumnos. |
| **`GET`** | `/alumnos/<id>` | Muestra un alumno específico. (Devuelve **404** si no existe). |
| **`POST`**| `/alumnos` | Crea un nuevo alumno. (Requiere JSON con `nombre` y `materia`). |
| **`PUT`** | `/alumnos/<id>` | Modifica un alumno existente. (Devuelve **404** si no existe). |
| **`DELETE`**| `/alumnos/<id>` | Elimina un alumno. (Devuelve **404** si no existe). |

---

## Guía de Instalación y Uso

### 1. Preparación del Entorno

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

### 2. Configuración de PostgreSQL

1.  Asegúrate de que tu servidor PostgreSQL esté corriendo.
2.  Crea una base de datos en tu servidor PostgreSQL llamada **`universidad_db`**.
3.  Abre el archivo **`database.py`** y actualiza las variables `DB_USER` y `DB_PASS` con tus credenciales de PostgreSQL.
4.  Crea la Tabla: Ejecuta la siguiente consulta SQL en tu `universidad_db` para inicializar la tabla:
    ```sql
    CREATE TABLE alumnos (
        id SERIAL PRIMARY KEY,
        nombre TEXT NOT NULL,
        materia TEXT NOT NULL,
        nota REAL
    );
    ```

### 3. Ejecución

1.  **Iniciar la API:**
    ```bash
    python web_app.py
    ```
2.  **Probar la Interfaz:** Abre el archivo `index.html` en un navegador para interactuar con la API (agregar y eliminar alumnos).

---