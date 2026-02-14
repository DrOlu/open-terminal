import os

API_KEY = os.environ.get("OPEN_TERMINAL_API_KEY", "")
MAX_OUTPUT_LINES = int(os.environ.get("OPEN_TERMINAL_MAX_OUTPUT_LINES", "10000"))
