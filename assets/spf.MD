I lead the architecture, development, security and deployment of nationwide institutional platforms for the SPF with full ownership of the stack: frontend, backend, AI services and Dockerized infrastructure (Debian + NGINX + PM2, 170 concurrent users). I replace manual, error-prone processes with secure, scalable, AI-assisted digital solutions.



🔹 Institutional Platform Sige2i (Private – VPN)

End-to-end modernization replacing Excel workflows and legacy iBase8 systems (Next.js, NestJS, Prisma, MySQL/MariaDB).



Key contributions:



NL intelligence chatbot (SQL-RAG + local LLM): deterministic SQL over a 90+ table legacy DB (zero hallucinated facts, air-gapped) + grounded local LLM (Ollama/Qwen2.5, CPU-only), LLM structured-output NL parsing, inline [n] citations, NDJSON streaming; >45s self-join → sub-second.

Python Face Matcher in prod: InsightFace buffalo_l (ONNX CPU), 512-d L2-normalized embeddings, NumPy cosine top-K, per-UID centroid for multi-photo enrollment, MariaDB BLOB storage. Endpoints /face/embed, /face/search, /face/search-multi (FastAPI).



Legacy DB migration: ~110 GB iBase8 → MySQL/MariaDB across 80+ modules (tables + PDFs, scanned images, ZIPs, Word docs). Normalized schema, ETL with chunked streaming, per-asset checksum integrity.



AI document intelligence (Python/FastAPI): OCR (Tesseract LSTM spa+eng), hybrid PDF extraction (PyPDF2 + pdf2image/Poppler 300 DPI, NDJSON streaming), ASR (faster-whisper INT8 CPU, .opus via ffmpeg). Auto-populate forms with human-in-the-loop, summaries, risk classification.



PDF/Excel/Word reports with temporal and statistical filters.

GIS with Leaflet and Google Maps.



Security: Auth0 2FA, CSRF, input sanitization, rate limiting, Helmet/CORS.

Deploy: Docker + NGINX + PM2, automated MySQL backups.



🔹 Public Web Verification Portal (External)

HMAC-SHA256, time-limited JWT, anti-copy/anti-capture with dynamic watermarking, TipTap JSON → HTML rendering. Docker/Compose, NGINX, Helmet, CORS.