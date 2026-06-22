"""Generate Jonathan Sanso's resume PDF (v2) with fpdf2.

v2 changes:
- SPF: added Python Face Matcher (InsightFace buffalo_l, 512-d embeddings) and
  legacy iBase8 -> MySQL/MariaDB ETL migration (80+ modules).
- Oceans HR: added SendGrid automated/semi-automated transactional emails
  triggered on candidate pipeline phase advancement.
"""
from fpdf import FPDF

class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(format="letter")
        self.set_auto_page_break(auto=False)
        self.BLACK = (0, 0, 0)
        self.DARK = (30, 30, 30)
        self.LINK_BLUE = (0, 102, 204)
        self.GRAY_LINE = (60, 60, 60)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*self.BLACK)
        self.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(*self.GRAY_LINE)
        self.set_line_width(0.4)
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(1.5)

    def skill_line(self, label, value):
        self.set_font("Helvetica", "B", 7.3)
        self.set_text_color(*self.BLACK)
        lw = self.get_string_width(label + " ")
        self.cell(lw, 3.3, label + " ")
        self.set_font("Helvetica", "", 7.3)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 3.3, value, new_x="LMARGIN", new_y="NEXT", markdown=True)

    def job_header(self, company, role, dates):
        self.set_font("Helvetica", "B", 8.5)
        self.set_text_color(*self.BLACK)
        self.cell(self.get_string_width(company + " "), 4.5, company + " ")
        self.set_font("Helvetica", "", 7.5)
        self.write(4.5, "-- ")
        self.set_font("Helvetica", "I", 7.5)
        self.write(4.5, role)
        self.set_font("Helvetica", "", 7.5)
        self.write(4.5, "  - " + dates)
        self.ln(4.5)

    def sub_header(self, text):
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(80, 80, 80)
        self.cell(0, 3.5, text, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 7.1)
        self.set_text_color(*self.DARK)
        bullet_indent = 3.5
        self.cell(bullet_indent, 3.2, "- ")
        self.multi_cell(self.w - self.l_margin - self.r_margin - bullet_indent, 3.2, text, new_x="LMARGIN", new_y="NEXT", markdown=True)

    def edu_header(self, title, institution, dates):
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.BLACK)
        self.cell(self.get_string_width(title + " "), 4, title + " ")
        self.set_font("Helvetica", "", 7.5)
        self.write(4, "- " + institution + " - " + dates)
        self.ln(4)


def build():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(12, 8, 12)
    pdf.set_y(8)

    # -- Header --
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(*pdf.BLACK)
    pdf.cell(0, 7, "JONATHAN SANSO", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(*pdf.DARK)
    pdf.cell(0, 3.5,
             "Full-Stack Developer / Software Engineer / AI Engineer | Gemini LLM, Face Recognition, OCR/NLP/STT | Multi-tenant SaaS (Supabase/Postgres RLS)",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 3.5,
             "Buenos Aires, Argentina | +54 9 11 6912-3268 | jonasans2@live.com.ar | English B2",
             align="C", new_x="LMARGIN", new_y="NEXT")

    # Links (explicit URLs)
    pdf.set_font("Helvetica", "", 7.5)
    links = [
        ("https://portfolio-sanso-jonathan.netlify.app", "https://portfolio-sanso-jonathan.netlify.app/"),
        ("https://github.com/jonathansansok", "https://github.com/jonathansansok"),
        ("https://linkedin.com/in/jonathan-sanso-fullstack", "https://www.linkedin.com/in/jonathan-sanso-fullstack/"),
    ]
    total_w = sum(pdf.get_string_width(l[0]) for l in links) + pdf.get_string_width(" | ") * 2
    start_x = (pdf.w - total_w) / 2
    pdf.set_x(start_x)
    for i, (label, url) in enumerate(links):
        pdf.set_text_color(*pdf.LINK_BLUE)
        pdf.cell(pdf.get_string_width(label), 3.5, label, link=url)
        if i < len(links) - 1:
            pdf.set_text_color(*pdf.DARK)
            pdf.cell(pdf.get_string_width(" | "), 3.5, " | ")
    pdf.ln(4.5)

    # -- Summary --
    pdf.section_title("SUMMARY")
    pdf.set_font("Helvetica", "", 7.3)
    pdf.set_text_color(*pdf.DARK)
    pdf.multi_cell(0, 3.4, (
        "**Full-Stack Developer** with **4 years** of experience building web products end-to-end (multi-tenant SaaS, internal platforms, AI services). "
        "Core expertise in **tenant isolation** (Supabase **RLS**/Policies), **POS/orders lifecycle**, **RBAC**, "
        "**AI engineering** (face recognition embeddings, OCR/NLP/STT, LLM scoring), **legacy DB migrations**, "
        "and **security-first architecture** (MFA, CSRF, HMAC/JWT). "
        "Daily stack: **Next.js**, **React**, **TypeScript**, Tailwind, **Supabase/PostgreSQL**, **NestJS**, Prisma, "
        "**Python** (FastAPI, Pandas, **InsightFace**). Experienced with **Docker**, NGINX, **AWS**, Terraform, "
        "**Redis/BullMQ**, **SendGrid**, Mercado Pago API."
    ), new_x="LMARGIN", new_y="NEXT", markdown=True)
    pdf.ln(0.8)
    # Core competencies keyword line (ATS-friendly flat list, wraps to left margin)
    pdf.set_font("Helvetica", "", 7.3)
    pdf.set_text_color(*pdf.DARK)
    pdf.multi_cell(0, 3.4, (
        "**Core Competencies:** Full-Stack Development | Software Engineering | AI Engineering | LLM Integration | RAG | Vector Search | "
        "Face Recognition | OCR | Speech-to-Text | Multi-tenant SaaS | RBAC | Row-Level Security | REST APIs | "
        "Microservices | CI/CD | Legacy DB Migration | ETL | Agile / Scrum | Code Review"
    ), new_x="LMARGIN", new_y="NEXT", markdown=True)
    pdf.ln(0.5)

    # -- Technical Skills --
    pdf.section_title("TECHNICAL SKILLS")
    skills = [
        ("Frontend:", "**Next.js**, **React**, **TypeScript**, **JavaScript (ES6+)**, **Tailwind CSS**, HTML5, CSS3, Zustand, **TanStack Query**, **Zod**, react-hook-form, @dnd-kit, ShadCN UI"),
        ("Backend:", "**NestJS**, **Node.js**, **Prisma**, **FastAPI** (Python), Express, GraphQL, **REST APIs / RESTful**, **OpenAPI / Swagger**, **Microservices**"),
        ("Databases:", "**PostgreSQL** (Supabase **RLS**, Triggers, RPC, Indexes), **MySQL**, **MariaDB**, MongoDB, SQL Server, **iBase** (legacy migration)"),
        ("DevOps & Infra:", "**Docker**, **NGINX**, Debian/Linux, **AWS** (EC2, RDS, S3, CloudFront), **Terraform**, **CI/CD**, **GitHub Actions**, Vercel, Git/GitHub, PM2"),
        ("AI & Data:", "**Gemini API**, **InsightFace** (**512-d face embeddings**), **Tesseract OCR**, **faster-whisper STT**, NLP, Pandas, NumPy, jsPDF, ExcelJS"),
        ("Integrations:", "**SendGrid** (transactional email), **Mercado Pago**, **Redis/BullMQ**, Webhooks (HMAC signed)"),
        ("Testing & Methods:", "**Unit Testing**, **Jest**, integration tests, **Agile / Scrum**, Kanban, Code Review, Git Flow"),
        ("Security:", "Auth0, **MFA/2FA**, **CSRF**, Helmet/CORS, **HMAC-SHA256**, **JWT**, Rate Limiting, Input Sanitization"),
    ]
    for label, value in skills:
        pdf.skill_line(label, value)
    pdf.ln(1.5)

    # -- Professional Experience --
    pdf.section_title("PROFESSIONAL EXPERIENCE")

    # Ocean Stack
    pdf.job_header("Ocean Stack", "Full-Stack Developer / Software Engineer (Multi-tenant SaaS)", "Dec 2025 - Present")
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 3.5, "Products: Niappa POS | Oceans HR (ATS)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.5)

    ocean_bullets = [
        "Shipped **weekly product increments** in a structured delivery loop: **Figma** as source of truth, daily alignment with **CTO + PM**, iterative releases, and **UX/UI polishing** (Next.js, TypeScript, Tailwind).",
        "Implemented **tenant-safe isolation** and **role-based permissions** across modules so each business only sees and mutates its own data (**Supabase Postgres**, **RLS/Policies**).",
        "Delivered **operational back-office flows** (products, ingredients, stock, counts, suppliers) with **strong data consistency** guarantees via DB automation (**Postgres triggers**, indexes, **SQL/RPC**).",
        "Implemented **orders at scale**: **table sessions + split checks**, resilient **order lifecycle**, and safe **edit/void/restore** flows keeping stock accurate end-to-end (**RPC**, **transactional integrity**, **idempotent stock adjustments**).",
        "Built **reporting exports** for operations: **PDF/Excel** (sales + cash/audit), plus productivity-focused UI improvements (**i18n ES/EN**, search, sorting, confirmations).",
        "Built **Oceans HR ATS module** serving **hundreds of CVs/month per tenant** across multiple active clients: **Kanban pipeline with drag-and-drop**, vacancy management, candidate profiles with notes/comments, **recruitment funnel reports**, **RBAC with company-level roles**, full **ES/EN i18n** (Next.js 16, React 19, TanStack Query v5, Zod v4, @dnd-kit, Supabase RLS).",
        "Engineered **AI-Powered CV Matching Engine**: **LLM integration** (**Gemini API with 3-model cascade fallback** for HA), **PDF text extraction**, **weighted scoring across 8 criteria** (skills, seniority, role, education, location, salary, language, industry), **structured JSON output**, plus full frontend UX with drag-and-drop upload, color-coded score cards, per-criteria progress bars, and **automated candidate creation pipeline** (Next.js App Router, Supabase RLS).",
        "Implemented **SendGrid transactional email pipeline** triggered by **candidate pipeline phase changes** (**automated and semi-automated flows** with recruiter approval step): **templated emails per stage**, **Supabase triggers + queued dispatch**, **idempotency keys**, and **delivery audit log per tenant**.",
    ]
    for b in ocean_bullets:
        pdf.bullet(b)
    pdf.ln(0.8)

    # Argentine Federal Penitentiary Service
    pdf.job_header("Argentine Federal Penitentiary Service",
                   "Full-Stack Developer / AI Engineer / Software Engineer", "Jan 2024 - Present")
    pdf.sub_header("Private repos -- Sige2i internal platform (NestJS + Next.js + Python/FastAPI)")
    pdf.ln(0.5)

    afps_bullets = [
        "Led delivery of a **two-platform ecosystem** (internal ops + public verification portal) with **secure data flows** and controlled access for multiple stakeholders (React, Next.js, TypeScript, Tailwind, NestJS, Prisma).",
        "Built **Python Face Matcher service** in production: **InsightFace buffalo_l** (ONNX CPU) **512-d L2-normalized embeddings**, in-memory (N, 512) float32 index with **NumPy cosine brute-force + argpartition top-K**, **per-UID centroid** (mean + renormalize) for multi-photo enrollment, persisted as **BLOBs in MariaDB**. Endpoints /face/embed, /face/search, /face/search-multi (**FastAPI**).",
        "Built an **AI-assisted document intelligence pipeline**: **OCR** (**Tesseract LSTM** spa+eng with grayscale + binarization threshold 140), **hybrid PDF extraction** (PyPDF2 for native text, **pdf2image + Poppler @ 300 DPI** fallback with per-page OCR, **NDJSON streaming progress**), and **ASR** (**faster-whisper small INT8 CPU** normalizing WhatsApp .opus via ffmpeg), all with **human-in-the-loop review**.",
        "Migrated **~110 GB of legacy iBase8 data** to **MySQL/MariaDB** across **80+ modules**: relational tables plus heterogeneous binary content (**PDFs**, **scanned images**, **ZIP archives**, **Word documents**). Designed **normalized relational schema**, built **ETL pipelines** with chunked streaming and resumable runs, **classified and stored binary assets** with checksum integrity, mapped legacy field types and indexes, validated data integrity end-to-end, and integrated migrated entities into the new **NestJS + Next.js** stack.",
        "Automated **operational reporting** (**PDF/Excel/Word**) with charts, filters, and standardized formatting replacing manual workflows (TypeScript, Pandas).",
        "Engineered **secure document verification**: **time-limited access**, **cryptographic validation**, **anti-exfiltration controls** (**HMAC-SHA256**, **JWT**, watermarking).",
        "Implemented **end-to-end security** (**MFA**, **CSRF**, input sanitization, **rate limiting**, **Helmet/CORS**) and delivered **containerized infrastructure** dimensioned for **170 concurrent users** with reverse proxying, process management and **automated backups** (**Docker**, **NGINX**, **PM2**, Debian).",
        "Built **secure integration layer**: **signed requests**, **idempotency**, **clock-skew validation**, **file integrity checks** (**SHA-256**).",
        "Leveraged **Redis** for **async job queues** (audit logging, cross-service publishing, scheduled sync) with **BullMQ**, plus **server-side caching** with **automatic in-memory fallback** for **zero-downtime resilience**.",
    ]
    for b in afps_bullets:
        pdf.bullet(b)
    pdf.ln(0.8)

    # VirtuaState
    pdf.job_header("VirtuaState", "Frontend Developer", "May 2022 - Dec 2023")
    pdf.bullet("Built a responsive marketing/portfolio site for a VR/AR studio with **SEO** and performance optimizations (HTML5, CSS3, JavaScript, mobile-first).")
    pdf.set_font("Helvetica", "", 7.3)
    bullet_indent = 3.5
    pdf.set_x(pdf.l_margin + bullet_indent)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pdf.get_string_width("Live: "), 3.4, "Live: ")
    pdf.set_text_color(*pdf.LINK_BLUE)
    virtua_url = "https://www.virtuastate.net/"
    pdf.cell(pdf.get_string_width(virtua_url), 3.4, virtua_url, link=virtua_url)
    pdf.ln(3.4)
    pdf.ln(1.5)

    # -- Education --
    pdf.section_title("EDUCATION")
    pdf.edu_header("Higher Degree in Programming", "Teclab", "Aug 2022 - Aug 2024")
    pdf.bullet("Software fundamentals and delivery practices: databases, web development, UX, cloud basics, project management.")
    pdf.ln(0.5)
    pdf.edu_header("Full-Stack Web Development", "CoderHouse", "Jan 2022 - Mar 2023")
    pdf.bullet("Delivered multiple end-to-end projects: frontend and backend foundations, web app architecture (HTML5, EJS, CSS/SASS, React, Node.js, MongoDB, Express, GraphQL).")
    pdf.set_font("Helvetica", "", 7.3)
    bullet_indent = 3.5
    pdf.set_x(pdf.l_margin + bullet_indent)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pdf.get_string_width("Live: "), 3.4, "Live: ")
    pdf.set_text_color(*pdf.LINK_BLUE)
    coder_url = "https://react-e-commerce-j-sanso.vercel.app/"
    pdf.cell(pdf.get_string_width(coder_url), 3.4, coder_url, link=coder_url)
    pdf.ln(3.4)

    pdf.output("Jonathan-Sanso-Full-Stack-AI-Engineer2.pdf")
    print(f"PDF generated! Pages: {pdf.pages_count}, final Y: {pdf.get_y():.1f} / {pdf.h:.1f}")

if __name__ == "__main__":
    build()
