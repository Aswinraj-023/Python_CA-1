#2) Guessing game
import random #importing random function to generate random numbers
guesses = 5  # Total chances or guesses for a player is 5 
comp_guess = random.randint(1,100)  # assigning computer guess to random values from 1 to 100 using random function
for i in range(1,guesses+1):   #looping the guess value  from 1 to 5 using range()
  player = int(input("Enter your guess (1-100) : ")) # getting input as integer from player to guess a number from 1 to 100
  if player==comp_guess:     #if player's guess is equal to computer guess 
    print(" You won")     # the player wins
    break               # breaks the loop and ends the game if the player wins
  elif player<comp_guess:   # if player's guess is less than computer's guess the computer gives a clue 
    print("Computer guess is Higher")   
  elif player>comp_guess:    # if player's guess is greater than computer's guess the computer gives a clue 
    print("Computer guess is Lower")
  print("you have", guesses-i, "guesses left")  # printing the number of guesses or chances left for the player
  i=i+1   # iterating i value to six 
  if i==guesses+1 :   #if the total number of guesses exceeds 5 the player looses
    print("You Lost","\nThe number is  : ",comp_guess)   #printing the user has lost & the computer's guess
  

     
