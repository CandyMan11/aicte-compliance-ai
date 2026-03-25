from src.config import POLICY_DIR, IMAGE_DIR
from src.excel_loader import load_questions
from src.pdf_processor import load_all_pdfs
from src.image_processor import load_all_images
from src.evidence_combiner import combine_evidence
from src.prompt_builder import build_prompt
from src.llm_client import call_llm
from src.response_parser import parse_llm_response
from src.scorer import score_response
from src.report_generator import export_to_excel


def main():

    print("\n=== AICTE Compliance Automation Pipeline ===\n")

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

    # 5. Evaluate all questions
    results = []

    print("Starting evaluation for all questions...\n")

    for index, row in questions.iterrows():

        question = row.values[0]

        print(f"\nProcessing Question {index + 1}:")
        print(question + "\n")

        # Build prompt
        prompt = build_prompt(question, evidence)

        # Call LLM (mocked / real later)
        result = call_llm(prompt)

        # Parse response
        parsed_result = parse_llm_response(result)

        # Score response
        scored_result = score_response(parsed_result)

        # Store result
        results.append({
            "question": question,
            "final_decision": scored_result["final_decision"],
            "confidence_score": scored_result["confidence_score"],
            "reasoning": scored_result["reasoning"],
            "suggestions": scored_result["suggestions"]
        })

        print(f"→ Decision: {scored_result['final_decision']}")

        # spacing between questions
        print("\n" + "=" * 60 + "\n")

    # 6. Final formatted report
    print("\n=== FINAL COMPLIANCE REPORT ===\n")

    for i, r in enumerate(results, start=1):

        print(f"Question {i}: {r['question']}\n")

        print(f"Decision          : {r['final_decision']}")
        print(f"Confidence Score  : {r['confidence_score']}")
        print(f"Reasoning         : {r['reasoning']}")
        print(f"Suggestions       : {r['suggestions']}")

        # clean spacing between entries
        print("\n" + "-" * 60 + "\n")

    # 7. Export report
    export_to_excel(results)


if __name__ == "__main__":
    main()