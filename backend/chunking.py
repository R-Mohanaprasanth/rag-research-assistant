# chunking.py
def chunk_text(data, chunk_size=500, overlap=100):
    chunks = []

    for item in data:
        text = item["text"]

        for i in range(0, len(text), chunk_size - overlap):
            chunks.append({
                "content": text[i:i+chunk_size],
                "page": item["page"]
            })

    return chunks