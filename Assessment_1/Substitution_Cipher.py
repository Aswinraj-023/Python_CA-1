#3) Substitution Cipher
encrypt=""  # assigning encrypt variable to an empty string
decrypt=""  # assigning decrypt variable to an empty string
string_1 = input("String 1 : ").upper()		# getting plain text from user & converting to uppercase
string_2 = input("String 2 : ").lower()		# getting encrypted text from user & converting to lowercase
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  # creating a list of 26 alphabets in uppercase
code =    ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']  # creating a list of 26 alphabets in reverse order in lowercase
for i in string_1: #accessing each values of string_1 
	if i in letters: #if value in i is in 'letters'
		index = letters.index(i)  #accessing the index values in letters using index values of string_1
		encrypt = encrypt + code[index]  # encrypting the plain text 
		decrypt = decrypt + letters[index]  #decrypting the encrypted text
if string_2==encrypt:  #comparing if user's encrypted text is equal to the encrypted text found
	print("String 2 is the encoded version of String 1") #if they are equal string_2 is the encoded text
else:   # if they aren't equal string_2 is not encoded text
	print("String 2 is not encoded version of String 1")  #printing string_2 is not encoded text
print("Plain Text : ",string_1)  # printing the plain text
print("Encrypted Text  is : ",encrypt)  # printing the encrypted text


