import tkinter as tk
from cryptography.fernet import Fernet

class StringEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Symmetric String Encryptor")

        self.key_label = tk.Label(root, text="Generated Key:")
        self.key_label.pack()

        self.generate_key_button = tk.Button(root, text="Generate Key", command=self.generate_key)
        self.generate_key_button.pack()

        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.encrypted_text_label = tk.Label(root, text="Encrypted Text:")
        self.encrypted_text_label.pack()

        self.encrypted_text = tk.Label(root, text="")
        self.encrypted_text.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        self.decrypted_text_label = tk.Label(root, text="Decrypted Text:")
        self.decrypted_text_label.pack()

        self.decrypted_text = tk.Label(root, text="")
        self.decrypted_text.pack()

    def generate_key(self):
        self.key = generate_key()
        self.key_label.config(text="Generated Key: " + self.key.decode())

    def encrypt(self):
        text = self.text_entry.get()
        encrypted_text = encrypt_string(self.key, text)
        self.encrypted_text.config(text=encrypted_text.decode())

    def decrypt(self):
        encrypted_text = self.encrypted_text.cget("text").encode()
        decrypted_text = decrypt_string(self.key, encrypted_text)
        self.decrypted_text.config(text=decrypted_text)

def generate_key():
    return Fernet.generate_key()

def encrypt_string(key, text):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def decrypt_string(key, encrypted_text):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

if __name__ == "__main__":
    root = tk.Tk()
    app = StringEncryptorApp(root)
    root.mainloop()
