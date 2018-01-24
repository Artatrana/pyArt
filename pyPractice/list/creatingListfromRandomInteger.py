#Python program to generate random numbers form 1 to 20 and append them inot list
import random
a =[]
for j in range(1,10):
    a.append(random.randint(1,20))
print(a)