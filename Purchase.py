from pydantic import BaseModel

class Purchase(BaseModel):
  age: int
  EstimatedSalary: int