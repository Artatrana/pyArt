#python program to sort list by the second item of the sublist
a=[['A',34],['B',21],['C',26]]
a.sort(key=lambda x:x[1])
print(a)

b=[['A',34],['B',21],['C',26]]
for i in range(0,len(b)):
    for j in range(0,len(b)-i-1):
        if b[j][1] > b[j+1][1]:
            b[j][1], b[j+1][1] = b[j+1][1], b[j][1]
            
print(b)
