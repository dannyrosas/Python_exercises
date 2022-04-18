import random 

def select():
    a=random.randint(0,214)
    with open("./2_hangman/word_hangman.txt","r",encoding="utf-8") as f:
        words=[line for line in f]
        word= list(words[a])    
        word.pop()
        del words     
    return word    
    
print(select())