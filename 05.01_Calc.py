# Have user repeatedly enter numbers until he enters 'done'
# When 'done' is entered, print the total, count, and average of the numbers

# Create empty list
num_list = []

# Ask user for input and build num_list
while True :
    num = input('Enter a number: ')
    num = num.lower()
    if num == 'done' :
        break
    try :
        num = float(num)
        num_list.append(num)
    except :
        print('Invalid input')
        
# Calculate after loop breaks
ttl = 0
cnt = 0
avg = 0
for value in num_list :
    ttl = ttl + value
    cnt = int(cnt + 1)
    # Avoid ZeroDivsionError when user inputs 'done' as first value
    try :
        avg = ttl / cnt
    except ZeroDivisionError :
        avg = 0

print('Total:', ttl, 'Count:', cnt, 'Average:', avg)
    
