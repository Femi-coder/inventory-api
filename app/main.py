from fastapi import FastAPI, HTTPException
from app.database import collection
from app.models import Product
import requests

app = FastAPI()

# Get all products
@app.get("/getAll")
def get_all():
    products = []
    for item in collection.find():
        item["_id"] = str(item["_id"])
        products.append(item)
    return products


# Get single product
@app.get("/getSingleProduct/{product_id}")
def get_single(product_id: int):
    product = collection.find_one({"ProductID": product_id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Add new product
@app.post("/addNew")
def add_product(product: Product):
    collection.insert_one(product.dict())
    return {"message": "Product added"}


# Delete product
@app.delete("/deleteOne/{product_id}")
def delete_product(product_id: int):
    result = collection.delete_one({"ProductID": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}


# Starts with
@app.get("/startsWith/{letter}")
def starts_with(letter: str):
    return list(collection.find(
        {"Name": {"$regex": f"^{letter}", "$options": "i"}},
        {"_id": 0}
    ))


# Pagination
@app.get("/paginate")
def paginate(start_id: int, end_id: int):
    return list(collection.find(
        {"ProductID": {"$gte": start_id, "$lte": end_id}},
        {"_id": 0}
    ).limit(10))


# Convert USD → EUR
@app.get("/convert/{product_id}")
def convert_price(product_id: int):
    product = collection.find_one({"ProductID": product_id})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    usd_price = product["UnitPrice"]

    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    eur_rate = response.json()["rates"]["EUR"]

    return {
        "ProductID": product_id,
        "Price_EUR": round(usd_price * eur_rate, 2)
    }