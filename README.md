# ShinyLive API

## Introduction

This is a simple app to demonstrate how to serve a ShinyLive site using FastAPI.

## Instructions to Run the API

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/shinyLiveApi.git
   cd shinyLiveApi
   ```

2. **Sync uv:**

   ```sh
   uv sync
   ```

   *Note: If you don't have uv installed, please visit the [[official page](https://docs.astral.sh/uv/getting-started/installation/) to install it.*

3. **Compile the ShinyLive site:**

   ```sh
   shinylive export excel_reader site
   ```

4. **Run the API with uvicorn:**

   ```sh
   uvicorn main:app --reload
   ```

5. **Access the API:**

   Open your web browser and go to `http://127.0.0.1:8000` to access the ShinyLive API.
