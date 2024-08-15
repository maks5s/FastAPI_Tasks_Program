from pydantic import BaseModel


class SchemaTaskAdd(BaseModel):
    name: str
    description: str | None = None


class SchemaTask(SchemaTaskAdd):
    id: int
