# Have user input his name and respond by greeting him

# Prompt user to enter name
# remove spaces from n (string) -- in case user falls asleep on the spacebar --
# and capitalise the first letter(s)
n = input('Enter your name: ').strip().title()
# Note: capitalize() only changes the first letter of the string
# whereas title() will capitalise first letter of the string 
# AND first letter after each subsequent space
print(f'Hallo, {n}!')
