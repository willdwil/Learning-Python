# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cal = name1.lower() + name2.lower()

t = cal.count('t')
r = cal.count('r')
u = cal.count('u')
e = cal.count('e')
truee = str(t+r+u+e)

l = cal.count('l')
o = cal.count('o')
v = cal.count('v')
e = cal.count('e')
lovee = str(l+o+v+e)

true_love = int(truee+lovee)


if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

