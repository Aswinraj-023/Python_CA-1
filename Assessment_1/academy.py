#6 ) Addition Game
import random #importing random function
count =1  #declaring variable count for counting consecutive rows
while count<=3: #until count is less than or equal to 3 the below conditions will be executed
  a = random.randint(1,100) #declaring variable 'a' to generate random number
  b = random.randint(1,100) #declaring variable 'b' to generate random number
  c = a+b  #adding two variables and storing it in another variable 'c'
  print("______________________________________________________________")
  print("What is ",a,"+",b,"?") #asking the user about the sum of two variables 
  answer = int(input("Your answer : ")) #getting the answer in integer from user 
  if answer==c:   #comparing the users's answer & calculated answer
    count+=1  #iterating count value
    print("Correct! You've gotten",count-1,"correct in a row") #prints message & number of rows answered correctly
  else :  # if above condition is false 
    print("Incorrect! Expected answer is : ",c) #prints "Incorrect" and the correct answer
    count=1   #assigning the count value to one so that the number of rows answered correctly will start from 1 again
print("You've mastered addition") #prints message after 3 consecutive answers in a row
