#!/usr/bin/python
#
#
#
#
#show number of arguments
import sys

if len(sys.argv) == 1:
    print("You must provide this script with at least one argument.")
    print()
    exit(9)

#show number of arguments
print("\nlen(sys.argv) shows you how many arguments you passed to the script. ") 
print("The first argument is always the script name, the second is the first argument.\n") 
print("If you ran the script and passed it one argument, len(sys.argv) should be 2.  Right now len(sys.argv) is the following.")
print("len(sys.argv) =", len(sys.argv))

#show all the arguments
print("\nsys.argv shows you all the arguments passed to the script.")
print("sys.argv =", sys.argv)

#call specific arguments
print("\nsys.argv[0], sys.argv[1], etc are used to call each argument seperatly.")
print("sys.argv[0] =", sys.argv[0])
print("sys.argv[1] =", sys.argv[1])

if (len(sys.argv)) > 2:
     print("sys.argv[2] =", sys.argv[2])

# call the script you are running
print("\nIf you call sys.argv[0] it will give you the script name.")
print("sys.argv[0] =", sys.argv[0])
