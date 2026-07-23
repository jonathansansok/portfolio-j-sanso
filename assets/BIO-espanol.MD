👋 Ssr Full-Stack / AI Engineer, 4 años entregando SaaS multi-tenant y plataformas con IA end-to-end. Especialidad: aislamiento por tenant (Supabase RLS), POS/órdenes, RBAC, RAG + chatbots con LLM local, reconocimiento facial en prod, IA documental (OCR/NLP/STT), migraciones legacy, seguridad (MFA, CSRF, HMAC/JWT).

Stack: Next.js, React, TypeScript, Tailwind, Supabase/PostgreSQL, NestJS, Prisma, Python (FastAPI, InsightFace, Pandas), Docker, NGINX, AWS, Terraform, Redis/BullMQ, SendGrid.

🧩 Plataformas clave

1️⃣ Ocean Stack (Dic 2025 - Jun 2026) - SaaS multi-tenant (Niappa POS + Oceans HR ATS). Aislamiento por tenant (Supabase RLS). Niappa POS: mesas, cuentas divididas, ciclo de órdenes resiliente, Mercado Pago. Oceans HR ATS (cientos de CVs/mes por cliente): Kanban, vacantes, reportes de embudo, i18n ES/EN. AI CV Matching: Gemini API (cascada de 3 modelos), extracción de PDF, scoring sobre 8 criterios. Emails transaccionales SendGrid por cambio de fase (auto + semi-auto con aprobación, triggers Supabase, idempotencia, log por tenant). Next.js 16, React 19, TanStack Query, Zod, @dnd-kit.

2️⃣ SPF - Plataforma institucional (Full-Stack + IA). Dos plataformas (ops interna + verificación pública) para 170 usuarios concurrentes. Chatbot NL de inteligencia sobre DB legacy de 90+ tablas: SQL-RAG (retrieval determinista, cero alucinaciones, air-gapped) + LLM local grounded (Ollama/Qwen2.5, solo CPU), citas [n], streaming NDJSON; self-join de >45s → sub-segundo. Python Face Matcher en prod: InsightFace buffalo_l, embeddings 512-d, búsqueda cosine, BLOB MariaDB (FastAPI). IA documental: Tesseract OCR + faster-whisper STT + extracción híbrida de PDFs con revisión humana. Migración: ~110 GB iBase8 → MySQL/MariaDB en 80+ módulos (tablas + PDFs, imágenes, ZIPs, Word) vía ETL con streaming en chunks y checksum. Verificación: HMAC-SHA256, JWT, marca de agua. MFA, CSRF, rate limiting. Redis/BullMQ. Docker + NGINX + PM2 + Debian.

3️⃣ VirtuaState - Sitio responsive VR/AR (HTML5/CSS/JS, mobile-first), SEO. Live: virtuastate.net

☁️ AWS + Terraform (IaC) — Personal. VPC, EC2 (NestJS + NGINX dockerizados), RDS MySQL, S3 + CloudFront.

Live: d2hiu34pyeqif1.cloudfront.net

⚙️ React · Next.js · NestJS · TypeScript · Tailwind · Prisma · Supabase/PostgreSQL (RLS) · MySQL · MariaDB · FastAPI · SQL-RAG · LLM local (Ollama) · InsightFace · Gemini API · OCR/NLP/STT · Redis/BullMQ · SendGrid · AWS · Terraform · Docker · NGINX

🎯 SaaS multi-tenant · Chatbots RAG · Face recognition en prod · IA documental · Migraciones de DB legacy · POS/Órdenes · Seguridad web.