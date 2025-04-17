from random import randint
gamble_score = 50
def login():
    with open('practise.txt','r') as f:
        lines=f.readlines()
        name=input("please enter your name as saved before : ").lower()
        for i in lines:
            user,score=i.strip('\n').split('|')
            if user==name:
                print('Hello ',user,' your saved score is : ',score)
                return [int(score),user]

def signup():
    name = str(input("enter your name for signup : "))
    with open('practise.txt','a') as f:
        f.write('\n'+name+'|50')
        print('welcome ',name,' !! signup successful!!')

def save():
    with open('practise.txt','r') as f:
        lines=f.readlines()
        with open('practise.txt','w') as fw:
            for line in lines:
                if line.find(name)==-1:
                    fw.write(line)
    with open('practise.txt','a') as f:
        data = f.write('\n'+name+'|'+str(gamble_score))
    print('hello ',name,' your score successfully saved')


print()
if gamble_score < 0:
    gamble_score = 0
while gamble_score>0:
    user_input= str(input('enter from the given below \n(login) or (signup) or (heist) or (gamble) or (points) or (help) or (save) : \n').strip(" ").lower())
    #this is for gamble
    if user_input=='gamble':
        a = randint(1, 100)
        amount = int(input("enter gamble amount : "))
        if amount<=gamble_score:
            if a in range(1,49):
                gamble_score=gamble_score-amount
            elif a in range(50,99):
                gamble_score=gamble_score+amount
            else:
                gamble_score = gamble_score+(2*amount)
            print('|=| dice is rolled..your roll is: ', a, '-----your score is: ', gamble_score)
        else:
            print("your score is very low sorry!!")

    #this is for heist
    elif user_input=='heist':
        heist_amount=int(input("enter heist amount : ").strip(" "))
        b=randint(1,2)
        if heist_amount<=gamble_score:
            if b==1:
                gamble_score=int(gamble_score+(2.5*heist_amount))
                print("you escaped !! and the total amount is : ",gamble_score)
            elif b==2:
                gamble_score=int(gamble_score-(1.5*heist_amount))
                print("you got killed in the heist..so sad!!, remaining score : ",gamble_score)
        else:
            print("your score is very low , sorry!!")

# code for printing points
    elif user_input=='points':
        print('your score is: ',gamble_score)
# code for duel option
    elif user_input=='duel':
        print()
        print('-------code under construction..will be avaliable soon--------')
        print()
#code for help option
    elif user_input=='help':
        print()
        print('='*100)
        print()
        print("**(for gamble) ,,a dice is rolled between 1 to 100 numbers\n    when you get 1 to 49 roll,"
              "then you will loose your amount..\n    if roll is 50 to 99, then you will get double the points..\n    "
              "when you get a roll of 100 , the u will get triple the amount\n"
              "\n**(for heist) ,,when u escaped the heist ,, then you will get 2.5 times the amount,\n"
              "    when you not escaped ,, you will loose 1.5 times the amount\n"
              "\n**(for points) ,, to know how much score or amount you have\n"
              "\n**(for dual),, its under construction..will be avaliable soon")
        print()
        print('='*100)

    elif user_input=='save':
        save()
    elif user_input=='signup':
        signup()
    elif user_input=='login':
        gamble_score,name=login()

    print()
    play=input("------wanna try your luck again? =====> \n  enter if 'yes' or type 'no' to exit : ").lower().strip(" ")
    if play =='no':
        break
    print("*"*60)
