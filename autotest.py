import os
import re
import sys

STUDENT_SCRIPTS = sys.argv[1:]
source_files = ""
for file in STUDENT_SCRIPTS:
    source_files += file + " "

source_files = source_files[:-1]

FILES = os.listdir(".")
INPUT_LIST = []
OUTPUT_LIST = []

input_ext = False;

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
        OUTPUT_LIST.append(raw_match.group())

INPUT_LIST.sort()
OUTPUT_LIST.sort()

if (not input_ext):
    for file in INPUT_LIST:
        os.system("gcc " + source_files + " " + file + " -o " + file[0:-2] + ".x")
    for file in INPUT_LIST:
        os.system(file[0:-2] + ".x")

else:
    for file in INPUT_LIST:
        os.system("gcc " + source_files + " -o " + file[0:-6] + ".x")
    for file in INPUT_LIST:
        os.system(file[0:-6] + ".x < " + file + " | diff -b - " + file[0:-6] + ".output")
        
