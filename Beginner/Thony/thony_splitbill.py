# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# '''tipe1'''
# name_len = len(names)
# namar = names[random.randint(0,name_len-1)]
# 
# print(f"{namar} is going to buy the meal today!")

'''tipe2'''
names_l = len(names)
random_a = random.randint(0,names_l-1)
pay = names[random_a]

print(f"{pay} is going to buy the meal today!")

