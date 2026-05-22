<p align="center">
  <img src="./banner.png" alt="Jonathan Sansó — Ssr. Full-Stack Developer" width="100%" />
</p>

<h3 align="center">Full-Stack Developer / Software Engineer / AI Engineer | Gemini LLM, Face Recognition, OCR/NLP/STT | Multi-tenant SaaS (Supabase/Postgres RLS)</h3>
<p align="center">Buenos Aires, Argentina · Remote · English B2</p>

---

### What I do
**4 years** building **multi-tenant SaaS** and **internal AI platforms** end-to-end — from tenant-isolated backends with **Supabase RLS/Policies** to polished frontends with **Next.js + TypeScript + Tailwind**.  
I build **face recognition services in production** (**InsightFace buffalo_l**, 512-d L2-normalized embeddings, NumPy cosine search, MariaDB BLOB storage), **AI document intelligence pipelines** (Tesseract OCR, NLP, Speech-to-Text with faster-whisper), **LLM-powered features** (Google Gemini API with 3-model cascade fallback for HA), **SendGrid transactional email workflows**, and **legacy DB migrations** (~110 GB of iBase8 → MySQL/MariaDB across 80+ modules). Deploy with **Docker, NGINX, AWS, Terraform**. Mercado Pago integration.

---

### Core Stack
| Layer | Technologies |
|---|---|
| **Frontend** | Next.js, React, TypeScript, JavaScript (ES6+), Tailwind, Zustand, TanStack Query, Zod, ShadCN UI |
| **Backend** | NestJS, Node.js, Prisma, FastAPI (Python), Express, GraphQL, REST APIs, OpenAPI/Swagger, Microservices |
| **Databases** | PostgreSQL (Supabase RLS, Triggers, RPC), MySQL, MariaDB, MongoDB, SQL Server, Redis, iBase (legacy migration) |
| **DevOps** | Docker, NGINX, AWS (EC2, RDS, S3, CloudFront), Terraform, CI/CD, GitHub Actions, Vercel, PM2, Git/GitHub |
| **AI & Data** | Gemini API (LLM cascade), InsightFace (buffalo_l, 512-d face embeddings), Tesseract OCR, faster-whisper STT, NLP, Pandas, NumPy, jsPDF, ExcelJS |
| **Integrations** | SendGrid (transactional email), Mercado Pago, Redis/BullMQ, Webhooks (HMAC signed) |
| **Testing & Methods** | Unit Testing, Jest, integration tests, Agile/Scrum, Kanban, Code Review, Git Flow |
| **Security** | Auth0, MFA/2FA, CSRF, Helmet/CORS, HMAC-SHA256, JWT, Rate Limiting |

---

### Experience

**Ocean Stack** — Full-Stack Developer / Software Engineer (Multi-tenant SaaS) · Dec 2025 – Present  
_Products: [Niappa POS](https://niappa-restaurant.vercel.app/) | [Oceans HR (ATS)](https://oceans-hr.vercel.app/)_  
- Multi-tenant isolation with **Supabase Postgres RLS/Policies** and RBAC across modules.  
- Orders at scale: table sessions, split checks, resilient order lifecycle with transactional integrity.  
- Built **Oceans HR ATS** serving **hundreds of CVs/month per tenant**: Kanban pipeline, drag-and-drop, recruitment funnel reports (Next.js 16, React 19, TanStack Query v5, @dnd-kit).  
- Engineered **AI-Powered CV Matching Engine**: LLM integration (Gemini API with 3-model cascade fallback for HA), PDF text extraction, weighted scoring across 8 criteria (skills, seniority, role, education, location, salary, language, industry), structured JSON output, drag-and-drop upload, color-coded score cards, per-criteria progress bars, and automated candidate creation pipeline.  
- Implemented **SendGrid transactional email pipeline** triggered by candidate pipeline phase changes (automated and semi-automated flows with recruiter approval): templated emails per stage, Supabase triggers + queued dispatch, idempotency keys, delivery audit log per tenant.  
- Mercado Pago API integration, PDF/Excel reporting, full ES/EN i18n.

**Argentine Federal Penitentiary Service** — Full-Stack Developer / AI Engineer / Software Engineer · Jan 2024 – Present  
- Led a **national-scale two-platform ecosystem** (internal ops + public verification portal).  
- Built **Python Face Matcher service** in production: **InsightFace buffalo_l** (ONNX CPU) 512-d L2-normalized embeddings, in-memory NumPy cosine brute-force + argpartition top-K, per-UID centroid (mean + renormalize) for multi-photo enrollment, persisted as BLOBs in MariaDB. Endpoints `/face/embed`, `/face/search`, `/face/search-multi` (FastAPI).  
- Built **AI document intelligence pipeline**: OCR (Tesseract LSTM spa+eng with grayscale + binarization threshold 140), hybrid PDF extraction (PyPDF2 native + pdf2image + Poppler @ 300 DPI fallback with per-page OCR, NDJSON streaming progress), and ASR (faster-whisper small INT8 CPU normalizing WhatsApp .opus via ffmpeg), all with human-in-the-loop review.  
- Migrated **~110 GB of legacy iBase8 data** to **MySQL/MariaDB** across **80+ modules**: relational tables plus heterogeneous binary content (**PDFs**, **scanned images**, **ZIP archives**, **Word documents**). Designed normalized relational schema, built ETL pipelines with chunked streaming and resumable runs, classified and stored binary assets with checksum integrity.  
- Containerized infrastructure dimensioned for **170 concurrent users** (Docker + NGINX + PM2 + Debian), automated backups, Redis job queues (BullMQ).  
- End-to-end security: MFA, CSRF, HMAC-SHA256, JWT, cryptographic document verification with watermarking.

**VirtuaState** — Frontend Developer · May 2022 – Dec 2023  
- Responsive marketing site for a VR/AR studio with SEO optimizations. [virtuastate.net](https://www.virtuastate.net/)

---

### Live Projects & Links
| | |
|---|---|
| **Portfolio** | [portfolio-sanso-jonathan.netlify.app](https://portfolio-sanso-jonathan.netlify.app/) |
| **Niappa POS** | [niappa-restaurant.vercel.app](https://niappa-restaurant.vercel.app/) |
| **Oceans HR** | [oceans-hr.vercel.app](https://oceans-hr.vercel.app/) |
| **VirtuaState** | [virtuastate.net](https://www.virtuastate.net/) |
| **E-Commerce React** | [react-e-commerce-j-sanso.vercel.app](https://react-e-commerce-j-sanso.vercel.app/) |
| **LinkedIn** | [jonathan-sanso-fullstack](https://www.linkedin.com/in/jonathan-sanso-fullstack/) |
| **GitHub** | [jonathansansok](https://github.com/jonathansansok) |

---

### Contact
- **Email:** jonasans2@live.com.ar  
- **WhatsApp:** [+54 9 11 6912-3268](https://wa.me/5491169123268)  
- **LinkedIn:** [jonathan-sanso-fullstack](https://www.linkedin.com/in/jonathan-sanso-fullstack)

---

```ts
const jonathanSanso = {
  role: "Full-Stack Developer / Software Engineer / AI Engineer",
  english: "B2",
  focus: [
    "Multi-tenant SaaS",
    "Face recognition in production",
    "AI document intelligence (OCR/NLP/STT)",
    "Legacy DB migrations (iBase8 → MySQL)",
    "SendGrid transactional email workflows",
    "Security-first architecture",
    "Product-minded delivery",
  ],
  stack: {
    frontend: ["Next.js", "React", "TypeScript", "JavaScript (ES6+)", "Tailwind", "Zustand", "TanStack Query", "ShadCN UI"],
    backend: ["NestJS", "Node.js", "Prisma", "FastAPI", "Express", "GraphQL", "REST APIs", "OpenAPI"],
    databases: ["PostgreSQL (Supabase RLS)", "MySQL", "MariaDB", "MongoDB", "Redis", "SQL Server", "iBase (legacy)"],
    ai_data: [
      "Gemini API (LLM cascade)",
      "InsightFace (buffalo_l, 512-d face embeddings)",
      "Tesseract OCR",
      "faster-whisper STT",
      "NLP",
      "Pandas",
      "NumPy",
      "jsPDF",
      "ExcelJS",
    ],
    integrations: ["SendGrid", "Mercado Pago", "Redis/BullMQ", "Webhooks (HMAC signed)"],
    infra: ["Docker", "NGINX", "AWS", "Terraform", "CI/CD", "GitHub Actions", "PM2", "Debian Linux", "Vercel"],
    security: ["Auth0", "MFA/2FA", "CSRF", "HMAC-SHA256", "JWT", "Rate Limiting"],
  },
} as const;
```

---

<p align="center"><a href="https://reactjs.org/"><img src="https://cdn.simpleicons.org/react/61DAFB" alt="react" height="40" /></a> <a href="https://nextjs.org/"><img src="https://cdn.simpleicons.org/nextdotjs/white" alt="nextjs" height="40" /></a> <a href="https://www.typescriptlang.org/"><img src="https://cdn.simpleicons.org/typescript/3178C6" alt="typescript" height="40" /></a> <a href="https://tailwindcss.com/"><img src="https://cdn.simpleicons.org/tailwindcss/06B6D4" alt="tailwind" height="40" /></a> <a href="https://nestjs.com/"><img src="https://cdn.simpleicons.org/nestjs/E0234E" alt="nestjs" height="40" /></a> <a href="https://expressjs.com/"><img src="https://cdn.simpleicons.org/express/white" alt="express" height="40" /></a> <a href="https://www.prisma.io/"><img src="https://cdn.simpleicons.org/prisma/2D3748" alt="prisma" height="40" /></a> <a href="https://www.mysql.com/"><img src="https://cdn.simpleicons.org/mysql/4479A1" alt="mysql" height="40" /></a> <a href="https://www.postgresql.org/"><img src="https://cdn.simpleicons.org/postgresql/4169E1" alt="postgresql" height="40" /></a> <a href="https://www.mongodb.com/"><img src="https://cdn.simpleicons.org/mongodb/47A248" alt="mongodb" height="40" /></a> <a href="https://www.docker.com/"><img src="https://cdn.simpleicons.org/docker/2496ED" alt="docker" height="40" /></a> <a href="https://redis.io/"><img src="https://cdn.simpleicons.org/redis/DC382D" alt="redis" height="40" /></a> <a href="https://www.python.org/"><img src="https://cdn.simpleicons.org/python/3776AB" alt="python" height="40" /></a> <a href="https://aws.amazon.com/"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" height="40" /></a> <a href="https://www.nginx.com/"><img src="https://cdn.simpleicons.org/nginx/009639" alt="nginx" height="40" /></a></p>

<p align="center"><a href="https://github.com/jonathansansok"><img src="https://img.shields.io/github/followers/jonathansansok?style=for-the-badge&logo=github&label=Followers&color=0d1117" alt="Followers" /></a> <a href="https://github.com/jonathansansok?tab=repositories"><img src="https://img.shields.io/github/stars/jonathansansok?style=for-the-badge&logo=github&label=Stars&color=0d1117" alt="Stars" /></a> <a href="https://github.com/jonathansansok"><img src="https://komarev.com/ghpvc/?username=jonathansansok&style=for-the-badge&color=0d1117&label=Profile+Views" alt="Profile Views" /></a></p>

<p align="center"><a href="https://github.com/jonathansansok"><img src="https://github-readme-streak-stats.herokuapp.com/?user=jonathansansok&theme=tokyonight&hide_border=true" alt="GitHub Streak" /></a></p>

<p align="center"><a href="https://github.com/jonathansansok"><img src="https://github-profile-trophy.vercel.app/?username=jonathansansok&theme=tokyonight&no-frame=true&row=1&column=7&margin-w=8" alt="GitHub Trophies" /></a></p>
