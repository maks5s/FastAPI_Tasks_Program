from pydantic import BaseModel, ConfigDict


class SchemaTaskAdd(BaseModel):
    name: str
    description: str | None = None


class SchemaTask(SchemaTaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
