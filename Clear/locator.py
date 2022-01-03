import json
import ipinfo
import socket

array = []
ips = []

with open('ips_cleaned.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip().split(' ')
        array = l

with open('ips_extracted.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip().split(' ')
        ips = l

data = []
access_token = '*YOUR IPINFO API ACCESS TOKEN*'
handler = ipinfo.getHandler(access_token)
i = 0

for ip in ips:
    ip = ip.replace("[", "")
    ip = ip.replace("]", "")
    ip = ip.replace("'", "")
    ip = ip.replace(",", "")
    try:
        details = handler.getDetails(ip)
        dicto = {
            "ip": ip,
            "url": array[i],
            "hostname": details.hostname,
            "country": details.country,
            "region": str(details.region),
            "city": str(details.city),
            "coords": details.loc,
            "org": details.org,
            "postal": details.postal,
            "timezone": details.timezone
        }
        data.append(dicto) 
        print(dicto)
    except socket.timeout:
        pass
    except AttributeError:
        pass
    i = i+1

with open('ips_located.json', 'w') as o:
    json.dump(data, o, indent=4)