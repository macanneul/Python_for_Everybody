# Read through mbox-short.txt to find lines that start with 'From'
# Split each line into words and print the sender's email address
# Count and print, at the end, the number of 'From' lines

# Open the file
with open('mbox-short.txt', 'r') as fhandle :
    fl = 0
    for line in fhandle :
        # Strip /n at line's end and split
        wd = line.rstrip().split()
        # To avoid blank lines and IndexError: list index out of range
        # (Tried len(line)<1 and still got Traceback due to /n in blank lines)
        if len(line) < 2 or wd[0] != 'From' : continue
        print(wd[1])
        fl = fl + 1

print('Lines starting with "From":', fl)