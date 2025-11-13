import fitz

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF"""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text()
    return text
