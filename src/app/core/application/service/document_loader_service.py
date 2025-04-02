import os

from langchain_community.document_loaders import S3FileLoader

from src.app.enterprise.infra.config.logger import Logger


class DocumentLoaderService:
    def __init__(self, log: Logger):
        self.log = log

    def load_document(self, url: str) -> str | None:
        self.log.info(f"Loading document from {url}")
        try:
            text = self._extract_text_from_pdf(url)

            if not text:
                raise Exception("No text extracted from PDF")

            self.log.info(f"Text extracted successfully from {url}")

            return text
        except Exception as e:
            self.log.error(f"Exception while loading document from {url}: {e}")
            return None

    def _extract_text_from_pdf(self, url: str) -> str:
        try:
            bucket_name = os.getenv("AWS_BUCKET_NAME")
            loader = S3FileLoader(bucket_name, url)
            documents = loader.load()
            return " ".join(document.page_content for document in documents if document.page_content)
        except Exception as e:
            self.log.error(f"Error extracting text from PDF: {e}")
            return ""