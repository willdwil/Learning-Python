import random
batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kertas = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
'''tipe 1'''
# print("Selamat datang di Program Suit")
# user = input("Silahkan pilih 1 = Batu, 2 = Gunting, 3 = Kertas? ")
# print("\n")
# 
# if user == "1":
#   print(f" Kamu :{batu}")
# elif user == "2":
#   print(f" Kamu :{gunting}")
# else:
#   print(f" Kamu :{kertas}")
# 
# print("Aku :")
# 
# 
# cop = random.randint(0,2)
# 
# if cop == 0:
#   print(batu)
#   if user == "1":
#     print("Cie Sehati 🥰😊")
#   elif user == "2":
#     print("Yeay Aku menang 😎😋")
#   else:
#     print("Yah Aku Kalah 🥺😭")
# elif cop == 1:
#   print(gunting)
#   if user == "1":
#     print("Yah Aku Kalah 🥺😭")
#   elif user == "2":
#     print("Cie Sehati 🥰😊")
#   else:
#     print("Yeay Aku menang 😎😋")
# else:
#   print(kertas)
#   if user == "1":
#     print("Yeay Aku menang 😎😋")
#   elif user == "2":
#     print("Yah Aku Kalah 🥺😭")
#   else:
#     print("Cie Sehati 🥰😊")
    
'''tipe 2'''
game_images = [batu, gunting, kertas]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end