from pathlib import Path
import yaml


def load_config(file:Path):
    with open(file, 'r') as f:
        return yaml.safe_load(f)