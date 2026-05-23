from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from models.dto import BookRequest

from graph.workflow import build_graph

import os

import uuid

from services.source_ingestion_service import (
    ingest_pdf_source
)

from services.chapter_regeneration_service import (
    prepare_regeneration_plan
)

from models.repair_models import (
    RepairRequest
)

from services.repair_service import (
    repair_book_continuity
)

from services.runtime_store import (
    RUN_CACHE
)

from services.pdf_service import (
    generate_pdf
)

from services.docx_service import (
    generate_docx
)

UPLOAD_DIR = "uploaded_sources"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


OUTPUT_DIR = "outputs"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


router = APIRouter()

graph = build_graph()


@router.post("/generate")

def generate_book(request: BookRequest):

    initial_state = {
        "run_id": str(uuid.uuid4()),
        "brief": request.dict(),
        "outline": {},
        "research_notes": [],
        "chapters": [],
        "memory": {},
        "fact_checks": [],
        "final_book": "",
        "front_matter": {},
        "back_matter": {},
    }

    result = graph.invoke(initial_state)

    RUN_CACHE[result["run_id"]] = result

    return {
        "run_id": result["run_id"],
        "outline": result["outline"],
        "book": result["final_book"],
        "evaluations": result.get("evaluations", []),
    }


@router.post("/upload-source")

async def upload_source(

    topic: str,

    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    result = ingest_pdf_source(
        file_path=file_path,
        topic=topic
    )

    return result

@router.post("/repair/{run_id}")

def repair_book(

    run_id: str,

    request: RepairRequest
):

    state = RUN_CACHE.get(run_id)

    if not state:

        return {
            "error":
                "Run not found"
        }

    result = repair_book_continuity(

            state=state,

            changed_chapter=request.changed_chapter,

            new_content=request.new_content
        )

    RUN_CACHE[run_id] = (
        result["updated_state"]
    )

    return {

        "message":
            "Repair completed",

        "affected_chapters":
            result["affected_chapters"],

        "updated_book":
            result["updated_state"][
                "final_book"
            ]
    }


@router.post("/export/pdf/{run_id}")

def export_pdf(run_id: str):

    state = RUN_CACHE.get(run_id)

    if not state:

        return {
            "error":
                "Run not found"
        }

    output_path = os.path.join(
        OUTPUT_DIR,
        f"{run_id}.pdf"
    )

    generate_pdf(

        book_text=state["final_book"],

        output_path=output_path
    )

    return FileResponse(

        output_path,

        media_type="application/pdf",

        filename=f"{run_id}.pdf"
    )


@router.post("/export/docx/{run_id}")

def export_docx(run_id: str):

    state = RUN_CACHE.get(run_id)

    if not state:

        return {
            "error":
                "Run not found"
        }

    output_path = os.path.join(
        OUTPUT_DIR,
        f"{run_id}.docx"
    )

    generate_docx(

        book_text=state["final_book"],

        output_path=output_path
    )

    return FileResponse(

        output_path,

        media_type=(
            "application/vnd.openxmlformats-"
            "officedocument.wordprocessingml.document"
        ),

        filename=f"{run_id}.docx"
    )


@router.get("/health")
def health_check():

    return {
        "status": "ok"
    }