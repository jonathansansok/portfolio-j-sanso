"""Generate Jonathan Sanso's resume PDF with fpdf2."""
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
        self.set_font("Helvetica", "B", 7.5)
        self.set_text_color(*self.BLACK)
        lw = self.get_string_width(label + " ")
        self.cell(lw, 3.5, label + " ")
        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 3.5, value, new_x="LMARGIN", new_y="NEXT")

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
        self.set_font("Helvetica", "", 7.3)
        self.set_text_color(*self.DARK)
        bullet_indent = 3.5
        self.cell(bullet_indent, 3.4, "- ")
        self.multi_cell(self.w - self.l_margin - self.r_margin - bullet_indent, 3.4, text, new_x="LMARGIN", new_y="NEXT")

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
             "Full-Stack Developer | React/Next.js, Node.js/NestJS | Multi-tenant SaaS (Supabase/Postgres RLS)",
             align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 3.5,
             "Buenos Aires, Argentina | +54 9 11 6912-3268 | jonasans2@live.com.ar | English B2",
             align="C", new_x="LMARGIN", new_y="NEXT")

    # Links
    pdf.set_font("Helvetica", "", 7.5)
    links = [
        ("Portfolio", "https://portfolio-sanso-jonathan.netlify.app/"),
        ("GitHub", "https://github.com/jonathansansok"),
        ("LinkedIn", "https://www.linkedin.com/in/jonathan-sanso-fullstack/"),
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
        "Full-Stack Developer with 3+ years building multi-tenant SaaS products end-to-end. "
        "Core expertise in tenant isolation (Supabase RLS/Policies), POS/orders lifecycle, RBAC, "
        "AI document intelligence (OCR/NLP/STT), and security-first architecture (MFA, CSRF, HMAC/JWT). "
        "Daily stack: Next.js, React, TypeScript, Tailwind, Supabase/PostgreSQL, NestJS, Prisma. "
        "Experienced with Docker, NGINX, AWS, Terraform, and Python (FastAPI, Pandas). Mercado Pago API integration."
    ), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1.5)

    # -- Technical Skills --
    pdf.section_title("TECHNICAL SKILLS")
    skills = [
        ("Frontend:", "Next.js, React, TypeScript, Tailwind CSS, HTML5, CSS3, JavaScript, Zustand, TanStack Query, Zod, react-hook-form, @dnd-kit, ShadCN UI"),
        ("Backend:", "NestJS, Node.js, Prisma, FastAPI (Python), Express, GraphQL"),
        ("Databases:", "PostgreSQL (Supabase RLS, Triggers, RPC, Indexes), MySQL, MariaDB, MongoDB, SQL Server"),
        ("DevOps & Infra:", "Docker, NGINX, Debian/Linux, AWS (EC2, RDS, S3, CloudFront), Terraform, Vercel, Git/GitHub"),
        ("AI & Data:", "Gemini API (LLM cascade), Tesseract OCR, NLP, Speech-to-Text, Pandas, jsPDF, ExcelJS"),
        ("Security:", "Auth0, MFA/2FA, CSRF, Helmet/CORS, HMAC-SHA256, JWT, Rate Limiting, Input Sanitization"),
    ]
    for label, value in skills:
        pdf.skill_line(label, value)
    pdf.ln(1.5)

    # -- Professional Experience --
    pdf.section_title("PROFESSIONAL EXPERIENCE")

    # Ocean Stack
    pdf.job_header("Ocean Stack", "Full-Stack Developer (Multi-tenant SaaS)", "Dec 2025 - Present")
    # Products line with links
    pdf.set_font("Helvetica", "I", 7)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pdf.get_string_width("Products: "), 3.5, "Products: ")
    pdf.set_text_color(*pdf.LINK_BLUE)
    pdf.cell(pdf.get_string_width("Niappa POS"), 3.5, "Niappa POS", link="https://niappa-restaurant.vercel.app/")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pdf.get_string_width(" | "), 3.5, " | ")
    pdf.set_text_color(*pdf.LINK_BLUE)
    pdf.cell(pdf.get_string_width("Oceans HR (ATS)"), 3.5, "Oceans HR (ATS)", link="https://oceans-hr.vercel.app/")
    pdf.ln(3.5)
    pdf.ln(0.5)

    ocean_bullets = [
        "Shipped weekly product increments in a structured delivery loop: Figma as source of truth, daily alignment with CTO + PM, iterative releases, and UX/UI polishing (Next.js, TypeScript, Tailwind).",
        "Implemented tenant-safe isolation and role-based permissions across modules so each business only sees and mutates its own data (Supabase Postgres, RLS/Policies).",
        "Delivered operational back-office flows (products, ingredients, stock, counts, suppliers) with strong data consistency guarantees via DB automation (Postgres triggers, indexes, SQL/RPC).",
        "Implemented orders at scale: table sessions + split checks, resilient order lifecycle, and safe edit/void/restore flows keeping stock accurate end-to-end (RPC, transactional integrity, idempotent stock adjustments).",
        "Built reporting exports for operations: PDF/Excel (sales + cash/audit), plus productivity-focused UI improvements (i18n ES/EN, search, sorting, confirmations).",
        "Built Oceans HR ATS module: Kanban pipeline with drag-and-drop, vacancy management, candidate profiles with notes/comments, recruitment funnel reports, RBAC with company-level roles, full ES/EN i18n (Next.js 16, React 19, TanStack Query v5, Zod v4, @dnd-kit, Supabase RLS).",
        "Engineered AI-Powered CV Matching Engine: LLM integration (Gemini API with 3-model cascade fallback for HA), PDF text extraction, weighted scoring across 8 criteria (skills, seniority, role, education, location, salary, language, industry), structured JSON output, and full frontend UX -- drag-and-drop upload, color-coded score cards, per-criteria progress bars, and automated candidate creation pipeline (Next.js App Router, Supabase RLS).",
    ]
    for b in ocean_bullets:
        pdf.bullet(b)
    pdf.ln(0.8)

    # Argentine Federal Penitentiary Service
    pdf.job_header("Argentine Federal Penitentiary Service",
                   "Full-Stack Developer / AI Engineering", "Jan 2024 - Present")
    pdf.sub_header("Private repos")
    pdf.ln(0.5)

    afps_bullets = [
        "Led delivery of a two-platform ecosystem (internal ops + public verification portal) with secure data flows and controlled access for multiple stakeholders (React, Next.js, TypeScript, Tailwind, NestJS, Prisma).",
        "Built an AI-assisted document intelligence pipeline: extract and summarize from scans/images/audio with human-in-the-loop review (Python, FastAPI, Tesseract OCR, NLP, Speech-to-Text).",
        "Automated operational reporting (PDF/Excel/Word) with charts, filters, and standardized formatting replacing manual workflows (TypeScript, Pandas).",
        "Engineered secure document verification: time-limited access, cryptographic validation, anti-exfiltration controls (HMAC-SHA256, JWT, watermarking).",
        "Implemented end-to-end security (MFA, CSRF, input sanitization, rate limiting, Helmet/CORS) and delivered containerized infrastructure with reverse proxying and automated backups (Docker, NGINX, Debian).",
        "Built secure integration layer: signed requests, idempotency, clock-skew validation, file integrity checks (SHA-256).",
        "Leveraged Redis for async job queues (audit logging, cross-service publishing, scheduled sync) with BullMQ, plus server-side caching with automatic in-memory fallback for zero-downtime resilience.",
    ]
    for b in afps_bullets:
        pdf.bullet(b)
    pdf.ln(0.8)

    # VirtuaState
    pdf.job_header("VirtuaState", "Frontend Developer", "May 2022 - Dec 2023")
    # VirtuaState bullet with link
    pdf.set_font("Helvetica", "", 7.3)
    pdf.set_text_color(*pdf.DARK)
    bullet_indent = 3.5
    pdf.cell(bullet_indent, 3.4, "- ")
    text_before = "Built a responsive marketing/portfolio site for a VR/AR studio with SEO and performance optimizations (HTML5, CSS3, JavaScript, mobile-first). Live: "
    pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin - bullet_indent, 3.4, text_before, new_x="END", new_y="LAST")
    # Go back to append link on the same line
    x_end = pdf.get_x()
    y_end = pdf.get_y()
    pdf.set_xy(x_end, y_end)
    pdf.set_text_color(*pdf.LINK_BLUE)
    pdf.cell(pdf.get_string_width("virtuastate.net"), 3.4, "virtuastate.net", link="https://www.virtuastate.net/")
    pdf.ln(3.4)
    pdf.ln(1.5)

    # -- Education --
    pdf.section_title("EDUCATION")
    pdf.edu_header("Higher Degree in Programming", "Teclab", "Aug 2022 - Aug 2024")
    pdf.bullet("Software fundamentals and delivery practices: databases, web development, UX, cloud basics, project management.")
    pdf.ln(0.5)
    pdf.edu_header("Full-Stack Web Development", "CoderHouse", "Jan 2022 - Mar 2023")
    # CoderHouse bullet with live project link
    pdf.set_font("Helvetica", "", 7.3)
    pdf.set_text_color(*pdf.DARK)
    bullet_indent = 3.5
    pdf.cell(bullet_indent, 3.4, "- ")
    text_before = "Delivered multiple end-to-end projects: frontend and backend foundations, web app architecture (HTML5, EJS, CSS/SASS, React, Node.js, MongoDB, Express, GraphQL). "
    pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin - bullet_indent, 3.4, text_before, new_x="END", new_y="LAST")
    x_end = pdf.get_x()
    y_end = pdf.get_y()
    pdf.set_xy(x_end, y_end)
    pdf.set_text_color(*pdf.LINK_BLUE)
    pdf.cell(pdf.get_string_width("Live project"), 3.4, "Live project", link="https://react-e-commerce-j-sanso.vercel.app/")
    pdf.ln(3.4)

    pdf.output("resume-fullstack-jonathan-sanso-2026.pdf")
    print(f"PDF generated! Pages: {pdf.pages_count}, final Y: {pdf.get_y():.1f} / {pdf.h:.1f}")

if __name__ == "__main__":
    build()
