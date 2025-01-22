# ShinyLive API

## Instructions to Run the API

1. **Sync uv:**

   ```sh
   uv sync
   ```

   *Note: If you don't have uv installed, please visit the [[official page](https://docs.astral.sh/uv/getting-started/installation/) to install it.*

2. **Compile the ShinyLive site:**

   ```sh
   shinylive export excel_reader site
   ```

3. **Run the API with uvicorn:**

   ```sh
   uvicorn excel_reader.app:app --reload
   ```

4. **Access the API:**

   Open your web browser and go to `http://127.0.0.1:8000` to access the ShinyLive API.
