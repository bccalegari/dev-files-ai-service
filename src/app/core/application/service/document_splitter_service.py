from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.app.enterprise.infra.config.logger import Logger


class DocumentSplitterService:
    def __init__(self, text_splitter: RecursiveCharacterTextSplitter, log: Logger):
        self.text_splitter = text_splitter
        self.log = log

    def split_text(self, text: str) -> list[str]:
        self.log.info(f"Splitting text into chunks")
        chunks = self.text_splitter.split_text(text)
        self.log.info(f"Split text into {len(chunks)} parts")
        return chunks
