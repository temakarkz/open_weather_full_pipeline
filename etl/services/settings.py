import os
from pathlib import Path
from dotenv import load_dotenv

env = os.getenv("ENV", "local")
env_file = f".env.{env}"

env_path = Path(env_file)

if not env_path.exists():
    raise FileNotFoundError(f"File {env_path} does not exist")

print(f"Loading env: {env_path}")
load_dotenv(env_path)
