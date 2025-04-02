from langchain_ollama import OllamaLLM

from src.app.enterprise.infra.config.logger import Logger


class OllamaService:
    def __init__(self, model: str, base_url: str, log: Logger):
        self.log = log
        self.model = OllamaLLM(model=model, base_url=base_url)


    def invoke(self, query: str, context: str) -> str:
        self.log.info(f"Invoking ollama")

        query_with_context = f"""
        You are an intelligent assistant that answers questions based on provided context.

        Context:
        {context}

        Question:
        {query}

        Please answer the question based solely on the provided context and without using any external information.
        Format the response as a single sentence or a short paragraph without any special formatting.
        If the information to answer the question is not in the context, please answer with "I don't have enough information to answer the question."
        """

        res = self.model.invoke(query_with_context)

        self.log.info(f"Ollama invoked successfully")

        return res
