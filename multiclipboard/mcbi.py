import tkinter as tk
from tkinter import simpledialog, messagebox
import shelve
import pyperclip

def save_clipboard():
    keyword = simpledialog.askstring("Save Clipboard", "Enter a keyword:")
    if keyword:
        with shelve.open('mcb') as mcbShelf:
            mcbShelf[keyword] = pyperclip.paste()
        update_listbox()

def load_clipboard():
    keyword = listbox.get(tk.ANCHOR)
    if keyword:
        with shelve.open('mcb') as mcbShelf:
            pyperclip.copy(mcbShelf[keyword])

def delete_clipboard():
    keyword = listbox.get(tk.ANCHOR)
    if keyword and messagebox.askyesno("Delete", f"Delete {keyword}"):
        with shelve.open('mcb') as mcbShelf:
            del mcbShelf[keyword]
        update_listbox()


def update_listbox():
    listbox.delete(0, tk.END)
    with shelve.open('mcb') as mcbShelf:
        for keyword in mcbShelf.keys():
            listbox.insert(tk.END, keyword)

app = tk.Tk()
app.title('Clipboard Manager')

listbox = tk.Listbox(app)
listbox.pack(fill=tk.BOTH, expand=True)

save_button = tk.Button(app, text="Save Clipboard", command=save_clipboard)
save_button.pack(fill=tk.X)

load_button = tk.Button(app, text="Load Selected", command=load_clipboard)
load_button.pack(fill=tk.X)

delete_button = tk.Button(app, text="Delete selected", command=delete_clipboard)
delete_button.pack(fill=tk.X)

update_listbox()

app.mainloop()
