# 📄 Módulo de Ubicación de Firmas E-digital (Frontend)

Una herramienta frontend ligera y robusta para la previsualización de documentos PDF y el posicionamiento visual de coordenadas de firmas electrónicas. Diseñada para integrarse mediante `iframes` con sistemas backend (ej. CodeIgniter, Laravel, Node).

## ✨ Características Principales

* **Renderizado de PDF Nativo:** Utiliza `PDF.js` para renderizar documentos de forma local en el navegador, garantizando privacidad y rapidez.
* **Smart Anchors (Anclaje Inteligente):** Escanea el texto del PDF y auto-posiciona las cajas de firma sobre palabras clave (`firma`, `rut`, `empleador`, etc.), dando prioridad de derecha a izquierda.
* **Drag & Drop con Clamping:** Permite arrastrar las cajas de firma libremente, pero incluye un sistema de contención matemática (clamping) que impide que las firmas salgan del área imprimible del documento.
* **Dimensionamiento Dinámico:** El tamaño de las cajas se adapta automáticamente:
  * **Estándar:** `160x56 px` (para 3, 5 o más firmas).
  * **Avanzada:** `200x70 px` (para 1, 2 o 4 firmas).
  * **Metadatos:** Respeta cualquier tamaño exacto enviado por el backend.
* **Persistencia Local (Auto-guardado):** Guarda el progreso en `localStorage`. Si el usuario recarga la página por accidente, las firmas ubicadas se restauran instantáneamente.
* **Paginación Estricta:** Manejo seguro de paginación que desactiva botones y controles si el documento tiene una sola página o si el usuario intenta ingresar un número fuera de los límites.

## 🚀 Tecnologías Utilizadas

* **HTML5 / CSS3:** Diseño responsivo, variables CSS y animaciones fluidas (Loader).
* **Vanilla JavaScript (ES6+):** Lógica pura sin frameworks pesados (sin React, Vue o jQuery).
* **[PDF.js](https://mozilla.github.io/pdf.js/) (v3.11.174):** Core para el procesamiento y extracción de texto de documentos PDF.

## 🔌 Integración y Comunicación (API Frontend)

Este módulo se comunica con el sistema padre (Backend/Iframe) a través de la API `window.postMessage`.

### 1. Iniciar el Módulo (De Backend a Frontend)
Para configurar la cantidad de firmas requeridas y su tamaño, el sistema padre debe enviar el siguiente objeto JSON:

```javascript
window.postMessage({
    tipo: 'CONFIGURAR_FIRMAS',
    cantidad: 3, // Número de firmas a ubicar
    metadata: {  // Opcional: Fuerza un tamaño específico para la caja
        ancho: 220,
        alto: 100
    }
}, '*');
