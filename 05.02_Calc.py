# Got told that lists are unnecessary for the objective of 05.01_Calc.py
    # Not the first time I complicate things for myself and won't be the last
# Here's an attempt to trim my code down

ttl = 0.0
cnt = 0
avg = 0.0

while True :
    num = input('Enter a number: ')
    num = num.lower()
    if num == 'done' :
        break
    try :
        num = float(num)
    except :
        print('Invalid input')
        continue
    ttl = ttl + num
    cnt = cnt + 1
    # Avoid ZeroDivsionError when user inputs 'done' as first value
    try :
        avg = ttl / cnt
    except ZeroDivisionError :
        avg = 0

print('Total:', ttl, 'Count:', cnt, 'Average:', avg)
