# Write a program to read through a mail log
# Build a histogram using a dictionary to count how many messages have come from each email address
# Find the most frequent email address

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

while True :
    fname = input('Enter a file name: ')
    # Deal with traceback due to file not found
    try :
        with open(fname, 'r') as fhandle : 
            # Populate dictionary with { 'word' : frequency }
            countme = {}
            for line in fhandle :
                words = line.split()
                # To avoid blank lines and IndexError: list index out of range
                if len(line) < 2 or words[0] != 'From' : continue
                # Find email address in line (a string) using regular expression
                email = re.findall(regex, line)
                # Since re.findall() returns a list and get() will only take strings, convert the list to string
                email = email[0]
                # Retrieve (the old), create (the new), update (the key-value)
                countme[email] = countme.get(email, 0) + 1
            break
    except :
        yn = input('File not found. Would you like to try again? (y/n): ')
        if yn == 'y' :
            continue
        else :
            quit()

# Find word with the highest frequency in countme (the dictionary)
mostmail = None
mostfreq = None
for (email, freq) in countme.items() :
    if mostfreq is None or freq > mostfreq :
        mostemail = email
        mostfreq = freq

print('The most common email address is "' + mostemail + '" you received', mostfreq, 'email(s) from it.')