#!/home/jusa/Desktop/python_automation/venv/bin/python3
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else: 
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)

