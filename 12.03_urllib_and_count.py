# Use `urllib` to retrieve a document from a user-input URL, display up to 3000 characters, 
# and count the number of characters in the document (ignore header).

import urllib.request

while True :
    url = input('Enter URL of file: ')
    try :
        fhandle = urllib.request.urlopen(url)
    except FileNotFoundError :
        yn = input('File not found. Would you like to try again? (y/n): ')
        if yn == 'y' :
            continue
        else :
            quit()
    break

char_count = 0
spc_count = 0
for line in fhandle :
    line = line.decode().strip()
    # the line below shortens this: char_count = char_count + len(line)
    char_count += len(line)
    spc_count += line.count(' ')
    if char_count > 3000 : break
    print(line)

print(f'\nNumber of characters in this document (maximum 3000): {char_count} (of which {spc_count} are spaces)')