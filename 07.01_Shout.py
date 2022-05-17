# Write a program to read through mbox-short.txt and print its contents (line by line) all in upper case.
# Prompt the user to enter file name first.

while True :
    fname = input('Enter a file name: ')
    # Deal with traceback due to file not found
    try :
        # Open the file
        with open(fname, 'r') as fhandle :
            for line in fhandle :
                # Strip /n from end of line and print the line ALL CAPS
                print(line.upper().rstrip())
            break
    except :
        yn = input('File not found. Would you like to try again? (y/n): ')
        if yn == 'y' :
            continue
        else :
            break