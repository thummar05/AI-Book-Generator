import os

from services.document_parser_service import (
    extract_pdf_text
)

from services.research_service import (
    ingest_research
)


def ingest_pdf_source(
    file_path,
    topic
):

    filename = os.path.basename(file_path)

    text = extract_pdf_text(file_path)

    ingest_research(
        topic=topic,
        source=filename,
        content=text
    )

    return {
        "source": filename,
        "status": "ingested"
    }