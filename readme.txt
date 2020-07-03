-fileComp.py is a script to compares two files and outputs the usernames that are in one but not the other

-format of input files should have one username on each line

-to run the script:
    -pass the 2 file names through the command line arg handler. The first should be the new file that the
    script will find the new usernames from. The second is the old file that the new file will be compared to.
    Ex. 'python fileComp.py first.txt second.txt'
    -or name one file "old.txt" and the other "new.txt" and dont pass any argument via command line. The 
    script will run the files automatically.
    Ex. 'python fileComp.py'

-the outcome:
    -Will output usernames in the new file that aren't in the old file to a file named 'search.txt'
    -Will also update the old file to include the usernames in the search file.