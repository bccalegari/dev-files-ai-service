import os

import chromadb
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from src.app.core.application.service.vector_store_service import VectorStoreService
from src.app.enterprise.infra.config.logger import Logger


class VectorStoreServiceFactory:
    @staticmethod
    def execute() -> VectorStoreService:
        log = Logger()
        return VectorStoreService(
            Chroma(
                collection_name="users_documents",
                embedding_function=OllamaEmbeddings(
                    model="nomic-embed-text", base_url=os.getenv("OLLAMA_EMBEDDING_BASE_URL")
                ),
                client=chromadb.HttpClient(os.getenv("CHROMA_DB_HOST"), int(os.getenv("CHROMA_DB_PORT", "8000")))
            ),
            log
        )
