import random

a="ROCK"
b="PAPER"
c="SCISSORS"

sec=random.choice([a,b,c])

score=0
comp_score=0
rounds=0
max_rounds=5

while rounds<max_rounds:
    guess=input("ROCK , PAPER , SCISSORS....SHOOT: ")
    rounds+=1

    if guess==sec:
        print("YOU HAVE WON THIS ROUND")
        score+=1
    else:
        print(" YOU LOST THIS ROUND")
        comp_score+=1
if score>comp_score:
    print("YOU WON")
else:
    print("I WIN NIGGA")

