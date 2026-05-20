import tkinter as tk
from tkinter import messagebox


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep spaces, numbers, symbols unchanged
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)



def perform_encryption():
    text = message_entry.get("1.0", tk.END).strip()

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    encrypted_text = encrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)


def perform_decryption():
    text = message_entry.get("1.0", tk.END).strip()

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    decrypted_text = decrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)


def clear_fields():
    message_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    output_text.delete("1.0", tk.END)



root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("600x450")
root.config(bg="#1e1e2f")

title_label = tk.Label(
    root,
    text="Caesar Cipher Encryption & Decryption",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=15)

# Message Input
message_label = tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
message_label.pack(anchor="w", padx=20)

message_entry = tk.Text(root, height=5, width=60, font=("Arial", 11))
message_entry.pack(pady=5)

# Shift Value
shift_label = tk.Label(
    root,
    text="Enter Shift Value:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
shift_label.pack(anchor="w", padx=20, pady=(10, 0))

shift_entry = tk.Entry(root, font=("Arial", 12), width=10)
shift_entry.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=15)

encrypt_button = tk.Button(
    button_frame,
    text="Encrypt",
    command=perform_encryption,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(
    button_frame,
    text="Decrypt",
    command=perform_decryption,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)
decrypt_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#f44336",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
)
clear_button.grid(row=0, column=2, padx=10)

# Output Section
output_label = tk.Label(
    root,
    text="Output:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
output_label.pack(anchor="w", padx=20)

output_text = tk.Text(root, height=5, width=60, font=("Arial", 11))
output_text.pack(pady=5)

root.mainloop()
