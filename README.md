# Alan Data Connector Template

This repository serves as a starting point for developing data connectors for [Alan](https://alan.de) using Python and FastAPI.

## Prerequisites

- Python >= 3.10 including pip and venv

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/alan-data-connector-template.git <your-connector-name>
   cd <your-connector-name>
   ```

2. **Create a virtual environment:**

   ```sh
   python3 -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On macOS/Linux:

     ```sh
     source .venv/bin/activate
     ```

   - On Windows:

     ```sh
     .\.venv\Scripts\activate
     ```

4. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, use the following command:

```sh
python main.py
```

or

```sh
API_KEY=1234 python main.py
```

## Example CURL Command

You can use the following CURL command for testing:

```bash
   curl -X 'POST' \
   'http://localhost:9001/query' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -H 'X-API-KEY: 1234' \
   -d '{
   "message": "Hello World"
   }'
```
