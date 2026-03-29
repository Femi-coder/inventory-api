from pydantic import BaseModel, Field

class Product(BaseModel):
    ProductID: int = Field(..., gt=0)
    Name: str
    UnitPrice: float = Field(..., gt=0)
    StockQuantity: int = Field(..., ge=0)
    Description: str