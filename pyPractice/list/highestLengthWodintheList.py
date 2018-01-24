#Python program to return the word having maximum length
l = ["Apple", "Ball","Cat" , "Dinosaur", "Bangalore","Mumbai", "Delhi"]

temp =l[0]
max_len = len(l[0])
for i in l:
    if len(i) > max_len:
        max_len = len(i)
        temp = i
        
print(temp , " has the highest length ", max_len)
    