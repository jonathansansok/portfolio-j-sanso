"""Jonathan Sanso resume - Solutions Engineer variant (fpdf2).

Copy of generate_resume_v3.py, retargeted for Solutions Engineer applications.
Beefed up 2 points per recruiter follow-up (Rafael Braganca thread):
  1) Cloud/PowerShell autonomy: AWS+Terraform+GitHub Actions depth + hands-on Azure exposure.
  2) Pre-sales / requirements-gathering angle: SPF role includes discovery with
     stakeholders to find manual workflows worth automating with AI.
Note: SPF platforms are private/internal (federal confidentiality) - no public
links can be shared for that work, flagged inline under the SPF sub-header.
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
             "Solutions Engineer | Full-Stack / AI Engineer | AWS + Terraform + GitHub Actions | Azure-ready | Automation",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 3.5,
             "Buenos Aires, Argentina | +54 9 11 6912-3268 | jonasans2@live.com.ar | English B2",
             align="C", new_x="LMARGIN", new_y="NEXT")

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
        "**Solutions Engineer / Full-Stack Developer** with **4 years** combining **development, infrastructure and "
        "automation** to deliver end-to-end solutions. Deep hands-on **AWS** (EC2, RDS, S3, CloudFront) + **Terraform** "
        "(IaC) + **GitHub Actions** (CI/CD), which transfers directly to **Azure** (hands-on: dockerized Next.js + MySQL "
        "app deployed on Azure) and to **PowerShell** (used daily for Windows/Debian workflow automation, in addition to "
        "Python/Bash). Owns **requirements discovery**: at the Federal Penitentiary Service I am the one who surveys "
        "staff needs and identifies which manual workflows are worth automating with AI, then ships the solution. "
        "Daily stack: **Next.js**, **React**, **TypeScript**, **NestJS**, **Python** (FastAPI), **Docker**, **Gemini API/LLM**."
    ), new_x="LMARGIN", new_y="NEXT", markdown=True)
    pdf.ln(0.8)
    pdf.set_font("Helvetica", "", 7.3)
    pdf.set_text_color(*pdf.DARK)
    pdf.multi_cell(0, 3.4, (
        "**Core Competencies:** Solutions Engineering | Requirements Discovery / Stakeholder Relevamiento | Full-Stack "
        "Development | AI/LLM Integration | AWS | Azure (hands-on) | Terraform | GitHub Actions / CI/CD | PowerShell | "
        "Python | Bash | Docker | Multi-tenant SaaS | REST APIs | Legacy DB Migration | RBAC / Row-Level Security | "
        "Microservices | CI/CD | Agile / Scrum"
    ), new_x="LMARGIN", new_y="NEXT", markdown=True)
    pdf.ln(0.5)

    # -- Technical Skills --
    pdf.section_title("TECHNICAL SKILLS")
    skills = [
        ("Cloud & IaC:", "**AWS** (EC2, RDS, S3, CloudFront), **Terraform** (IaC), **Azure** (hands-on: Docker app + MySQL deploy, public reports portal), Vercel"),
        ("Automation & Scripting:", "**Python**, **Bash** (Linux/Debian), **PowerShell** (Windows/Debian file transfer & workflow automation), **GitHub Actions**, **CI/CD**"),
        ("Frontend:", "**Next.js**, **React**, **TypeScript**, **JavaScript (ES6+)**, **Tailwind CSS**, Zustand, **TanStack Query**, **Zod**, react-hook-form, @dnd-kit"),
        ("Backend:", "**NestJS**, **Node.js**, **Prisma**, **FastAPI** (Python), Express, **REST APIs**, **OpenAPI/Swagger**, **Microservices**"),
        ("Databases:", "**PostgreSQL** (Supabase RLS/Triggers/RPC), **MySQL**, **MariaDB**, MongoDB, SQL Server, **iBase** (legacy migration)"),
        ("AI & Data:", "**Gemini API** (LLM scoring/cascade), **InsightFace** (face embeddings), **Tesseract OCR**, **faster-whisper STT**, NLP, Pandas, NumPy"),
        ("Integrations:", "**SendGrid** (transactional email), **Mercado Pago**, **Redis/BullMQ**, Webhooks (HMAC signed)"),
        ("Infra & Security:", "**Docker**, **NGINX**, Debian/Linux, PM2, **MFA/2FA**, **HMAC-SHA256**, **JWT**, Helmet/CORS, Rate Limiting"),
    ]
    for label, value in skills:
        pdf.skill_line(label, value)
    pdf.ln(1.5)

    # -- Professional Experience --
    pdf.section_title("PROFESSIONAL EXPERIENCE")

    # Ocean Stack
    pdf.job_header("Ocean Stack", "Full-Stack Developer / Software Engineer (Multi-tenant SaaS)", "Dec 2025 - Jun 2026")
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pdf.get_string_width("Products: Niappa POS | Oceans HR (ATS)  "), 3.5, "Products: Niappa POS | Oceans HR (ATS)  ")
    pdf.set_text_color(*pdf.LINK_BLUE)
    pdf.cell(0, 3.5, "oceansstack.com", link="https://oceansstack.com/", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(80, 80, 80)
    pdf.ln(0.5)

    ocean_bullets = [
        "Shipped **weekly product increments** in a structured delivery loop: **Figma** as source of truth, daily alignment with **CTO + PM**, iterative releases, and **UX/UI polishing** (Next.js, TypeScript, Tailwind).",
        "Implemented **tenant-safe isolation** and **role-based permissions** across modules so each business only sees and mutates its own data (**Supabase Postgres**, **RLS/Policies**).",
        "Delivered **operational back-office flows** (products, ingredients, stock, counts, suppliers) with **strong data consistency** guarantees via DB automation (**Postgres triggers**, indexes, **SQL/RPC**).",
        "Implemented **orders at scale**: **table sessions + split checks**, resilient **order lifecycle**, and safe **edit/void/restore** flows keeping stock accurate end-to-end (**RPC**, **transactional integrity**, **idempotent stock adjustments**).",
        "Built **reporting exports** for operations: **PDF/Excel** (sales + cash/audit), plus productivity-focused UI improvements (**i18n ES/EN**, search, sorting, confirmations).",
        "Built **Oceans HR ATS module** serving **hundreds of CVs/month per tenant**: **Kanban pipeline with drag-and-drop**, vacancy management, candidate profiles, **recruitment funnel reports**, **RBAC with company-level roles**, full **ES/EN i18n** (Next.js 16, React 19, TanStack Query v5, Zod v4, Supabase RLS).",
        "Engineered **AI-Powered CV Matching Engine**: **Gemini API with 3-model cascade fallback** for HA, **PDF text extraction**, **weighted scoring across 8 criteria**, **structured JSON output**, drag-and-drop upload UX and **automated candidate creation pipeline**.",
        "Implemented **SendGrid transactional email pipeline** triggered by **candidate pipeline phase changes** (automated and semi-automated flows): **templated emails per stage**, **Supabase triggers + queued dispatch**, **idempotency keys**, and **delivery audit log per tenant**.",
    ]
    for b in ocean_bullets:
        pdf.bullet(b)
    pdf.ln(0.8)

    # Argentine Federal Penitentiary Service
    pdf.job_header("Argentine Federal Penitentiary Service",
                   "Full-Stack Developer / AI Engineer / Software Engineer", "Jan 2024 - Present")
    pdf.sub_header("Sige2i internal platform (NestJS + Next.js + Python/FastAPI) - private, internal repos, no public links (federal confidentiality)")
    pdf.ln(0.5)

    afps_bullets = [
        "Act as the **requirements-discovery point of contact**: survey staff/leadership needs, identify manual workflows worth automating with **AI**, scope the solution and ship it end-to-end -- the in-house equivalent of pre-sales/technical discovery.",
        "Deployed **\"Movimientos de un Solo Mes\"** on **AWS**: a password-gated internal platform (EC2 + RDS) for controlled, authenticated access to monthly movement records.",
        "Built and deployed a **public reports portal outside the VPN**, redundantly on **AWS** and **Azure**, so external/public-facing statistics stay isolated from the internal network while internal systems remain air-gapped.",
        "Shipped an **on-prem NL intelligence chatbot** over a **90+ table legacy database**: **SQL-RAG** (deterministic parameterized retrieval, **zero hallucinated facts**, zero data egress) + **grounded 100% local LLM** (**Ollama/Qwen2.5**, **CPU-only**, air-gapped) with **LLM structured-output NL parsing**, inline **[n] citations**, and **NDJSON token streaming**; cut a >45s legacy self-join to **sub-second**.",
        "Led delivery of a **multi-platform ecosystem** (internal ops + public verification portal) with **secure data flows** and controlled access for multiple stakeholders (React, Next.js, TypeScript, NestJS, Prisma).",
        "Built **Python Face Matcher service** in production: **InsightFace buffalo_l** (ONNX CPU), **512-d L2-normalized embeddings**, NumPy cosine search + argpartition top-K, per-UID centroid enrollment, MariaDB BLOB storage (**FastAPI**).",
        "Built an **AI-assisted document intelligence pipeline**: **OCR** (Tesseract LSTM spa+eng), **hybrid PDF extraction** (PyPDF2 + pdf2image/Poppler @ 300 DPI), and **ASR** (faster-whisper INT8 CPU), all with **human-in-the-loop review**.",
        "Migrated **~110 GB of legacy iBase8 data** to **MySQL/MariaDB** across **80+ modules** (tables, PDFs, scanned images, ZIPs, Word docs) via custom **ETL pipelines** with chunked streaming and checksum integrity.",
        "Automated **operational reporting** (PDF/Excel/Word) with charts and filters replacing manual workflows; engineered **secure document verification** (HMAC-SHA256, JWT, watermarking, anti-capture).",
        "Delivered **containerized infrastructure** (Docker, NGINX, PM2, Debian) for **170 concurrent users** with **MFA**, **CSRF**, rate limiting, Helmet/CORS, and automated backups; **Redis/BullMQ** async job queues with in-memory fallback for zero-downtime resilience.",
    ]
    for b in afps_bullets:
        pdf.bullet(b)
    pdf.ln(0.2)

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
    pdf.ln(1.2)

    # -- Education --
    pdf.section_title("EDUCATION")
    pdf.edu_header("Higher Degree in Programming", "Teclab", "Aug 2022 - Aug 2024")
    pdf.bullet("Software fundamentals and delivery practices: databases, web development, UX, cloud basics, project management.")
    pdf.ln(0.5)
    pdf.edu_header("Full-Stack Web Development", "CoderHouse", "Jan 2022 - Mar 2023")
    pdf.bullet("Delivered multiple end-to-end projects: frontend and backend foundations, web app architecture (HTML5, React, Node.js, MongoDB, Express, GraphQL).")
    pdf.set_font("Helvetica", "", 7.3)
    bullet_indent = 3.5
    pdf.set_x(pdf.l_margin + bullet_indent)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pdf.get_string_width("Live: "), 3.4, "Live: ")
    pdf.set_text_color(*pdf.LINK_BLUE)
    coder_url = "https://react-e-commerce-j-sanso.vercel.app/"
    pdf.cell(pdf.get_string_width(coder_url), 3.4, coder_url, link=coder_url)
    pdf.ln(3.4)

    pdf.output("Jonathan-Sanso-Solutions-Engineer.pdf")
    print(f"PDF generated! Pages: {pdf.pages_count}, final Y: {pdf.get_y():.1f} / {pdf.h:.1f}")

if __name__ == "__main__":
    build()
