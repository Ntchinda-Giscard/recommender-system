import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "ml_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipelines/__init__.py",
    "src/steps/__init__.py",
    "src/entity/__inti__.py",
    "src/entity/config_entity.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/data-loader.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f" Creating directory: {filedir} for the file name {filename} ")

    if (not os.path.exists(filepath)) or ((os.path.getsize) == 0):
        with open(filepath, "w") as f:
            pass
            # logging.info(f"Creating empty file: {filepath}")

    else:
        pass
        # logging.info(f"{filename} already exists")