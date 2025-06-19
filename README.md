# AI Service

> **Study project developed for learning purposes.**

This is the AI microservice for the **DevFiles** platform.  
It handles file analysis, embeddings, and query resolution using locally hosted LLMs such as `gemma:3b` and `nomic-embed-text` via the **Ollama** runtime.

The service exposes an HTTP API and is designed to work as part of a multi-container deployment managed by Docker Compose.

> This repository/module is part of the [DevFiles Monorepo](https://github.com/bccalegari/dev-files-monorepo).

## Features

- Accepts file content and user queries for AI-based contextual responses
- Generates and stores embeddings for semantic search
- Supports Retrieval-Augmented Generation (RAG) flow
- Communicates with Ollama LLMs running locally
- RESTful interface for integration with the main API
- Uses ChromaDB for vector storage and retrieval
- Authentication through API KEY


## Technologies Used

- Python 3.11+
- Flask (Web framework)
- LangChain (For building AI applications)
- Pydantic (For data validation)
- ChromaDB (for vector storage)
- Ollama – Local LLMs (embedding and conversational models)
- Docker – Containerized execution

## Prerequisites
- Docker installed
- devfiles-network network created

```bash
docker network create devfiles-network
```

## Running locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com/bccalegari/dev-files-ai-service.git
    ```

2. **Navigate to the project directory:**
   ```bash
    cd dev-files-ai-service
    ```

3. **Create a `.env` file:**
    ```bash
    cp .env.example .env
    ```
    Copy the `.env.example` to `.env` and fill in the required environment variables.

4. **Run dev compose:**
    ```bash
    docker compose -f docker-compose.dev.yml up
    ```

## Integration with DevFiles API
This service is integrated with the main dev-files-api service through HTTP requests. The API endpoints are designed to handle file embeddings and user queries, returning AI-generated responses.

## Logging
Logs are managed using the `loguru` library, which provides a simple and flexible logging interface. They are stored in a folder named `logs` in the project root.

Trace ID are received from through the HTTP headers and are used to correlate logs across services.

---

> **Study project developed for learning purposes.**

Built with ❤️ by Bruno Calegari