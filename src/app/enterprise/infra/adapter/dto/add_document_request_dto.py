from pydantic import BaseModel, Field


class AddDocumentRequestDto(BaseModel):
    url: str = Field(..., title="Document URL", description="Document URL")
    user_slug: str = Field(..., min_length=36, title="User ID", description="User slug with 36 characters")
    document_slug: str = Field(..., min_length=36, title="Document ID", description="Document slug with 36 characters")
