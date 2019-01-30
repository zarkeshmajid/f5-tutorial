user_input = input("what is yoru first name ")
print (" hello " + user_input + "!")
names = ['Aaron','Bob','John','Paddy'] # list of names, this should be stored in redis
ctr = len(names) -1
ctr2 = 0 # ctr for looping through 
for x in names:
	if user_input == x:
		print(user_input +' you are already in th VIP list')
		break #will loop through names, if user input is  in list will print statment
	if ctr2 == ctr:
		print("your name was not in the list" + user_input)
		add_to_list = input(" would you like to be added to list") # see if want to be added to party list
		if add_to_list == "yes" or "Yes":
			print('you are part of the VIPlist now')
			names.append(user_input) # if name is not in list and it has looped through full list
								# this if statment will add the users name to the list
			break
		elif add_to_list == "no" or "No":
			print('you will not be added to list')
			break
	ctr2 += 1
ctr2 = 0 # reseting the internal counter 


## ideally i would have stored list in redis, then instead of apending names list 
## i would LPUSH the name into the list stored in redis





	
