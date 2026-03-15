def combine_evidence(pdf_documents, image_documents):
    """
    Combine PDF text evidence and image evidence
    """

    combined = ""

    # add PDF evidence
    for filename, content in pdf_documents.items():

        combined += f"\n\n===== DOCUMENT: {filename} =====\n"

        combined += content

    # add image evidence
    for filename in image_documents.keys():

        combined += f"\n\n===== IMAGE: {filename} =====\n"

        combined += "[Image evidence available]\n"

    return combined