from pathlib import Path
from typing import Iterable, List
from langchain_classic.schema import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)

from multi_doc_chat.custom_logger import CustomLogger as log
from multi_doc_chat.custom_exception import DocumentPortalException


SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def load_documents_from_folder(folder_path: Path) -> List[Document]:
    """Load all supported documents from a folder."""
    docs: List[Document] = []

    try:
        if not folder_path.exists() or not folder_path.is_dir():
            raise ValueError(f"Invalid folder path: {folder_path}")

        files = [
            p for p in folder_path.iterdir()
            if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
        ]

        if not files:
            log.warning("No supported documents found", folder=str(folder_path))
            return []

        for p in files:
            ext = p.suffix.lower()

            if ext == ".pdf":
                loader = PyPDFLoader(str(p))
            elif ext == ".docx":
                loader = Docx2txtLoader(str(p))
            elif ext == ".txt":
                loader = TextLoader(str(p), encoding="utf-8")
            else:
                continue  # already filtered, just safety

            docs.extend(loader.load())

        log.info(
            "Documents loaded from folder",
            folder=str(folder_path),
            files=len(files),
            documents=len(docs),
        )
        return docs

    except Exception as e:
        log.error("Failed loading documents from folder", error=str(e))
        raise DocumentPortalException("Error loading documents from folder", e) from e
    