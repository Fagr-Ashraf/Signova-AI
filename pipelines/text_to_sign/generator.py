import re

import numpy as np
from .assets_loader import load_landmarks

landmarks_dict = None

def get_landmarks():
    global landmarks_dict

    if landmarks_dict is None:
        print("Loading landmarks...")
        landmarks_dict = load_landmarks()

    return landmarks_dict

def generate_frames(mapped_sequence):

    landmarks = get_landmarks()

    all_frames = []

    for item in mapped_sequence:

        if item["type"] == "direct":
            word = item["mapped"].lower()

            if word in landmarks:
                frames = [np.array(f, dtype=float) for f in landmarks[word]]
                all_frames.extend(frames)

        else:
            word = re.sub(r"[^a-z]", "", item["original"].lower())

            for letter in word:
                if letter in landmarks:
                    frames = [np.array(f, dtype=float) for f in landmarks[letter]]
                    all_frames.extend(frames)

    return all_frames