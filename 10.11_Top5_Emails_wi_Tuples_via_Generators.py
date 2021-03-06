# Same as 10.01_Top5_Emails_wi_Tuples but use generators
# to enable larger mail-log processing whilst increase
# efficiency on RAM usage

# Set up regular expression
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Set up the generator
def open_file_reader(fname) :
    try :
        with open(fname, 'r') as fhandle : 
            for line in fhandle :
                yield line
    except FileNotFoundError :
        yn = input('File not found. Would you like to try again? (y/n): ').strip().lower()
        if yn == 'y' :
            start_prog()
        else :
            quit(print('Goodbye!'))

countme = {}
# Populate countme (type dic) with email:freq pairs
def start_prog() :
    for line in open_file_reader(input('Enter a file name: ')) :
        words = line.split()
        # To avoid blank lines and IndexError: list index out of range
        if len(line) < 2 or words[0] != 'From' : continue
        # Find email address in line (type str) using regular expression
        email = re.findall(regex, line)[0]
        # Retrieve (the old), create (the new), update (the key-value)
        countme[email] = countme.get(email, 0) + 1

start_prog()
# Sort to find top 5 frequent emails in countme
tpl = sorted( ( (freq, email) for (email, freq) in countme.items() ), reverse = True)
# (swapping 2nd set of [] for () above turned a list compression into a generator expression)
print('Here are the top 5 email addresses and their number of commits:')
for (freq, email) in tpl[ : 5] :
    print(email, freq)