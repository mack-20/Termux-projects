"""
    Author: MacLeod
    Date: Sunday, February 15 2023
"""
import sys

# Creates an object of the actual file ready to be read from

secretFile = open(sys.argv[1],"r")

# Reads content of the files into a list
code_list = secretFile.readlines()

parsed_list = ""


for code in code_list:
   parsed_list += str(chr(int(code.strip("\n"))))

print (parsed_list)


secretFile.close()
