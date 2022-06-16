# Same as 09.04_Most_Common_Email but print the top 5 email addresses with the most commits 
# by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order before printing out the results.

# Set up what we need for regular expression
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

while True :
    fname = input('Enter a file name: ')
    # Deal with traceback due to FileNotFoundError
    try :
        with open(fname, 'r') as fhandle : 
            # Populate dictionary with { 'word' : frequency }
            countme = {}
            for line in fhandle :
                words = line.split()
                # To avoid blank lines and IndexError: list index out of range
                if len(line) < 2 or words[0] != 'From' : continue
                # Find email address in line (a string) using regular expression
                email = re.findall(regex, line)[0]
                # Retrieve (the old), create (the new), update (the key-value)
                countme[email] = countme.get(email, 0) + 1
            break
    except FileNotFoundError :
        yn = input('File not found. Would you like to try again? (y/n): ')
        if yn == 'y' :
            continue
        else :
            print('Goodbye!')
            quit()

# Create a list of tuples from countme (the dictionary)

tpl = list()
for (email, freq) in countme.items() :
    tpl.append( (freq, email) )
# Find top 5 frequent emails by sorting countme
# Note: sorted() returns a sorted list, whereas sort() only returns None
tpl = sorted(tpl, reverse = True)
# The line below should also work in place of lines 35-40
# tpl = sorted( [ (freq, email) for (email, freq) in countme.items() ], reverse = True)

print('Here are the top 5 email addresses and their number of commits:')
for (freq, email) in tpl[ : 5] :
    print(email, freq)
print('Done!')