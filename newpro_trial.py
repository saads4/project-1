#guess the number game
import random 
num=random.randint(1,10)
c=0
while(c<=5):
        user_num=int(input("guess three digit number"))
        c=c+1 
        
        if(num>user_num):
            print("think of bigger number")
        elif(num<user_num):
                 print("think of smaller number")
        else:
            print("You won")     
            print("Your score is:",(5-c))
            print("Number was:" ,num) 
            break