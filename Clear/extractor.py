import re

array = []
pure = []

with open('ips_cleaned.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip().split(',')
        array = l


with open('ips_extracted.txt', 'w') as o:
    for item in array:
        pure = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str(item))
        o.write(str(pure))
