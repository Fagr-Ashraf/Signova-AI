import json
import numpy as np
from pathlib import Path
from .config import JSON_PATH, LANDMARKS_PATH

print("=" * 60)
print("Current working directory:", Path.cwd())
print("JSON_PATH:", JSON_PATH)
print("JSON exists:", Path(JSON_PATH).exists())
print("LANDMARKS_PATH:", LANDMARKS_PATH)
print("LANDMARKS exists:", Path(LANDMARKS_PATH).exists())
print("=" * 60)


def load_landmarks():
    with open(JSON_PATH) as f:
        data = json.load(f)

    landmarks_data = np.load(LANDMARKS_PATH, allow_pickle=True)
    landmarks_array = landmarks_data["landmarks"]

    landmarks_dict = {}

    for sample, lm in zip(data, landmarks_array):
        gloss = sample["gloss"].lower().strip()
        landmarks_dict[gloss] = lm

    return landmarks_dict