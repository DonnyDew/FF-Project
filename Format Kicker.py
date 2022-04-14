import re
from os import path

file_path = input('File Path: ')
while not path.exists(file_path):
    input('Invalid file path. Try again: ')

with open(file_path, 'r') as f:
    file_str = f.read()
with open(file_path, 'w') as f:
    file_str = re.sub(' *[(].*[)],| +,', ',', file_str)
    f.write(file_str)

#C:\Users\Donald Robbins\Desktop\Python Files\hello_ds\K_Stats_tot.csv
    
