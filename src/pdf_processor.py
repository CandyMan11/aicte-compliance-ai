import os
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path: str):
    """
    Convert PDF to images then perform OCR
    """

    text = ""

    images = convert_from_path(pdf_path, dpi=300)

    for img in images:
        text += pytesseract.image_to_string(img)

    return text


def load_all_pdfs(folder: str):
    """
    Load and OCR all PDFs in a folder
    """

    pdf_texts = {}

    for file in os.listdir(folder):

        if file.lower().endswith(".pdf"):

            full_path = os.path.join(folder, file)

            pdf_texts[file] = extract_text_from_pdf(full_path)

    return pdf_texts