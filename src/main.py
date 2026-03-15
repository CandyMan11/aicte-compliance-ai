from src.config import POLICY_DIR, IMAGE_DIR
from src.excel_loader import load_questions
from src.pdf_processor import load_all_pdfs
from src.image_processor import load_all_images
from src.evidence_combiner import combine_evidence
from src.prompt_builder import build_prompt
from src.llm_client import call_llm


def main():

    print("\n--- AICTE Compliance Automation Pipeline ---\n")

    # 1. Load questions
    print("Loading questions...")
    questions = load_questions("data/all_questions.xlsx")
    print(f"Loaded {len(questions)} questions.\n")

    # 2. OCR PDFs
    print("Processing PDFs...")
    pdfs = load_all_pdfs(POLICY_DIR)
    print(f"OCR completed for {len(pdfs)} PDF documents.\n")

    # 3. Process images
    print("Processing images...")
    images = load_all_images(IMAGE_DIR)
    print(f"Loaded {len(images)} images.\n")

    # 4. Combine evidence
    print("Combining evidence...")
    evidence = combine_evidence(pdfs, images)
    print("Evidence combined successfully.\n")

    # 5. Select first question
    print("Preparing prompt...")
    first_question = questions.iloc[0].values[0]

    # 6. Build LLM prompt
    prompt = build_prompt(first_question, evidence)

    print("Prompt built successfully.\n")

    # 7. Call LLM
    print("Calling LLM API...")
    result = call_llm(prompt)

    print("\n--- LLM RESPONSE ---\n")
    print(result)


if __name__ == "__main__":
    main()