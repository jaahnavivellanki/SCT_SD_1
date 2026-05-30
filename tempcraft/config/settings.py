"""Application configuration settings."""
import os
from pathlib import Path

# App Information
APP_NAME = "TempCraft"
APP_VERSION = "1.0.0"
AUTHOR = "Software Engineering Student"

# Directories
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

# Ensure data dir exists
os.makedirs(DATA_DIR, exist_ok=True)

# Files
STORAGE_FILE = DATA_DIR / "storage.json"
LOG_FILE = BASE_DIR / "tempcraft.log"

# UI Settings
THEME_MODE = "dark"
COLOR_THEME = "dark-blue"
WINDOW_GEOMETRY = "900x650"
