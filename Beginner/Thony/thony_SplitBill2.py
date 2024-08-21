#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
'''tipe1'''
money = input("Welcome to the tip calculator!\nWhat was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
splitt = input("How many people to split the bill? ")

buy1 = float(money)/int(splitt)
tip1 = (int(tip)/100)+1
split1 = buy1 * tip1
end = "{:.2f}".format(split1)

# Where:
# 
# : introduces the format spec //memperkenalkan spesifikasi format
# .2 sets the precision to 2 //atur presisi menjadi 2
# f displays the number as a fixed-point number //menampilkan nomor sebagai nomor fixed-point
# format bagian yang diterapkan

print(f"\nEach person should pay: ${end}")

'''solution'''
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))
# 
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)