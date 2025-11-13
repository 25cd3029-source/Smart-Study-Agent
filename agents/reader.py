from utils.pdf_utils import extract_text_from_pdf

class ReaderAgent:
    def __init__(self, file):
        self.file = file

    def run(self):
        return extract_text_from_pdf(self.file)
