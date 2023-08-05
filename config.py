from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    API_KEY = os.getenv("API_KEY")