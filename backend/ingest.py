# ingest.py
import fitz

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    data = []

    for i, page in enumerate(doc):
        data.append({
            "text": page.get_text(),
            "page": i
        })

    return data