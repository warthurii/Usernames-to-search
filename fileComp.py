import numpy as np
import sys

if len(sys.argv) > 3:
    print("Sorry to many arguemnts")
    sys.exit()
elif len(sys.argv) == 3:
    newFile = sys.argv[1]
    oldFile = sys.argv[2]
else:
    newFile = "new.txt"
    oldFile = "old.txt"

# read file content into list
with open(newFile, 'r') as file_handle:
    newList = file_handle.readlines()
with open(oldFile, 'r') as file_handle:
    oldList = file_handle.readlines()

file_handle.close()

# Stripping the \n in each element
newList = [line.strip() for line in newList]
oldList = [line.strip() for line in oldList]

# Create a new list that has all usernames in the new file that aren't in the old
searchList = np.setdiff1d(newList,oldList)

# output searchList to file
with open('search.txt', 'w') as file_handler:
    for x in searchList:
        file_handler.write("%s\n" % x)

# adding searchList to oldList
for x in searchList:
    oldList.append(x)

# writing oldList to the old file
with open('old.txt', 'w') as file_handler:
    for x in oldList:
        file_handler.write("%s\n" % x)

file_handler.close()
