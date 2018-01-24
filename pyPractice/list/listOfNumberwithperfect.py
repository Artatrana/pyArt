items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

a=[]
a=[x for x in range(1,100) if (int(x**0.5))**2 == x ]
print(a)