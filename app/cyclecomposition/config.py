import os


def get_api_url() -> str:
    host = os.environ.get("API_HOST", "localhost")
    print("HOST: " + host)
    port = 8000 if host == "localhost" else 5005
    return f"http://{host}:{port}"
