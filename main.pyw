import sys
from tkinter import *
from tkinter import ttk
import wireheart

DIMENSIONS = (500, 550)

root = Tk()
root.geometry(f"{DIMENSIONS[0]}x{DIMENSIONS[1]}")
root.title(f"/WIREHEART/")

try:
    root.iconbitmap("favicon.ico")
except TclError:
    pass


notebook = ttk.Notebook(root)
encrypt_page = Frame(notebook)
decrypt_page = Frame(notebook)

encrypt_entry = Entry(encrypt_page)
encrypt_entry.pack(expand=1, fill="x")
encrypt_out = Text(encrypt_page)
encrypt_out.pack(side=BOTTOM)
encrypt_entry.focus_set()

decrypt_entry = Entry(decrypt_page)
decrypt_entry.pack(expand=1, fill="x")
decrypt_out = Text(decrypt_page)
decrypt_out.pack(side=BOTTOM)
decrypt_entry.focus_set()


def on_encrypt():
    msg = encrypt_entry.get()
    msg = wireheart.encrypt(msg)
    encrypt_out.delete("1.0", END)
    encrypt_out.insert(END, msg)


def on_decrypt():
    msg = decrypt_entry.get()
    msg = wireheart.decrypt(msg)
    decrypt_out.delete("1.0", END)
    decrypt_out.insert(END, msg)

encrypt_button = Button(encrypt_page, command=on_encrypt, text="ENCRYPT")
encrypt_button.pack()
decrypt_button = Button(decrypt_page, command=on_decrypt, text="DECRYPT")
decrypt_button.pack()

notebook.add(encrypt_page, text="ENCRYPT")
notebook.add(decrypt_page, text="DECRYPT")
notebook.pack(expand=1, fill="both")

root.mainloop()
