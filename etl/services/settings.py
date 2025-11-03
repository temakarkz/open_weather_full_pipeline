import os
from pathlib import Path
from dotenv import load_dotenv

env = os.getenv("ENV", "local")
env_file = f".env.{env}"

BASE_DIR = Path(__file__).resolve().parents[2]

env_path = BASE_DIR / env_file

if not env_path.exists():
    raise FileNotFoundError(f"File {env_path} does not exist")

print(f"Loading env: {env_path}")
load_dotenv(env_path)
