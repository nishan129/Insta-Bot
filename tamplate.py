import os 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)")

list_file = [
    "src/__init__.py",
    "src/instabot/__init__.py",
    "src/instabot/config/agents.yaml",
    "src/instabot/config/task.yaml",
    "src/instabot/task.py",
    "src/instabot/agents.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    ""
]


for listpath in list_file:
    filepath = Path(listpath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file : {filename}")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        
        logging.info(f"Creating empty file : {filepath}")
        
    else:
        logging.info(f"{filename} file is already exists")
        