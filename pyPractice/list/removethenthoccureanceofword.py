#python program to remove the nth occurance of the word from a list
#l = ['A', 'B', 'A', 'A', 'C', 'A']
l ='apple', 'apple', 'ball', 'ball', 'cat'
word_to_remove = 'ball'
new_lst =[]
occu = 2
count = 0 

for i in l:
    if i == word_to_remove:
        count += 1
        if count != occu :
            new_lst.append(i)
    else:
        new_lst.append(i)

if count ==0 :
    print("The word is not present ")

print(new_lst)
    
        
    
    