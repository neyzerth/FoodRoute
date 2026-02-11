# FoodRoute - Tu Mapa de Sabores

> "La guía definitiva de comida callejera y rutas seguras."

[**Visitar Proyecto alojado en *PythonAnywhere***](https://neyzerth.pythonanywhere.com/map)

## 🚀 Cómo correrlo

Sigue estos pasos para ejecutar la aplicación localmente:

1.  **Clonar/Descargar** el repositorio.
2.  **Instalar dependencias** (asegúrate de tener Python instalado):
    ```bash
    pip install flask
    ```
3.  **Ejecutar el servidor**:
    ```bash
    cd sourcecode
    flask --app main run
    python main.py
    # O alternativamente:
    # python main.py
    ```
4.  **Abrir en el navegador**:
    Visita `http://127.0.0.1:5000` para ver la landing page.
    Visita `http://127.0.0.1:5000/map` para ir directo al mapa.

## 🛠 Stack Tecnológico

*   **Backend**: Flask (Python)
*   **Frontend**: HTML5, JavaScript
*   **Mapas**: Leaflet.js (OpenStreetMap)
*   **Estilos**: Tailwind CSS (CDN)

## 🎨 Justificación de Diseño

La interfaz ha sido diseñada priorizando la facilidad de uso y la accesibilidad, basándose en iteraciones previas:

*   **Identidad Visual (Actividad 1)**: Se eligió un tema claro y vibrante con acentos en naranja (`#FF6B00`) para evocar apetito y energía, alejándose de los mapas oscuros tradicionales. La Landing Page vende la idea de "aventura segura".
*   **Ergonomía Móvil (Actividad 2)**: Los controles de navegación (zoom) y pestañas se posicionaron en la zona inferior (Ley de Fitts). Esto permite que la aplicación sea totalmente operable con una sola mano en dispositivos móviles.
*   **Feedback de Estado (Actividad 3)**: Se implementó un sistema de "Toast" (notificaciones emergentes) para informar al usuario sobre procesos asíncronos (como guardar una ubicación). Esto reduce la incertidumbre y mejora la percepción de velocidad.
*   **Accesibilidad (Actividad 4)**: Se utilizaron etiquetas semánticas (`nav`, `main`, `aside`) y atributos ARIA (`aria-label`, `role="tab"`) para asegurar que la aplicación sea navegable por lectores de pantalla. Los estados de foco son claramente visibles.

## 🤖 Créditos a la IA

Este código fue co-creado con Gemini Canvas.

**Prompt principal:**
*"Vas a desarrollar la base de una aplicacion de Rutas y Mapas de la idea dada de "La Ruta del Antojo". Crea una Landing Page HTML para una app de mapas llamada FoodRoute. Debe tener un 'Hero' con una imagen de fondo de un mapa estilizado o topográfico, un título grande, y un botón CTA prominente que diga 'Explorar Mapa'. Usa Tailwind CSS. El diseño debe inspirar aventura/seguridad."*
