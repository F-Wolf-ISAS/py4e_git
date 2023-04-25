# Open the file mbox-short.txt and read it line by line. When you
# find a line that starts with 'From ' like the following line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out the
# second word in the line (i.e. the entire address of the person
# who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print
# the count.

# fname = input("Enter file name: ")
#if len(fname) < 1:
    #fname = "mbox-short.txt"

#fh = open(fname)
#count = 0

# print("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    count = count + 1
    words = line.split()
    print(words[1])

print("There were", count, "lines in the file with From as the first word")

# Musterlösung

# han = open('mbox-short.txt')
# for line in han:
    # line = line.rstrip()
    # wds = line.split()
    # #guardian in a compound statement
    # if len(wds) < 3 or wds[0] != 'From ':
        # continue
    # print(wds[2])
   