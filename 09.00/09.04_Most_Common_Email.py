# Write a program to read through a mail log
# Build a histogram using a dictionary to count how many messages have come from each email address
# Find the most frequent email address

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
                # Since we know email address comes right after 'From', words[1] will work; otherwise, take a look at 09.05_Most_Common_Email.py (lines 19-22)
                email = words[1]
                # Retrieve (the old), create (the new), update (the key-value)
                countme[email] = countme.get(email, 0) + 1
            break
    except FileNotFoundError :
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