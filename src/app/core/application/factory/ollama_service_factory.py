import os

from src.app.core.application.service.ollama_service import OllamaService
from src.app.enterprise.infra.config.logger import Logger


class OllamaServiceFactory:
    @staticmethod
    def execute() -> OllamaService:
        log = Logger()
        return OllamaService(
            model="gemma3:1b",
            base_url=os.getenv("OLLAMA_LLM_BASE_URL"),
            log=log
        )
