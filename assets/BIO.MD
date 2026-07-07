👋 Ssr Full-Stack / AI Engineer, 4 years shipping multi-tenant SaaS and AI platforms end-to-end. Core: tenant isolation (Supabase RLS), POS/orders, RBAC, RAG + local LLM chatbots, face recognition in prod, AI document intelligence (OCR/NLP/STT), legacy DB migrations, security-first (MFA, CSRF, HMAC/JWT).

Daily stack: Next.js, React, TypeScript, Tailwind, Supabase/PostgreSQL, NestJS, Prisma, Python (FastAPI, InsightFace, Pandas), Docker, NGINX, AWS, Terraform, Redis/BullMQ, SendGrid.

🧩 Key Platforms

1️⃣ Ocean Stack - Multi-tenant SaaS (Niappa POS + Oceans HR ATS). Tenant-isolated (Supabase RLS). Niappa POS: table sessions, split checks, resilient order lifecycle, Mercado Pago. Oceans HR ATS (hundreds of CVs/month per tenant): Kanban, vacancies, funnel reports, ES/EN i18n. AI CV Matching: Gemini API (3-model cascade), PDF extraction, scoring across 8 criteria. SendGrid transactional emails on candidate phase changes (auto + semi-auto with recruiter approval, Supabase triggers, idempotency, audit log per tenant). Next.js 16, React 19, TanStack Query, Zod, @dnd-kit. 

2️⃣ SPF - Institutional Platform (Full-Stack + AI). Two-platform ecosystem (internal ops + public verification) for 170 concurrent users. NL intelligence chatbot over 90+ table legacy DB: SQL-RAG (deterministic retrieval, zero hallucinated facts, air-gapped) + grounded local LLM (Ollama/Qwen2.5, CPU-only), inline [n] citations, NDJSON streaming; >45s self-join → sub-second. Python Face Matcher in prod: InsightFace buffalo_l, 512-d embeddings, cosine search, MariaDB BLOB (FastAPI). AI doc intelligence: Tesseract OCR + faster-whisper STT + hybrid PDF extraction, human-in-the-loop. Legacy migration: ~110 GB iBase8 → MySQL/MariaDB across 80+ modules via ETL (chunked streaming, checksum integrity). Secure verification: HMAC-SHA256, JWT, watermarking. MFA, CSRF, rate limiting. Docker + NGINX + PM2 + Debian.
Live: Private Platforms

3️⃣ VirtuaState - Responsive VR/AR studio site (HTML5/CSS/JS, mobile-first), SEO optimized. Live: virtuastate.net

☁️ AWS + Terraform (IaC) — Personal. Full-stack AWS: VPC, EC2 (Dockerized NestJS + NGINX), RDS MySQL, S3 + CloudFront. 
Live: d2hiu34pyeqif1.cloudfront.net

⚙️ React · Next.js · NestJS · TypeScript · Tailwind · Prisma · Supabase/PostgreSQL (RLS) · MySQL · MariaDB · FastAPI · SQL-RAG · Local LLM (Ollama) · InsightFace · Gemini API · OCR/NLP/STT · Redis/BullMQ · SendGrid · AWS · Terraform · Docker · NGINX

🎯 Multi-tenant SaaS · RAG chatbots · Face recognition in prod · AI document intelligence · Legacy DB migrations · POS/Orders · Web security.
