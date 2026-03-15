import os
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    text = ""
    images = convert_from_path(pdf_path)

    for img in images:
        text += pytesseract.image_to_string(img)

    return text

def load_all_pdfs(folder):
    pdf_texts = {}

    for file in os.listdir(folder):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(folder, file)
            pdf_texts[file] = extract_text_from_pdf(full_path)

    return pdf_texts