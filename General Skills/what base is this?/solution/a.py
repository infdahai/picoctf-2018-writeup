
import re
binary=raw_input()
binary = re.findall('(\d+)',binary)

print(binary)

ans = ''
for k in binary:
    ans+=chr(int(k,2))
print(ans)


hexa = raw_input()
hexa = re.findall('([0-9a-f]+) as ',hexa)[0]
ans = hexa.decode('hex')

print(ans) 

octo = raw_input()
octo=re.findall('[0-7]+',octo)
print octo
res = ''
for i in octo:
    res+= chr(int(i,8))
print(res)    