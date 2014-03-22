aList=[{'a':'f','b':'1'},{'a':'y','b':'2'},
    {'a':'x','b':'3'},{'a':'g','b':'4'}]
tem = []

for i in aList:
    tem.append(i['a'])
tem.sort()

T = []
for i in tem:
    for item in aList:
        if i == item['a']:
            T.append(item)

print T
