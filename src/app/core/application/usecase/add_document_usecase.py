import time

from src.app.core.application.service.document_loader_service import DocumentLoaderService
from src.app.core.application.service.document_splitter_service import DocumentSplitterService
from src.app.core.application.service.vector_store_service import VectorStoreService
from src.app.enterprise.infra.adapter.dto.response_dto import ResponseDto
from src.app.enterprise.infra.config.logger import Logger

class AddDocumentUseCase:
    def __init__(
            self, document_loader_service: DocumentLoaderService,document_splitter_service: DocumentSplitterService,
            vector_store_service: VectorStoreService, log: Logger
    ):
        self.document_loader_service = document_loader_service
        self.document_splitter_service = document_splitter_service
        self.vector_store_service = vector_store_service
        self.log = log

    def execute(self, url: str, user_slug: str, document_slug: str):
        try:
            start = time.time()
            self.log.info(f"Start adding document {url} with slug {document_slug} for user {user_slug}")
            text = self.document_loader_service.load_document(url)

            if not text:
                raise Exception("No text extracted from PDF")

            splitted_text = self.document_splitter_service.split_text(text)

            ids = self.vector_store_service.add_embeddings(user_slug, document_slug, splitted_text)

            end = time.time()

            self.log.info(f"Document added in {end - start} seconds")

            return ResponseDto.success({"ids": ids})
        except Exception as e:
            self.log.error(f"Error adding document: {e}")
            raise e
