from src.app.core.application.factory.recursive_character_text_splitter_factory import \
    RecursiveCharacterTextSplitterFactory
from src.app.core.application.factory.vector_store_service_factory import VectorStoreServiceFactory
from src.app.core.application.service.document_loader_service import DocumentLoaderService
from src.app.core.application.service.document_splitter_service import DocumentSplitterService
from src.app.core.application.usecase.add_document_usecase import AddDocumentUseCase
from src.app.enterprise.infra.config.logger import Logger


class AddDocumentAppContainer:
    def __init__(self):
        log = Logger()
        recursive_character_text_splitter = RecursiveCharacterTextSplitterFactory.execute()

        document_loader_service = DocumentLoaderService(log=log)
        document_splitter_service = DocumentSplitterService(
            log=log,
            text_splitter=recursive_character_text_splitter
        )

        vector_store_service = VectorStoreServiceFactory.execute()

        self.use_case = AddDocumentUseCase(
            document_loader_service=document_loader_service,
            document_splitter_service=document_splitter_service,
            vector_store_service=vector_store_service,
            log=log
        )

    def get_usecase(self) -> AddDocumentUseCase:
        return self.use_case
