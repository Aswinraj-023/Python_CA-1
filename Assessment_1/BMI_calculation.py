#5) BMI calculation
weight = float(input("Enter the weight in kg : ")) #getting weight in integer from user
while weight < 0:
  if weight<0:  # if the weight is negative, user have to re-enter the weight
    print("Weight can't be negative, Please re-enter") #prints the message for above condition
    weight = float(input("Enter the weight in kg : "))
else: #else if weight is positive
  height = float(input("Enter the height in meters : ")) #getting height in float from user
  BMI = weight / (height*height)   #calculating BMI from given weight & height
  print("BMI IS : ",BMI)
  if BMI>25 :  #comparing whether BMI is greater than 25
    print("Estimated BMI is: Overweight")  #prints the message for above condition
  elif BMI>=18 and BMI<25 : #comparing whether BMI is between 18 to 25
    print("Estimated BMI is: Normal") #prints the message for above condition
  elif BMI<18 :  #comparing whether BMI is less than 18
    print("Estimated BMI is: Underweight") #prints the message for above condition
