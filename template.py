import os
from pathlib import pathlib
import logging

logging.basicConfig(level=logging.INFO, format='[%(ascitime)s]: %(message)s:')

list_of_files=[
"src/__init__.py",
"src/helper.py",
"src/prompt.py"
".env",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"app.py"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    print(filepath)
    filedir, filename = os.path.split(filepath)
    print(filename)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the files{filename}")



