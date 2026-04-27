from pypdf import PdfReader
r = PdfReader("c:/dev/portfolio/portfolio-j-sanso/assets/resume-fullstack-jonathan-sanso-2026.pdf")
for i, page in enumerate(r.pages):
    if "/Annots" in page:
        for a in page["/Annots"]:
            obj = a.get_object()
            if obj.get("/Subtype") == "/Link":
                action = obj.get("/A")
                if action and "/URI" in action:
                    print(f"page {i}: {action['/URI']} rect={obj.get('/Rect')}")
