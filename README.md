# 📄 E-Digital Signature Placer (Posicionador Automático de Firmas)

Un módulo Frontend avanzado e independiente diseñado para la ubicación visual y automática de recuadros de firma electrónica sobre documentos PDF. 

Este sistema utiliza **PDF.js** para renderizar el documento en el navegador, escanear su contenido en busca de zonas de firma, y devolver un JSON enriquecido con coordenadas precisas para su posterior procesamiento en el Backend (ej. CodeIgniter, Laravel, Node).

## ✨ Características Principales

* 🧠 **Smart Anchor (Anclaje Inteligente):** Escanea la capa de texto del PDF buscando palabras clave como *"Empleador", "Trabajador", "RUT", "DNI", "RFC"*, entre otras. Si las encuentra, "teletransporta" y ancla la caja de firma exactamente sobre la línea correspondiente.
* 📏 **Coordenadas Universales (Eje Y Invertido):** Calcula y exporta las coordenadas tradicionales de la web (desde arriba hacia abajo) y las coordenadas estándar de los PDF (desde abajo hacia arriba), evitando dolores de cabeza en el Backend al momento de estampar la firma.
* 🧲 **Guías Magnéticas (Snapping):** Asistencia visual de alineación automática (ejes X e Y) al arrastrar múltiples firmas para un diseño simétrico y perfecto.
* 🛡️ **Prevención de Errores (Candados QA):** Validaciones estrictas para evitar el envío de JSON vacíos, firmas incompletas o interacciones antes de recibir la configuración del servidor.

## 🛠️ Tecnologías

* **HTML5 / CSS3:** Interfaz limpia, responsiva y orientada a la usabilidad (UX).
* **Vanilla JavaScript (ES6+):** Lógica de arrastre, cálculo de matrices y comunicación sin dependencias pesadas.
* **Mozilla PDF.js (v3.11):** Motor de renderizado y extracción de metadatos/texto nativo de los documentos.

## 🚀 Cómo funciona la Integración (API Interna)

Este módulo está pensado para vivir dentro de un `<iframe>` o ventana modal, comunicándose con el sistema padre (Backend/Plataforma principal) mediante `window.postMessage`.

### 1. Recibir Configuración (De Padre a Módulo)
El sistema padre debe enviar un mensaje indicando cuántas firmas se requieren para habilitar la interfaz:

```javascript
window.postMessage({
    tipo: 'CONFIGURAR_FIRMAS',
    cantidad: 2 // Número de firmantes requeridos
}, '*');
