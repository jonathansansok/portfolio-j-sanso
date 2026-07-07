Lidero la arquitectura, desarrollo, seguridad y despliegue de plataformas institucionales de alcance nacional para el Servicio Penitenciario Federal, con ownership completo del stack: frontend, backend e infraestructura dockerizada sobre Debian + NGINX.

Reemplazo procesos manuales y propensos a errores por soluciones digitales seguras, escalables y asistidas por IA, reduciendo tiempos operativos.

🔹 Plataforma Institucional de Eventos Complejos

(Privada – Alcance Nacional)

Modernización integral de procesos internos, reemplazando flujos en Excel por una plataforma web escalable construida con Next.js, NestJS, Prisma y MySQL.

Principales aportes:

Diseño de arquitectura modular y validaciones complejas

Formularios dinámicos, carga de archivos y procesamiento de imágenes

Generación automática de reportes PDF, Excel y Word con filtros temporales y estadísticos

Herramientas GIS con Leaflet y Google Maps

Seguridad aplicada: Auth0 2FA, CSRF, sanitización y rate limiting

Despliegue productivo con Docker, NGINX reverse proxy y backups automáticos de MySQL

Chatbot NL con SQL-RAG (SQL determinista sobre DB legacy 90+ tablas, cero alucinaciones, air-gapped) + LLM local (Ollama/Qwen2.5, solo CPU), citas [n], streaming NDJSON; >45s → sub-segundo

Integración de IA en producción mediante un microservicio en Python (FastAPI) para:

Extracción de texto desde imágenes, PDFs escaneados y audios (OCR y Speech-to-Text)

Autocompletado de información con flujos de revisión humana

Resúmenes automáticos con clasificación de riesgo

🔹 Portal Público de Verificación Web

(Externo)

Plataforma para verificación segura de documentos institucionales, con:

Validación HMAC-SHA256

Accesos temporales con JWT

Protección anticopia/capturas y watermark dinámico

Renderizado TipTap JSON → HTML

Despliegue con Docker/Compose, NGINX, Helmet y CORS

🔹 Sistema Interno de Tickets de Mantenimiento

PHP + MySQL con Google SSO, auditoría completa e historial consultable.