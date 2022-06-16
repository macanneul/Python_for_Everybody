# Count the frequency of each word in a file
# Store it in a dictionary
# Find the most common word

while True :
    fname = input('Enter a file name: ')
    # Deal with traceback due to file not found
    try :
        with open(fname, 'r') as fhandle : 
            # Populate dictionary with { 'word' : frequency }
            countme = {}
            for line in fhandle :
                words = line.rstrip().split()
                for word in words :
                    # Retrieve (the old), create (the new), update (the key-value)
                    countme[word] = countme.get(word, 0) + 1
            break
    except FileNotFoundError :
        yn = input('File not found. Would you like to try again? (y/n): ')
        if yn == 'y' :
            continue
        else :
            quit()

# Find word with the highest frequency in countme (the dictionary)
mostword = None
mostfreq = None
for (word, freq) in countme.items() :
    if mostfreq is None or freq > mostfreq :
        mostword = word
        mostfreq = freq

print('The most common word is "' + mostword + '" which occured', mostfreq, 'times.')