# This script will take text from your clipboard and extract all emails and phone numbers from it

import pyperclip
import re

phoneRegex = re.compile(r'''
(\d{3})     # Area code/040 etc.
(\s|-)?     # Optional separator
(\d{3})     # First 3 digits
(\s|-)?     # Optional separator
(\d{4})     # Last 4 digits
''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''
([a-zA-Z0-9._%+-]+       # Username
@                        # @ symbol
[a-zA-Z0-9.-]+           # Domain name
\.[a-zA-Z]{2,})          # Domain suffix
''', re.VERBOSE)

# Find matches from clipboard
text = str(pyperclip.paste())

# Separate lists for phone numbers and emails
phones = []
emails = []

# Find and add phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    phones.append(phoneNum)

# Find and add emails
for match in emailRegex.findall(text):
    emails.append(match)

# Alternate phone and email in the output, as much as possible
matches = []
max_len = max(len(phones), len(emails))
for i in range(max_len):
    if i < len(phones):
        matches.append(phones[i])
    if i < len(emails):
        matches.append(emails[i])

# Copy results to the clipboard and print them
if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    for match in matches:
        print(match)
else:
    print('No phone numbers or email addresses found.')

