import uuid

from langchain_chroma import Chroma

from src.app.enterprise.infra.config.logger import Logger


class VectorStoreService:

    def __init__(self, chroma: Chroma, log: Logger):
        self.chroma = chroma
        self.log = log

    def add_embeddings(self, user_slug: str, document_slug: str, splitted_text: list[str]):
        self.log.info(f"Adding embeddings for user {user_slug} and document {document_slug}")

        metadatas = [{"user_slug": user_slug, "document_slug": document_slug} for _ in range(len(splitted_text))]
        ids = [f"user:{user_slug}:document:{document_slug}:chunk:{str(uuid.uuid4())}" for _ in range(len(splitted_text))]

        return self.chroma.add_texts(
            texts=splitted_text,
            metadatas=metadatas,
            ids=ids,
        )

    def search(self, user_slug: str, document_slug: str, query) -> str:
        self.log.info(f"Searching for user {user_slug} and document {document_slug} with query {query}")
        documents = self.chroma.similarity_search(
            query=query,
            k=100,
            filter={"document_slug": document_slug}
        )
        return "\n\n".join([doc.page_content for doc in documents])
