def combine_evidence(pdf_documents):
    combined = ""
    for filename, content in pdf_documents.items():
        combined += f"\n\n===== DOCUMENT: {filename} =====\n"
        combined += content
    return combined