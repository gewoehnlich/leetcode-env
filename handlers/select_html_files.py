import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from exceptions.exceptions import NoFilesSelectedException
from typing import List
import json

def getHTMLFiles() -> List[str]:
    root = tk.Tk()
    root.withdraw()

    last_directory = getLastDirectory()

    file_paths = filedialog.askopenfilenames(
        title="Select files",
        initialdir=last_directory,
        filetypes=[("HTML files", "*.html")]
    )


    if not file_paths:
        raise NoFilesSelectedException

    last_directory = str(Path(file_paths[-1]).parent)
    if last_directory:
        saveLastDirectory(last_directory)

    return file_paths


def getLastDirectory() -> None:
    path = Path("config.json")    
    if not path:
        return False

    with open(path, "r") as file:
        data = json.load(file)
        if not data.get("last_directory"):
            return False
        
        return data.get("last_directory")


def saveLastDirectory(directory: str) -> None:
    path = Path("config.json")    
    if not path:
        return False
    
    data = {}
    with open(path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            pass

    data["last_directory"] = directory

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

