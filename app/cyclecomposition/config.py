import os


def get_api_url() -> str:
    host = os.environ.get("API_HOST", "localhost")
    port = 8000 if host == "localhost" else 8000
    return f"http://{host}:{port}"
