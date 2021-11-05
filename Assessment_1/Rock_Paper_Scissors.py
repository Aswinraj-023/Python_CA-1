#4)Rock, Paper & Scissors
score_a =0  #creating a variable score_a for score of player A
score_b =0  #creating a variable score_b for score of player B
game = 15  # total number of games to be played is 15
for i in range(1,game+1):  #iterating the below conditions till the range of 'game' ends
  print("---------------------------------------------------------------------------\n---------------------------------------------------------------------------")
  print("Game",i)   # printing the position of the game
  player_a = str(input("Player A : ")).upper() #getting input as string & converting to uppercase form player A
  player_b = str(input("Player B : ")).upper() #getting input as string & converting to uppercase form player B
  if player_a=="ROCK" and player_b=="ROCK" or player_a=="PAPER" and player_b=="PAPER" or player_a=="SCISSORS" and player_b=="SCISSORS":  # if input of player A & player B are equal no score is given
    print("No score, Try Again")  # prints message for the above condition
  elif player_a=="ROCK" and player_b=="PAPER":  #if score of player B is greater than Player A,  player B gets score
    score_b+=1   #iterating the score of player B 
    print("Paper covers rock . Player B wins\nPlayer B Score =",score_b)  #prints message & score for the above condition
  elif player_a=="PAPER" and player_b=="ROCK":  #if score of player A is greater than Player B,  player A gets score
    score_a+=1  #iterating the score of player A 
    print("Paper covers rock . Player A wins\nPlayer A Score =",score_a)  #prints message & score for the above condition
  elif player_a=="SCISSORS" and player_b=="ROCK":  #if score of player B is greater than Player A,  player B gets score
    score_b+=1  #iterating the score of player B 
    print("Rock breaks Scissors. Player B wins\nPlayer B Score =",score_b)  #prints message & score for the above condition
  elif player_a=="ROCK" and player_b=="SCISSORS":  #if score of player A is greater than Player B,  player A gets score
    score_a+=1  #iterating the score of player A 
    print("Rock breaks Scissors. Player A wins\nPlayer A Score =",score_a)  #prints message & score for the above condition
  elif player_a=="PAPER" and player_b=="SCISSORS":  #if score of player B is greater than Player A,  player B gets score
    score_b+=1  #iterating the score of player B 
    print("Scissors cuts Paper. Player B wins\nPlayer B Score =",score_b) #prints message & score for the above condition
  elif player_a=="SCISSORS" and player_b=="PAPER":  #if score of player A is greater than Player B,  player A gets score
    score_a+=1  #iterating the score of player A 
    print("Scissors cuts Paper. Player A wins\nPlayer A Score =",score_a) #prints message & score for the above condition
print("___________________________________________\n___________________________________________")
#comparing the scores of Player A & B
if score_a > score_b:  #if score of player A is greater than player B , player A wins 
  print("\n\nPlayer A Total Score : ",score_a,"\nPlayer B Total Score : ",score_b,"\nPlayer A wins ") #prints message & Total score for the above condition
elif score_a < score_b:   #if score of player A is less than player B , player B wins 
  print("\n\nPlayer B Total Score : ",score_b,"\nPlayer A Total Score : ",score_a,"\nPlayer B wins ")  #prints message & Total score for the above condition
elif score_a==score_b:  #if score of player A is equal toscore of player B , its a draw match 
  print("\n\nPlayer A Total Score : ",score_a,"\nPlayer B Total Score : ",score_b,"\nDraw match")  #prints message & Total score of each player for the above condition



        
