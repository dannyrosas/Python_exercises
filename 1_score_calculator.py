def fully_array(name,count):
    var_1=float(input(f"write {name} number {count}: "))
    return var_1

def calcu(num,num2):
    num2= num2/100
    var_1=num*num2
    return var_1

def printing_list(number_control, array1, array2):
    c=0
    while c < number_control:
        print(f"the score {(c+1)} : {array1[c]} value is {array2[c]}% ")
        c+=1

scores_No= int(input("how many scores do you want calculated:"))
name_1= "the score"
name_2= "the percent"
scores=[]
percentages=[]
count=1
sum=0
while count<= scores_No:
    var=fully_array(name_1,count)
    if var < 0:
        print("alert, Write value in range")
        continue

    varr=fully_array(name_2,count)

    if varr<=0 or varr>100:
        print("alert, Write value in range (0-100)")
        continue

    percentages.append(varr)
    scores.append(var)
    sum+=calcu(scores[(count-1)],percentages[(count-1)])
    count+=1

    if count > scores_No:
        printing_list(scores_No,scores,percentages)
        a=int(input("if these value are right press 1 or if those value are wrong press any number: "))
        if a == 1:
            pass
        else:
            count=1
            sum=0
            scores=[]
            percentages=[]
print(f"your total score is: {sum}")
    

