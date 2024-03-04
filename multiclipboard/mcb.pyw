# Saves and loads pieces of text to clipboard
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#           py.exe mcb.pyw load <keyword> - Loads all keywords to clipboard


import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# save Clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'load':
    # Load content to clipboard.
    if sys.argv[2] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[2]])
    else:
        print(f"Keyword {sys.argv[2]} not found.")
elif len(sys.argv) == 2:
    # List keywords and load content (for direct keyword access).
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print(f"Keyword {sys.argv[1]} not found.")



mcbShelf.close()