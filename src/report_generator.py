import pandas as pd
import os


def export_to_excel(results, output_path="data/output/compliance_report.xlsx"):
    """
    Exports results to a well-structured Excel file (AICTE-style)
    """

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Rename columns
    df = df.rename(columns={
        "question": "Question",
        "final_decision": "Status",
        "confidence_score": "Score",
        "reasoning": "Remarks",
        "suggestions": "Suggestions"
    })

    # Add additional useful columns
    df["Max Score"] = 100
    df["Compliance"] = df["Status"]

    # Reorder columns (important for presentation)
    df = df[[
        "Question",
        "Status",
        "Score",
        "Max Score",
        "Compliance",
        "Remarks",
        "Suggestions"
    ]]

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save Excel with formatting
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Compliance Report")

    print(f"\nExcel report generated at: {output_path}")