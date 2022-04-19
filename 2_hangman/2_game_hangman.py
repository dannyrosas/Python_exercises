from pickle import FALSE
import random 
import os,sys

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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
b=len(space_word)
while space_word != word:
    if lives>0:    
        control=1
        while control==1:
            for i in range (0,b): print(space_word[i],end=" ")
            try:
                print(f"\n \n \nyou have {lives} lives")
                letter= input("write a letter[a-z]: ")
                letter=letter.lower()
                pools= letter in alphabet                
                if pools:
                    control=2
                else:
                    raise ValueError
            except ValueError:
                os.system("cls")
                print("you only can input a caracter bweteen in [a-z]")

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