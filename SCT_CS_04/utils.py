# utils.py
from PIL import Image
import numpy as np
import os

def load_image(path):
    img = Image.open(path).convert("RGB")
    return img, np.array(img, dtype=np.uint8)

def array_to_image(array):
    return Image.fromarray(array.astype(np.uint8), mode="RGB")

def save_image(array, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = array_to_image(array)
    img.save(output_path)
    return output_path

def key_to_seed(key_string):
    return sum(ord(c) for c in key_string) % (2**32)
