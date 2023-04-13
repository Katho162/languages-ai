from typing import List
import pickle
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/nlmt.pkl", "rb") as f:
    model = pickle.load(f)

def predict_pipeline(languages : List[str]):
    print(model)
    # return pred