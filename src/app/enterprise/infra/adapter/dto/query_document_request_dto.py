from pydantic import BaseModel, Field


class QueryDocumentRequestDto(BaseModel):
    user_slug: str = Field(..., min_length=36, title="User ID", description="User slug with 36 characters")
    document_slug: str = Field(..., min_length=36, title="Document ID", description="Document slug with 36 characters")
    query: str = Field(..., min_length=3, max_length=500, title="Query", description="Query string with 3 to 500 characters")
