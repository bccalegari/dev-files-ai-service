from src.app.core.application.factory.ollama_service_factory import OllamaServiceFactory
from src.app.core.application.factory.vector_store_service_factory import VectorStoreServiceFactory
from src.app.core.application.usecase.query_document_usecase import QueryDocumentUseCase
from src.app.enterprise.infra.config.logger import Logger


class QueryDocumentAppContainer:
    def __init__(self):
        log = Logger()
        vector_store_service = VectorStoreServiceFactory.execute()
        ollama_service = OllamaServiceFactory.execute()

        self.use_case = QueryDocumentUseCase(
            vector_store_service=vector_store_service,
            ollama_service=ollama_service,
            log=log
        )

    def get_usecase(self) -> QueryDocumentUseCase:
        return self.use_case
