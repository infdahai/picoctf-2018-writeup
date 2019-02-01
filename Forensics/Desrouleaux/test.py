import json

js = json.load(open('incidents.json'))
tickets=js['tickets']
hashes = dict()

for ti in tickets:
    if ti['file_hash'] not in hashes.keys():
        hashes[ti['file_hash']]=[ti['dst_ip']]
    else:
        hashes[ti['file_hash']].append(ti['dst_ip'])

print(hashes)
result = 0
for k in hashes.keys():
    result+=len(hashes[k])
sum = result / len(hashes)

print(sum)