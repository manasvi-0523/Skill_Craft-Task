# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk
import numpy as np
import os

from utils import load_image, array_to_image, save_image
from encrypt import encrypt
from decrypt import decrypt

PREVIEW_SIZE = (280, 280)
BG = "#1e1e2e"
PANEL_BG = "#2a2a3e"
BTN_BG = "#7c3aed"
BTN_HOVER = "#6d28d9"
TEXT = "#e2e8f0"
SUBTEXT = "#94a3b8"
ACCENT = "#a78bfa"

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.geometry("1050x700")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        
        self.original_array = None
        self.encrypted_array = None
        self.decrypted_array = None
        self.current_indices = None
        
        self._build_ui()
    
    def _build_ui(self):
        # Title
        title = tk.Label(self.root, text="🔐 Image Encryption Tool",
                         font=("Segoe UI", 18, "bold"), bg=BG, fg=ACCENT)
        title.pack(pady=(20, 5))
        
        subtitle = tk.Label(self.root, text="XOR · RGB Shift · Pixel Shuffle",
                            font=("Segoe UI", 10), bg=BG, fg=SUBTEXT)
        subtitle.pack(pady=(0, 15))
        
        # Controls row
        ctrl = tk.Frame(self.root, bg=BG)
        ctrl.pack(pady=5)
        
        self._btn(ctrl, "📂 Upload Image", self.upload_image).grid(row=0, column=0, padx=8)
        
        tk.Label(ctrl, text="Key:", font=("Segoe UI", 11), bg=BG, fg=TEXT).grid(row=0, column=1, padx=(16,4))
        self.key_var = tk.StringVar()
        key_entry = tk.Entry(ctrl, textvariable=self.key_var, font=("Segoe UI", 11),
                             width=18, show="*", bg=PANEL_BG, fg=TEXT,
                             insertbackground=TEXT, relief="flat", bd=6)
        key_entry.grid(row=0, column=2, padx=4)
        
        self.shuffle_var = tk.BooleanVar()
        tk.Checkbutton(ctrl, text="Pixel Shuffle", variable=self.shuffle_var,
                       font=("Segoe UI", 10), bg=BG, fg=TEXT,
                       selectcolor=PANEL_BG, activebackground=BG,
                       activeforeground=ACCENT).grid(row=0, column=3, padx=12)
        
        self._btn(ctrl, "🔒 Encrypt", self.run_encrypt).grid(row=0, column=4, padx=8)
        self._btn(ctrl, "🔓 Decrypt", self.run_decrypt).grid(row=0, column=5, padx=8)
        
        # Save row
        save_row = tk.Frame(self.root, bg=BG)
        save_row.pack(pady=6)
        self._btn(save_row, "💾 Save Encrypted", self.save_encrypted).grid(row=0, column=0, padx=8)
        self._btn(save_row, "💾 Save Decrypted", self.save_decrypted).grid(row=0, column=1, padx=8)
        
        # Preview panels
        panels = tk.Frame(self.root, bg=BG)
        panels.pack(pady=10, fill="both", expand=True)
        
        self.orig_label, self.orig_img_label   = self._panel(panels, "Original")
        self.enc_label,  self.enc_img_label    = self._panel(panels, "Encrypted")
        self.dec_label,  self.dec_img_label    = self._panel(panels, "Decrypted")
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready. Upload an image to begin.")
        tk.Label(self.root, textvariable=self.status_var, font=("Segoe UI", 9),
                 bg=PANEL_BG, fg=SUBTEXT, anchor="w", padx=10).pack(
                 fill="x", side="bottom", ipady=5)
    
    def _btn(self, parent, text, command):
        b = tk.Button(parent, text=text, command=command,
                      font=("Segoe UI", 10, "bold"), bg=BTN_BG, fg="white",
                      relief="flat", padx=14, pady=7, cursor="hand2",
                      activebackground=BTN_HOVER, activeforeground="white")
        b.bind("<Enter>", lambda e: b.config(bg=BTN_HOVER))
        b.bind("<Leave>", lambda e: b.config(bg=BTN_BG))
        return b
    
    def _panel(self, parent, title):
        frame = tk.Frame(parent, bg=PANEL_BG, bd=0, relief="flat")
        frame.pack(side="left", expand=True, fill="both", padx=12, pady=5)
        
        tk.Label(frame, text=title, font=("Segoe UI", 11, "bold"),
                 bg=PANEL_BG, fg=ACCENT).pack(pady=(10, 5))
        
        placeholder = tk.Label(frame, text="No image", bg=PANEL_BG, fg=SUBTEXT,
                                width=30, height=14, relief="flat")
        placeholder.pack(padx=10, pady=(0, 10))
        return frame, placeholder
    
    def _show_image(self, array, label_widget):
        img = array_to_image(array)
        img.thumbnail(PREVIEW_SIZE)
        photo = ImageTk.PhotoImage(img)
        label_widget.config(image=photo, text="", width=PREVIEW_SIZE[0], height=PREVIEW_SIZE[1])
        label_widget.image = photo  # keep reference
    
    def _get_key(self):
        key = self.key_var.get().strip()
        if not key:
            messagebox.showwarning("Key Required", "Please enter an encryption key.")
            return None
        return key
    
    def upload_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")])
        if not path:
            return
        try:
            _, self.original_array = load_image(path)
            self.encrypted_array = None
            self.decrypted_array = None
            self._show_image(self.original_array, self.orig_img_label)
            self.enc_img_label.config(image="", text="No image")
            self.dec_img_label.config(image="", text="No image")
            self.status_var.set(f"Loaded: {os.path.basename(path)}  |  Size: {self.original_array.shape[1]}×{self.original_array.shape[0]}")
        except Exception as e:
            messagebox.showerror("Load Error", str(e))
    
    def run_encrypt(self):
        if self.original_array is None:
            messagebox.showwarning("No Image", "Upload an image first.")
            return
        key = self._get_key()
        if not key:
            return
        try:
            use_shuffle = self.shuffle_var.get()
            self.encrypted_array, self.current_indices = encrypt(
                self.original_array, key, use_shuffle)
            self._show_image(self.encrypted_array, self.enc_img_label)
            self.status_var.set("✅ Encryption successful.")
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))
    
    def run_decrypt(self):
        if self.encrypted_array is None:
            messagebox.showwarning("No Encrypted Image", "Encrypt an image first.")
            return
        key = self._get_key()
        if not key:
            return
        try:
            use_shuffle = self.shuffle_var.get()
            self.decrypted_array = decrypt(self.encrypted_array, key, use_shuffle)
            self._show_image(self.decrypted_array, self.dec_img_label)
            self.status_var.set("✅ Decryption successful.")
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))
    
    def save_encrypted(self):
        if self.encrypted_array is None:
            messagebox.showwarning("Nothing to Save", "Encrypt an image first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
            initialdir="output", filetypes=[("PNG", "*.png")])
        if path:
            save_image(self.encrypted_array, path)
            self.status_var.set(f"💾 Encrypted image saved → {os.path.basename(path)}")
    
    def save_decrypted(self):
        if self.decrypted_array is None:
            messagebox.showwarning("Nothing to Save", "Decrypt an image first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
            initialdir="output", filetypes=[("PNG", "*.png")])
        if path:
            save_image(self.decrypted_array, path)
            self.status_var.set(f"💾 Decrypted image saved → {os.path.basename(path)}")
