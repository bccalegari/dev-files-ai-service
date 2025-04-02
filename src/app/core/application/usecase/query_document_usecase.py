import time

from src.app.core.application.service.ollama_service import OllamaService
from src.app.core.application.service.vector_store_service import VectorStoreService
from src.app.enterprise.domain.error_code import ErrorCode
from src.app.enterprise.infra.adapter.dto.response_dto import ResponseDto
from src.app.enterprise.infra.config.logger import Logger


class QueryDocumentUseCase:
    def __init__(
            self, vector_store_service: VectorStoreService, ollama_service: OllamaService, log: Logger
    ):
        self.vector_store_service = vector_store_service
        self.ollama_service = ollama_service
        self.logger = log

    def execute(self, user_slug: str, document_slug: str, query: str) -> ResponseDto:
        try:
            start = time.time()
            self.logger.info(f"Start querying document {document_slug} for user {user_slug}")

            context = self.vector_store_service.search(user_slug, document_slug, query)

            if not context:
                raise Exception(f"Document {document_slug} not found")

            res = self.ollama_service.invoke(query, context)

            end = time.time()

            self.logger.info(f"Document queried in {end - start} seconds")

            return ResponseDto.success({"response": res})
        except Exception as e:
            self.logger.error(f"Error on query document usecase: {str(e)}")
            raise e
