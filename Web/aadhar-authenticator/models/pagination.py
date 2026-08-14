from pydantic import BaseModel, Field

class PageInfo(BaseModel):
    skip: int = Field(ge=0)
    limit: int = Field(ge=1, le=100)
    total: int = Field(ge=0)
