from pypdf import PdfReader


def extract_pdf_text(file_path):

    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:

        text = page.extract_text()

        if text:

            pages.append(text)

    return "\n".join(pages)