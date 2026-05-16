# decrypt.py
import numpy as np
from utils import key_to_seed

def xor_decrypt(pixel_array, key_string):
    seed = key_to_seed(key_string)
    rng = np.random.default_rng(seed)
    key_array = rng.integers(0, 256, size=pixel_array.shape, dtype=np.uint8)
    return pixel_array ^ key_array

def rgb_shift_decrypt(pixel_array, key_string):
    seed = key_to_seed(key_string)
    shifts = [seed % 256, (seed // 256) % 256, (seed // 65536) % 256]
    result = pixel_array.copy()
    for i, shift in enumerate(shifts):
        result[:, :, i] = (result[:, :, i].astype(np.int16) - shift) % 256
    return result.astype(np.uint8)

def unshuffle_decrypt(pixel_array, key_string):
    seed = key_to_seed(key_string)
    rng = np.random.default_rng(seed)
    flat = pixel_array.reshape(-1, 3)
    indices = np.arange(len(flat))
    rng.shuffle(indices)
    original = np.empty_like(flat)
    original[indices] = flat
    return original.reshape(pixel_array.shape)

def decrypt(pixel_array, key_string, use_shuffle=False):
    result = pixel_array.copy()
    if use_shuffle:
        result = unshuffle_decrypt(result, key_string)
    result = rgb_shift_decrypt(result, key_string)
    result = xor_decrypt(result, key_string)
    return result
