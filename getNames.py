import sys

repFile = ""

if len(sys.argv) > 2:
    print("Sorry to many args\n")
    sys.exit()
else:
    repFile = sys.argv[1]

with open(repFile, 'r') as file_handle:
    lines = file_handle.readlines()[8:]

file_handle.close()

lines.pop()
lines.pop()
lines.pop()
lines.pop()
lines.pop()

usernames = []
for x in lines:
    words = x.split()
    if len(words) == 6:
        usernames.append(words[4])
    elif len(words) == 5:
       usernames.append(words[3])
    else:
        print("There is another case not checked")

with open('new.txt', 'w') as file_handler:
    for x in usernames:
        file_handler.write("%s\n" % x)
