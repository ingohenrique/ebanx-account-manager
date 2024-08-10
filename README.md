# Ebanx Account Manager

Basic Finace operations API using Flask.

## Requirements

- Docker

## How to Run

1. **Build the Docker Image:**

    ```bash
    docker build -t my-app .
    ```

2. **Run the Container:**

    ```bash
    docker run -p 8000:8000 my-app
    ```

3. **Access the API:**

    - The API will be available at `http://localhost:8000`.

## Main Endpoints

- **POST /reset:** Resets the application state.
- **GET /balance:** Checks the balance of an account.
- **POST /event:** Handles deposit, withdrawal, or transfer.
