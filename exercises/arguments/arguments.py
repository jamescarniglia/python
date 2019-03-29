#!/usr/bin/python
#
#
#python version 2.6.8
#
#This sample script prints command line arguments using the sys.argv variable
#
#Import the sys module
import sys


#show all the arguments
print("\nsys.argv contains all the arguments passed to the script.")
print("sys.argv =", sys.argv)

#show the number of arguments
print("\nlen(sys.argv) counts the number of items in the sys.argv list. ")
print("Because the sys.argv will include the name of the script, ")
print("we must subtract one from len(sys.argv) to get the argument count.")
print("(len(sys.argv)-1) =", (len(sys.argv)-1))

#show all the arguments
#print specific arguments in the list
print("\nsys.argv[0], sys.argv[1], etc contains each argument separately.")
print("sys.argv[0] =", sys.argv[0])
print("sys.argv[1] =", sys.argv[1])


# print the script you are running
print("\nsys.argv[0] contains the script name.")
print("sys.argv[0] =", sys.argv[0])
