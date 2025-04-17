# 💈 Juancho Barber's API

Sistema de gestión de reservas para una barbería, construido con **FastAPI**. Este sistema permite gestionar reservas de citas, visualizarlas, y exportarlas a un archivo CSV. Ideal para practicar la creación de APIs y gestión de datos sencillos.

---

## Índice

- [Características](#🚀-características)
- [Tecnologías utilizadas](#🧠-tecnologías-utilizadas)
- [Estructura del proyecto](#📁-estructura-del-proyecto)
- [Instalación y ejecución](#⚙️-instalación-y-ejecución)
- [Endpoints disponibles](#🧪-endpoints-disponibles)
- [Notas](#🗒️-notas)
- [Contribuciones](#🧑‍💻-contribuciones)

---

## 🚀 Características

- **Crear nuevas reservas** con validación de fecha, hora y servicio.
- **Consultar todas las reservas** o filtrarlas por fecha.
- **Cancelar reservas** por nombre y fecha.
- **Exportar reservas** a un archivo `.csv` para su almacenamiento.
- Documentación interactiva disponible en **Swagger** en `/docs`.

---

## 🧠 Tecnologías utilizadas

- 🐍 **Python 3.11+**
- ⚡ **FastAPI**
- 🔍 **Uvicorn** (servidor ASGI)
- 📄 **CSV** (persistencia de datos)
- 🧪 **Pydantic** (validación de datos)
- 🔒 **CORS** (para interacción frontend)

---

## 📁 Estructura del proyecto
    ```
    barber-shop-api/
    ├── backend/
    │   ├── main.py               # Archivo principal con la lógica de FastAPI
    │   ├── crud.py               # Funciones para CRUD de reservas
    │   ├── models.py             # Modelos de datos (Pydantic)
    │   ├── utils.py              # Funciones auxiliares (validaciones, exportación)
    │   ├── requirements.txt      # Dependencias del proyecto
    ├── reservas.csv              # Archivo generado/exportado con las reservas
    └── README.md                 # Documentación del proyecto
    ```

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/moicanbas/barber-shop-api.git

cd barber-shop-api
```

2. **Crear un entorno virtual (opcional, pero recomendado)**
```bash
python -m venv venv

source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar las dependencias**
```bash
pip install -r requirements.txt
```
4. **Ejecutar el servidor**
```bash
uvicorn main:app --reload
```

5. **Abrir la aplicación**
Accede a la API y su documentación interactiva en http://localhost:8000/docs

## 🧪 Endpoints disponibles

### 1. Registrar una nueva reserva
- **Método:** `POST`
- **URL:** `/reservas/`
- **Descripción:** Crea una nueva reserva de cliente en la barbería.
- **Cuerpo de la solicitud (JSON):**
```json
{
    "nombre": "Juan Pérez",
    "fecha": "12/12/2025",
    "hora": "10:00",
    "servicio": "corte"
}
```
- **Respuesta exitosa (201):**
```json
{
    "mensaje": "Reserva creada exitosamente."
}
```

### 2. Ver todas las reservas
- **Método:** `GET`

- **URL:** `/reservas/`

- **Descripción:** Obtiene todas las reservas registradas en el sistema.

- **Respuesta (200):**
```json
[
  {
    "nombre": "Juan Pérez",
    "fecha": "12/12/2025",
    "hora": "10:00",
    "servicio": "corte"
  },
  {
    "nombre": "Ana Gómez",
    "fecha": "12/12/2025",
    "hora": "11:00",
    "servicio": "barba"
  }
]
```

### 3. Consultar reservas por fecha
- **Método:** `GET`

- **URL:** `/reservas/{fecha}`

- **Descripción:** Obtiene las reservas para una fecha específica.

- **Parámetros de la URL:**

    - `fecha`: Fecha en formato `DD/MM/AAAA`.

- **Respuesta (200):**
```json
[
  {
    "nombre": "Juan Pérez",
    "fecha": "12/12/2025",
    "hora": "10:00",
    "servicio": "corte"
  }
]
```

### 4. Cancelar una reserva
- **Método:** `DELETE`

- **URL:** `/reservas/`

- **Descripción:** Cancela una reserva por nombre y fecha.

- **Cuerpo de la solicitud (JSON):**
```json
{
  "nombre": "Juan Pérez",
  "fecha": "12/12/2025"
}
```
- **Respuesta exitosa (200):**
```json
{
  "mensaje": "Reserva cancelada exitosamente."
}
```

### 5. Exportar todas las reservas a un archivo CSV
- **Método:** `GET`

- **URL:** `/reservas/exportar/`

- **Descripción:** Exporta todas las reservas a un archivo reservas.csv.

- **Respuesta exitosa (200):**

    - El archivo CSV será generado y descargado.

    - No hay respuesta en el cuerpo de la solicitud.

## 🗒️ Notas:
- Todos los datos se almacenan en un archivo CSV (reservas.csv) en el servidor.

- La validación de entradas está implementada para asegurar que las reservas no se superpongan en el mismo horario.

## 🧑‍💻 Contribuciones
Este proyecto fue diseñado con fines educativos y de práctica. Puedes contribuir mediante pull requests o issues para mejoras, correcciones o nuevas características.

## 🧔 Autor
Desarrollado por *El curioso Dev*