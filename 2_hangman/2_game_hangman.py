import random 
import os,sys
def select():
    a=random.randint(0,214)
    with open("./2_hangman/word_hangman.txt","r",encoding="utf-8") as f:
        words=[line for line in f]
        word= list(words[a])    
        word.pop()
        del words     
    return word    

lives=8
word=select()
print(word)
space_word= []
for i in word: space_word.append("_")
while space_word != word:
    b=len(space_word)
    if lives>0:
        for i in range (0,b): print(space_word[i],end=" ")
        letter= input("\n \nwrite a letter[a-z]: ")
        comprobation= letter in word
        if comprobation:
            for i in range(0,b):
                if letter==word[i]:space_word[i]=letter
        else:
            lives-=1
    os.system("cls")
    if space_word == word:
        for i in range (0,b): print(space_word[i],end=" ")
        print("\n \n ¡CONGRATULATIONS!")
    if lives==0:
        print("¡you lose the game!")
        break
