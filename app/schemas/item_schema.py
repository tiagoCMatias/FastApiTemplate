from pydantic import BaseModel, field_validator


class ItemCreate(BaseModel):
    name: str
    price: float
    brand: str
    quantity: int

    @field_validator('price')
    def check_price_format(cls, value):
        if value <= 0:
            raise ValueError('Price must be higher than 0')
        return value

    @field_validator('quantity')
    def check_quantity_format(cls, value):
        if value <= 0:
            raise ValueError('Quantity must be higher than 0')
        return value


