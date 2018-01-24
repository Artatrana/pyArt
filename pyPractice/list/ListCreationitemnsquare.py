li =[]
for i in range(1,6):
    li.append((i,i*i))
print(li)
    
#Another way to do it
li1 =[(i,i**2) for i in range(1,6)]
print(li1)   
    