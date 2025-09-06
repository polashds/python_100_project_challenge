import os
from pathlib import Path

project_name = "Py_100_Project"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/data/raw/__init__.py",
    f"{project_name}/data/processed/__init__.py",
    f"{project_name}/data/external/__init__.py",
    f"{project_name}/1_helloworld.py",
    f"{project_name}/2_project_folder_file.py",
    f"{project_name}/3_calculator.py",
    f"{project_name}/4_number_guess.py",
    f"{project_name}/5_rock_paper_scissors_game.py",
    "setup.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"The file {filepath} already exists")