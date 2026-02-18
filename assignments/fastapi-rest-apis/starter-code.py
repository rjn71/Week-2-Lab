"""
FastAPI REST API Starter Code
Build your REST API by completing the endpoints below.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="Item Management API", description="A simple REST API for managing items")

# Define your data model using Pydantic
class Item(BaseModel):
    """Item model for request/response validation"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

# Sample data - in a real app, this would be a database
items_database: List[Item] = [
    Item(id=1, name="Example Item", description="This is an example item", price=9.99)
]

# TODO: Implement GET endpoint to retrieve all items
# Route: GET /items
# Returns: List of all items


# TODO: Implement GET endpoint to retrieve a single item by ID
# Route: GET /items/{item_id}
# Returns: Single item with matching ID or 404 error


# TODO: Implement POST endpoint to create a new item
# Route: POST /items
# Parameters: Item data in request body
# Returns: Created item with assigned ID


# TODO: Implement PUT endpoint to update an item
# Route: PUT /items/{item_id}
# Parameters: Item ID in path, updated data in request body
# Returns: Updated item or 404 error


# TODO: Implement DELETE endpoint to remove an item
# Route: DELETE /items/{item_id}
# Parameters: Item ID in path
# Returns: Success message or 404 error


if __name__ == "__main__":
    import uvicorn
    # Run with: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
