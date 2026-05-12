# PixelCrypt - Image Encryption Tool

**SkillCraft Technology Cybersecurity Internship | Task 04**

A desktop application that encrypts and decrypts images using three stacked operations: XOR cipher, RGB channel shift, and optional pixel shuffle. Built with Python and Tkinter. Decryption with the correct key recovers the original image exactly.

---

## Features

**Encryption pipeline**

1. XOR cipher: generates a deterministic random array from the key seed and XORs it against every pixel value
2. RGB shift: shifts each color channel independently by a different amount derived from the key
3. Pixel shuffle (optional): randomly permutes all pixel positions across the image

Decryption reverses these steps in the opposite order.

**GUI**
- Upload any PNG, JPG, JPEG, BMP, or TIFF file
- Password field (masked) for the encryption key
- Checkbox to enable or disable pixel shuffle
- Three side-by-side preview panels: Original, Encrypted, Decrypted
- Save buttons for encrypted and decrypted outputs (saved to `output/`)
- Status bar with file info and operation results

---

## Setup

Requirements: Python 3.8 or higher.

```bash
git clone https://github.com/manasvi-0523/Skill_Craft-Task.git
cd Skill_Craft-Task
pip install -r SCT_CS_04/requirements.txt
python SCT_CS_04/app.py
```

---

## How to use

1. Click "Upload Image" and select an image file.
2. Type a key in the password field.
3. Click "Encrypt". The encrypted preview appears in the middle panel.
4. Click "Save Encrypted" to write the file to `SCT_CS_04/output/`.
5. To decrypt, keep the same key and shuffle setting, then click "Decrypt".
6. The decrypted image appears in the right panel and should match the original exactly.

Using a different key or a different shuffle setting during decryption will produce garbage output.

---

## Key derivation

```python
def key_to_seed(key_string):
    return sum(ord(c) for c in key_string) % (2**32)
```

The seed initializes NumPy's default random generator, which produces the same XOR mask and shuffle order every time for the same key.

---

## Project structure

```
SCT_CS_04/
    app.py          entry point, launches the Tkinter window
    gui.py          all UI code (ImageEncryptionApp class)
    encrypt.py      xor_encrypt, rgb_shift_encrypt, shuffle_encrypt, encrypt
    decrypt.py      xor_decrypt, rgb_shift_decrypt, unshuffle_decrypt, decrypt
    utils.py        load_image, save_image, array_to_image, key_to_seed
    requirements.txt
    output/         default save directory (created on first save)
    README.md
```

---

## Test results

Verified with a 10x10 synthetic RGB array:

| Test | Result |
|------|--------|
| Encrypted output differs from original | pass |
| Decrypted output matches original (no shuffle) | pass |
| Decrypted output matches original (with shuffle) | pass |
| Wrong key does not recover original | pass |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| Pillow | image loading and saving |
| numpy | pixel array operations |

Tkinter ships with the Python standard library and requires no separate install.

---

## Limitations

The key derivation is a simple character sum, which means different keys can produce the same seed. For a project requiring stronger security, replace `key_to_seed` with PBKDF2 or Argon2 and use AES-GCM for the actual encryption.

---

## Author

Manasvi | [@manasvi-0523](https://github.com/manasvi-0523)
