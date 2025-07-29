import os

# ... The rest of our Django settings

BASE_URL = "http://localhost:8000"

USE_NGROK = (os.environ.get("USE_NGROK", "False") == "True"
             and os.environ.get("RUN_MAIN", None) != "True")
