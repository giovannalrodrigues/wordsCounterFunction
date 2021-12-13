import re

line = input("Please, enter your text: ")

def countWords(line):
    count = len(re.findall("[a-zA-Z_](?:\w|['-]\w)+", line))
    return count

count = countWords(line)

if count == 0:
    print("Sorry, you didn't enter a valid text.")

elif count == 1:
    print('Your text has', count, 'word.')

else:
    print('Your text has', count, 'words.')