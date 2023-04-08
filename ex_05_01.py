# This is chapter 5 exercise 1 in the book.
# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try 
# and except and print an error message and skip to the next number.

total = 0
count = 0
print('Before:', total, count)

while True:
    numbers = input('Please enter next number: ')
    if numbers == 'done':
        break
    else:
        try:
            num = int(numbers)
        except:
            num = -1

        if num > 0:
            total = total + num
            count = count + 1
        else:
            print('Invalid input!')
        continue

print('After:', total, count, total/count)

# Musterlösung
# num = 0
# tot = 0
# while True:
#    sval = input('Enter a number: ')
#    if sval == 'done':
#        break
#    try:
#        fval = float(sval)
#    except:
#        print('Invalid input')
#        continue
#    num = num + 1
#    tot = tot + fval
#
# print(tot, num, tot/num)