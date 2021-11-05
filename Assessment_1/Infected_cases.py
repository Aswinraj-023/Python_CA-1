#7) Checking infected cases
Evermore = [1,1,1,1,1,1,1]  # infected cases per day for a week in Evermore
Vanguard_City = [1,2,3,4,5,6,7] # infected cases per day for a week in Vanguard City
Excelsior = [1,1,2,3,5,8,13]  # infected cases per day for a week in Excelsior
Evermore_length = len(Evermore)  # declaring the length of the list Evermore
Vanguard_length = len(Vanguard_City)  # declaring the length of the list Vanguard_city
Excelsior_length = len(Excelsior) # declaring the length of the list Excelsior
Evermore_sum=0  #Assigning sum of infections of Evermore to 0, before calculation
i=0 #starting the iteration from 0
# Finding total number of infections in each location
print("__________________________________________\n\nTotal Numbers Of Infections\n__________________________________________\n")
# Finding total number of infections in Evermore
while i<Evermore_length: #Accessing the index value & iterating till the  length of evermore 
  Evermore_sum=Evermore[i]+Evermore_sum   #calculating the Total number of infections
  i+=1    # iterating 'i' till the final length of Evermore
print("Total number of infections in Evermore is : ",Evermore_sum)  #printing the total number of infections in Evermore
# Finding total number of infections in Vanguard_city
i=0 #starting the iteration from 0
Vanguard_sum=0  #Assigning sum of infections in Vanguard city to 0 before calculation
while i<Vanguard_length:  #Accessing the index value & iterating till the length of Vanguard City 
  Vanguard_sum=Vanguard_City[i]+Vanguard_sum  #calculating the Total number of infections
  i+=1  # iterating 'i' till the final length of Vanguard City
print("Total number of infections in Vanguard_City is : ",Vanguard_sum)   #printing the total number of infections in Vanguard City
# Finding total number of infections in Excelsior
i=0 #starting the iteration from 0
Excelsior_sum = 0 #Assigning sum of infections in Excelsior to 0 before calculation
while i<Excelsior_length: #Accessing the index value & iterating till the length of Excelsior 
  Excelsior_sum = Excelsior[i]+Excelsior_sum  #calculating the Total number of infections
  i+=1  # iterating 'i' till the final length of Excelsior
print("Total number of infections in Excelsior is : ",Excelsior_sum)  #printing the total number of infections in Excelsior
# Finding the infections per day at each location
print("__________________________________________\n\nInfections per day at each location\n__________________________________________\n")
i=0 #starting the iteration from 0
while i<7: # Accessing the index value & iterating till 7-1
  per = Evermore[i]+Vanguard_City[i]+Excelsior[i]  #Calculating Total Infections per day at each location
  print("Infections per day at each location : Day",i+1,":",per,"Cases")  #Printing infections per day at each location
  i+=1  #iterating 'i' till 7-1
print("__________________________________________\n\nHighest Infected population\n__________________________________________\n")
if Evermore_sum>Vanguard_sum and Evermore_sum>Excelsior_sum:  #comparing the sum of infections in Evermore, Vanguard city, Excelsior
  print("Location Evermore has highest infected population of : ",Evermore_sum," in these 7 days \n") #printing highest infected population & its Sum
elif Vanguard_sum>Evermore_sum and Vanguard_sum>Excelsior_sum: #comparing the sum of infections in Evermore, Vanguard city, Excelsior
  print("Location Vanguard_City has highest infected population of : ",Vanguard_sum," in these 7 days\n") #printing highest infected population & its Sum
else: #executes when above two condions are FALSE
  print("Location Excelsior has highest infected population of : ",Excelsior_sum," in these 7 days \n") #printing highest infected population & its Sum
