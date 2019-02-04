

string = "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"
first=ord('p')-ord('4')
print("hahahah\n"+str(first))   
text =[]
flag=''
for i in string:
    k = (ord(i)+first)%126
    if k<65:
        k+=32
    text.append(k)
    flag+=chr((k))

print(text)
print(flag)
