# ECommerce Documentation

This Python Django project implements a CRUD API using the Django REST framework, serializers, and view sets for managing products.

## Products Endpoint

### Get a List of All Products

- **URL**: `/products/`
- **HTTP Method**: GET
- **Description**: Retrieve a list of all products.
- **cURL**:
  curl --location 'https://atrishbhawna.pythonanywhere.com/products/' \
  --data ''

- **Response**:
  - **Status Code**: 200 OK
  - **Response Body**: A JSON array containing serialized data of all products. Each product includes attributes such as id, name, description, price, stock, created_at, manufacturer, category, is_featured, weight, dimensions, is_available, rating, brand, is_discounted, and discount_price.
  - **Response Example**:
    ```json
    [
        {
            "id": 1,
            "name": "Product 1",
            "description": "Description of Product 1",
            "price": 19.99,
            "stock": 100,
            "created_at": "2023-10-23T12:00:00Z",
            "manufacturer": "Manufacturer A",
            "category": "Electronics",
            "is_featured": true,
            "weight": 1.5,
            "dimensions": "5x5x5",
            "is_available": true,
            "rating": 4.5,
            "brand": "Brand X",
            "is_discounted": false,
            "discount_price": null
        },
        {
            "id": 2,
            "name": "Product 2",
            "description": "Description of Product 2",
            "price": 29.99,
            "stock": 50,
            "created_at": "2023-10-24T14:30:00Z",
            "manufacturer": "Manufacturer B",
            "category": "Clothing",
            "is_featured": false,
            "weight": null,
            "dimensions": null,
            "is_available": true,
            "rating": null,
            "brand": null,
            "is_discounted": true,
            "discount_price": 24.99
        }
    ]
    ```

### Get Product Details by ID

- **URL**: `/products/{product_id}/`
- **HTTP Method**: GET
- **Description**: Retrieve detailed information about a specific product based on its unique identifier (product_id).
- **cURL**:
curl --location 'https://atrishbhawna.pythonanywhere.com/products/2/' \
--data ''

- **Response**:
  - **Status Code**: 200 OK
  - **Response Body**: A JSON object containing serialized data of the specified product, including attributes like id, name, description, price, stock, created_at, manufacturer, category, is_featured, weight, dimensions, is_available, rating, brand, is_discounted, and discount_price.
  - **Response Example**:
    ```json
    {
        "id": 1,
        "name": "Product 1",
        "description": "Description of Product 1",
        "price": 19.99,
        "stock": 100,
        "created_at": "2023-10-23T12:00:00Z",
        "manufacturer": "Manufacturer A",
        "category": "Electronics",
        "is_featured": true,
        "weight": 1.5,
        "dimensions": "5x5x5",
        "is_available": true,
        "rating": 4.5,
        "brand": "Brand X",
        "is_discounted": false,
        "discount_price": null
    }
    ```

### Create a New Product

- **URL**: `/products/`
- **HTTP Method**: POST
- **Description**: Create a new product with specified attributes. The request body should contain JSON data with product details.
- **cURL**:
  curl --location 'https://atrishbhawna.pythonanywhere.com/products/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Product 1",
    "description": "Description of Product 1",
    "price": 19.99,
    "stock": 100,
    "manufacturer": "Manufacturer A",
    "category": "Electronics",
    "is_featured": true,
    "weight": 1.5,
    "dimensions": "5x5x5",
    "is_available": true,
    "rating": 4.5,
    "brand": "Brand X",
    "is_discounted": false,
    "discount_price": null
}'
- **Response**:
  - **Status Code**: 201 Created
  - **Response Body**: A JSON object containing serialized data of the newly created product, including its unique id.
  - **Request Body Example**:
    ```json
    {
        "name": "New Product",
        "description": "Description of New Product",
        "price": 25.99,
        "stock": 75,
        "manufacturer": "Manufacturer C",
        "category": "Electronics",
        "is_featured": true,
        "weight": 2.0,
        "dimensions": "6x6x6",
        "is_available": true,
        "rating": 4.2,
        "brand": "Brand Y",
        "is_discounted": true,
        "discount_price": 21.99
    }
    ```
  - **Response Example**:
    ```json
    {
        "id": 3,
        "name": "New Product",
        "description": "Description of New Product",
        "price": 25.99,
        "stock": 75,
        "created_at": "2023-10-25T09:45:00Z",
        "manufacturer": "Manufacturer C",
        "category": "Electronics",
        "is_featured": true,
        "weight": 2.0,
        "dimensions": "6x6x6",
        "is_available": true,
        "rating": 4.2,
        "brand": "Brand Y",
        "is_discounted": true,
        "discount_price": 21.99
    }
    ```

### Update Product Details

- **URL**: `/products/{product_id}/`
- **HTTP Method**: PUT
- **Description**: Update the details of a specific product based on its unique identifier (product_id). The request body should contain JSON data with the attributes to be updated.
- **cURL**:
curl --location --request PUT 'https://atrishbhawna.pythonanywhere.com/products/2/' \
--header 'Content-Type: application/json' \
--data '{
    "name" : "product1",
    "price": 20.0
}'

- **Response**:
  - **Status Code**: 200 OK
  - **Response Body**: A JSON object containing serialized data of the updated product.
  - **Request Body Example**:
    ```json
    {
        "name": "product1",
        "price": 20.00
    }
    ```
  - **Response Example**:
    ```json
    {
        "id": 1,
        "name": "Product 1",
        "description": "Description of Product 1",
        "price": 23.99,
        "stock": 100,
        "created_at": "2023-10-23T12:00:00Z",
        "manufacturer": "Manufacturer A",
        "category": "Electronics",
        "is_featured": true,
        "weight": 1.5,
        "dimensions": "5x5x5",
        "is_available": false,
        "rating": 4.5,
        "brand": "Brand X",
        "is_discounted": false,
        "discount_price": null
    }
    ```

### Delete a Product

- **URL**: `/products/{product_id}/`
- **HTTP Method**: DELETE
- **Description**: Delete a specific product based on its unique identifier (product_id).
-**cURL**:
curl --location --request DELETE 'https://atrishbhawna.pythonanywhere.com/products/2/' \
--data ''

- **Response**:
  - **Status Code**: 204 No Content

## Products in Category Endpoint

### Get Products by Category

- **URL**: `/find_products_in_category/`
- **HTTP Method**: POST
- **Description**: Retrieve and serialize products based on a specified category. The category is provided as a query parameter in the URL.
- **cURL**:
curl --location --request GET 'https://atrishbhawna.pythonanywhere.com/find_products_in_category' \
--header 'Content-Type: application/json' \
--data '{
    "category": "other"
}'

- **Query Parameter**:
  - `category`: The category for which products should be retrieved.
- **Response**:
  - **Status Code**: 200 OK
  - **Response Body**: A JSON array containing serialized data of products in the specified category.
  - **Request**:
    - **Content-Type**: application/json
    - **Request Body Example**:
      ```json
      {
          "category": "Electronics"
      }
      ```
  - **Response Example**:
    ```json
    [
        {
            "id": 1,
            "name": "Product 1",
            "description": "Description of Product 1",
            "price": 19.99,
            "stock": 100,
            "created_at": "2023-10-23T12:00:00Z",
            "manufacturer": "Manufacturer A",
            "category": "Electronics",
            "is_featured": true,
            "weight": 1.5,
            "dimensions": "5x5x5",
            "is_available": true,
            "rating": 4.5,
            "brand": "Brand X",
            "is_discounted": false,
            "discount_price": null
        },
        {
            "id": 3,
            "name": "New Product",
            "description": "Description of New Product",
            "price": 25.99,
            "stock": 75,
            "created_at": "2023-10-25T09:45:00Z",
            "manufacturer": "Manufacturer C",
            "category": "Electronics",
            "is_featured": true,
            "weight": 2.0,
            "dimensions": "6x6x6",
            "is_available": true,
            "rating": 4.2,
            "brand": "Brand Y",
            "is_discounted": true,
            "discount_price": 21.99
        }
    ]
    ```
