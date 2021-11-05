#1 ) Rocket launch countdown
start =int(input("Enter the start count :"))  #getting start value as integer from user
stop =int(input("Enter the stop count :"))    #getting stop value as integer from user
print("Count Down starts ")   # printing the message before countdown starts
while stop<=start:    # the countdown will start and run until the stop value is less than or equal to the start value
  print(start)      #prints the countdown 
  start-=1           # decrementing the start value till the countdown becomes one
print("Ready to launch")  # prints the message when the countdown stops
