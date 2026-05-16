# encrypt.py
import numpy as np
from utils import key_to_seed

def xor_encrypt(pixel_array, key_string):
    seed = key_to_seed(key_string)
    rng = np.random.default_rng(seed)
    key_array = rng.integers(0, 256, size=pixel_array.shape, dtype=np.uint8)
    return pixel_array ^ key_array

def rgb_shift_encrypt(pixel_array, key_string):
    seed = key_to_seed(key_string)
    shifts = [seed % 256, (seed // 256) % 256, (seed // 65536) % 256]
    result = pixel_array.copy()
    for i, shift in enumerate(shifts):
        result[:, :, i] = (result[:, :, i].astype(np.int16) + shift) % 256
    return result.astype(np.uint8)

def shuffle_encrypt(pixel_array, key_string):
    seed = key_to_seed(key_string)
    rng = np.random.default_rng(seed)
    flat = pixel_array.reshape(-1, 3)
    indices = np.arange(len(flat))
    rng.shuffle(indices)
    shuffled = flat[indices]
    return shuffled.reshape(pixel_array.shape), indices

def encrypt(pixel_array, key_string, use_shuffle=False):
    result = xor_encrypt(pixel_array, key_string)
    result = rgb_shift_encrypt(result, key_string)
    indices = None
    if use_shuffle:
        result, indices = shuffle_encrypt(result, key_string)
    return result, indices
