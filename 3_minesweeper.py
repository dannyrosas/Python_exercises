import random
import os


def table_creation(raws,colums,val):
    table=[]
    for i in range(raws):
        table.append([])
        for j in range(colums): table[i].append(val)
    return table

def show_table(table):
    for raw in table:
        for elem in raw:print(elem, end=" ")
        print()

def boms(table,bombs,raw,colum):
    hidden_bombs=[]
    num=0
    while num < bombs:
        y=random.randint(0,raw-1)
        x=random.randint(0,colum-1)
        if table[y][x] != 9:
            table[y][x]=9
            hidden_bombs.append((x,y))
            num+=1
    return table, hidden_bombs

def menu():
    print()
    option=input("Move: w/a/s/d Designate Bomb: b/v Select: x ::")
    option=option.lower()
    return option


colums=16
raws=12
visible_table=table_creation(raws,colums,"-")
hidden_table=table_creation(raws,colums,0)
hidden_table,hidden_bombs= boms(hidden_table,15,raws,colums)

y=random.randint(4,raws-4)
x=random.randint(4,colums-6)
real=visible_table[y][x]
visible_table[y][x]="x"

os.system("cls")

show_table(visible_table)

discovered_bombs=[]
play= True

while play:
    mov=menu()
    if mov=="w":
        if y==0:
            y==0
        else:
            visible_table[y][x]=real
            y-=1
            real=visible_table[y][x]
            visible_table[y][x]="x"
    elif mov=="s":
        if y==raws-1:
            y==raws-1
        else:
            visible_table[y][x]=real
            y+=1
            real=visible_table[y][x]
            visible_table[y][x]="x"    
    elif mov=="a":
        if x==0:
            x==0
        else:
            visible_table[y][x]=real
            x-=1
            real=visible_table[y][x]
            visible_table[y][x]="x"
    elif mov=="d":
        if x==colums-1:
            x==colums-1
        else:
            visible_table[y][x]=real
            x+=1
            real=visible_table[y][x]
            visible_table[y][x]="x"

    os.system("cls")
    show_table(visible_table)
    print()
    show_table(hidden_table)
    pass

