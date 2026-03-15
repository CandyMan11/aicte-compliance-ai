from src.config import POLICY_DIR
from src.excel_loader import load_questions
from src.pdf_processor import load_all_pdfs
from src.evidence_combiner import combine_evidence
from src.prompt_builder import build_prompt
from src.llm_client import call_llm

def main():

    questions = load_questions("data/all_questions.xlsx")
    pdfs = load_all_pdfs(POLICY_DIR)
    evidence = combine_evidence(pdfs)

    first_question = questions.iloc[0][0]

    prompt = build_prompt(first_question, evidence)
    result = call_llm(prompt)

    print(result)

if __name__ == "__main__":
    main()