import celebritydata
import random
from os import system
# system("clear")

#Could put ascii art in there
print(celebritydata.art)

print("\n--- --- --- --- ---")
print("Welcome to HIGHER OR LOWER!")
print("To play, select the celebrity account which has the most followers.")
print("Accounts are selected by typing 'A' or 'B', try to get the highest score!")
print("--- --- --- --- ---\n")

start = input("Enter 'Y' to start or 'N' to quit!: ").upper()
if start == 'Y':
    game_playing = True
    system("clear")
else:
    game_playing = False
    print("Damn")

A = random.choice(celebritydata.data)

score = 0

while game_playing and len(celebritydata.data) > 1:
    print(celebritydata.art)

    print(f"Compare A: {A['name']}. {A['description']}, from {A['country']}.")
    A_followers = A['follower_count']

    celebritydata.data.remove(A) #Remove it so it doesn't get picked by B

    
    # print("\nVS.\n")
    print(celebritydata.vs)


    B = random.choice(celebritydata.data)
    print(f"Compare B: {B['name']}. {B['description']}, from {B['country']}.")
    B_followers = B['follower_count']


    celebritydata.data.append(A) #Add it back after finding B

    #celebritydata.data.pop(person2)

    if A_followers > B_followers:
        correct = 'A'
    elif B_followers > A_followers:
        correct = 'B'

    guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    if guess == correct:
        score += 1
        system("clear")
        print(f"You're right! Current score : {score}")
        if correct == 'B':
            celebritydata.data.remove(A)
            A = B
        elif correct == 'A':
            celebritydata.data.remove(B)
        # print(A) #Debug statement
    else:
        print(f"\nSorry, that's wrong. Final score: {score}\n")
        game_playing = False

    #print("hi!")
        
if len(celebritydata.data) < 2:
    print(f"\nCongratulations! You completed the game! \nFinal score: {score}\n")
    game_playing = False