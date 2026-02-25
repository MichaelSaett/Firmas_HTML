from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pypdf import PdfReader
import io
from fastapi.middleware.cors import CORSMiddleware

# Imagina que el archivo de tu jefe se llama "extractor_jefe.py"
# import extractor_jefe 

app = FastAPI(title="Configurador de Firmas")

# --- Redirección automática a la interfaz ---
@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

# --- Configurar CORS para permitir el Iframe ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En el futuro aquí pondrás ["https://www.e-digital.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servimos la carpeta donde estará tu HTML
app.mount("/static", StaticFiles(directory="public"), name="static")

@app.post("/api/procesar")
async def procesar_documento(documento: UploadFile = File(...)):
    try:
        # =================================================================
        # 🛡️ SEGURIDAD BACKEND: Rechazar de inmediato si no es un PDF
        # =================================================================
        if documento.content_type != "application/pdf":
            return JSONResponse(status_code=400, content={"error": "Tipo de archivo no permitido. Solo se aceptan documentos PDF."})

        # 1. Leemos el PDF que subió el usuario en la web
        contenido_pdf = await documento.read()
        
        # =================================================================
        # 2. CONEXIÓN CON EL CÓDIGO DE TU JEFE
        # Aquí le pasas el PDF a la función de tu jefe y él te devuelve el HTML.
        # Ejemplo real: html_generado = extractor_jefe.transformar_pdf_a_html(contenido_pdf)
        # =================================================================
        
        # Para esta prueba, simularemos lo que devuelve tu jefe:
        html_generado = """<div style='padding:20px;'>
            <h3 style='text-align:center;'>Documento E-digital</h3>
            <p>En la ciudad de {ciudad}, a {fecha_actual}...</p>
            <br><br><br>
        </div>"""

        # 3. TU PARTE: Sacar las dimensiones del PDF para la pantalla
        pdf = PdfReader(io.BytesIO(contenido_pdf))
        total_paginas = len(pdf.pages)
        ultima_pagina = pdf.pages[total_paginas - 1]
        ancho = float(ultima_pagina.mediabox.width)
        alto = float(ultima_pagina.mediabox.height)

        # 4. Devolvemos TODO a la interfaz web (HTML de tu jefe + Medidas)
        return {
            "html_jefe": html_generado,
            "meta": {
                "page_width": round(ancho),
                "page_height": round(alto),
                "paginas_totales": total_paginas
            }
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})