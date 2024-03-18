from pydantic import BaseModel, Field


class CategoryModel(BaseModel):
    name: str
    description: str


class CategoryResponseModel(CategoryModel):
    id: int

    class Config:
        from_attributes = True
