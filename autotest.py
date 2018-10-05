import os
import re
import sys

if (len(sys.argv) < 2):
    print("Must enter at least one source file as an argument")
    sys.exit()
STUDENT_SCRIPTS = sys.argv[1:]
source_files = ""
for file in STUDENT_SCRIPTS:
    source_files += file + " "

source_files = source_files[:-1]

FILES = os.listdir(".")
INPUT_LIST = []
OUTPUT_LIST = []

input_ext = False;
output_ext = False;

for file in FILES:
    raw_match = re.search(r'public[0-9]+[.]c', file)
    if (raw_match != None):
        INPUT_LIST.append(raw_match.group())
    raw_match = re.search(r'public[0-9]+[.]input', file)
    if (raw_match != None):
        input_ext = True
        INPUT_LIST.append(raw_match.group())
    raw_match = re.search(r'public[0-9]+[.]output', file)
    if (raw_match != None):
        output_ext = True
        OUTPUT_LIST.append(raw_match.group())

INPUT_LIST.sort()
OUTPUT_LIST.sort()
count = 1;

if (not input_ext):
    for file in INPUT_LIST:
        os.system("gcc " + source_files + " " + file + " -o " + file[0:-2] + ".x")
    if (not output_ext):
        for file in INPUT_LIST:
            print("\nTest " + str(count) + " Running...\n")
            os.system(file[0:-2] + ".x")
            count+=1
    else:
        for file in OUTPUT_LIST:
            print("\nTest " + str(count) + " Running...\n")
            os.system(file[0:-7] + ".x | " + "diff -b - " + file)
            count+=1

else:
    for file in INPUT_LIST:
        os.system("gcc " + source_files + " -o " + file[0:-6] + ".x")
    for file in INPUT_LIST:
        print("\nTest " + str(count) + " Running...\n")
        os.system(file[0:-6] + ".x < " + file + " | diff -b - " + file[0:-6] + ".output")
        count+=1
        
