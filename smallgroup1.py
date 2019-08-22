# Small group programming challenge 1
# A program to take user-input name and output "Hello" and that name
# Python 3.7.3
# by Alberto Maiocco and Dara Lim, CS4500-002
# 8/22/2019

# Using Try/Except block:
# Checks config.txt exsisting. If it exists, pulls name from the file.
# If it doesnt exist, use standard input.
try:
    file = open('config.txt', 'r');
except:
    name = input('What is your name?\n');
    print("Hello", name);
else:
    nameFromFile = file.read();
    print("Hello", nameFromFile);
