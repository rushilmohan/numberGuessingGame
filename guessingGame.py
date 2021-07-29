import random;

number = random.randint(1,9) 
chances = 0

print("Number Guessing Game")
print("Guess a number (between 1 and 9)")

while chances <= 4 :

    guess = int(input('Enter your guess : '))
    if(number < guess):
        print("Choose a number lesser than this")
        chances = chances + 1
    elif(number > guess):
        print("Choose a number greater than this")
        chances = chances + 1
   
    else:
        print("Great!! You did it")
        break

if(chances>4):
    print("YOU LOSE !!! TRY AGAIN")