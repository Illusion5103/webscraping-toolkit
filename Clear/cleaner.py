array = []

with open('ips_raw.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip().split(',')
        array = l

with open('ips_cleaned.txt', 'w') as o:
    for item in array:
        if "u=" not in item:
            if "user=" not in item:
                if "usr=" not in item:
                    o.write(item)
