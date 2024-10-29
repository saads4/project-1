#developing a simple game of rock paper scissors
print("enter your choice \n rock \n scissors \n paper")
def win():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("you win")
    engine.runAndWait()
def loose():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("you loose")
    engine.runAndWait()
def draw():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("its a draw")
    engine.runAndWait()
def invalid():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("invalid input")
    engine.runAndWait()
import random
user= input("enter ur choice    ")
import pyttsx3
engine = pyttsx3.init()
engine.say( "Rock Paper Scissors shoot")
engine.runAndWait()
computer=random.choice(("rock","paper","scissors"))
print("u choose  "+user)
print("computer chooses  "+computer)
if(user==computer):
    draw()
    print("Draw")
elif(user=="rock" and computer=="paper"):
    loose()
    print("you loose")
elif(user=="paper" and computer=="scissors"):
    loose()
    print("you loose")
elif(user=="scissors" and computer=="rock"):
     loose()     
     print("you loose")   
elif(user=="scissors" and computer=="paper"):
    win()
    print("you win")
elif(user=="paper" and computer=="rock"):
    win()  
    print("you win")
elif(user=="rock" and computer=="scissors"):
    win()
    print("you win")
else:
    print("invalid") 
    invalid()  
    
