#Write your code below this row 👇

for fzb in range(1, 101):
    if (fzb %3 == 0) and (fzb %5 == 0):
        print("FizzBuzz")
    elif fzb %3 == 0:
        print("Fizz")
    elif fzb %5 == 0:
        print("Buzz")
    else:
        print(fzb)