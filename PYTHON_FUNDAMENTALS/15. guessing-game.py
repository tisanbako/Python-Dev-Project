#Lets write a code for a game that will guess a secret number.
#we want players to guess only 3 times, not more than 3

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit: 
    guess = int(input("Guess secret number: "))
    guess_count=1+guess_count
    if guess == secret_number:
        print("you won!")
        break
else:
    print("sorry, you failed")
    
   
    