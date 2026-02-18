# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework to understand HTTP methods, routing, request/response handling, and data validation. Create a complete API that handles CRUD operations and demonstrates best practices for web service development.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description

Develop a REST API using FastAPI that manages a collection of items (e.g., books, tasks, products). Your API should handle common operations like retrieving all items, getting a specific item, creating new items, updating existing items, and deleting items. Implement proper HTTP status codes and error handling throughout the application.

#### Requirements

Completed program should:

- Define FastAPI application with appropriate imports and initialization
- Implement GET endpoint to retrieve all items
- Implement GET endpoint to retrieve a single item by ID
- Implement POST endpoint to create new items with validation
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Use Pydantic models for request/response data validation
- Handle errors gracefully with appropriate HTTP status codes
- Include proper documentation and type hints for all endpoints

### 🛠️ Test and Document Your API

#### Description

Test your API endpoints using FastAPI's built-in interactive documentation tools and ensure all operations work correctly. Verify that validation works as expected and that error cases are handled appropriately.

#### Requirements

Completed program should:

- Access and use Swagger UI documentation at `/docs`
- Test all CRUD endpoints interactively
- Verify that invalid request data is rejected
- Confirm proper HTTP status codes are returned for success and error cases
- Document the purpose of each endpoint with docstrings
