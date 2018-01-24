#python program to remove the nth occurance of the word from a list
#l = ['A', 'B', 'A', 'A', 'C', 'A']
l =['apple', 'apple', 'ball', 'ball', 'cat']
word_to_remove = 'ball1'
occu = 2
count = 0 

for i in l:
    if i == word_to_remove:
        count += 1
        if count != occu :
            l.remove(i)
    

if count ==0 :
    print("The word is not present ")

print(l)