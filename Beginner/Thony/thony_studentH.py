# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
jumlah = 0
for hitung in student_heights:
    jumlah += hitung 
    
anak = 0
for student in student_heights:
    anak += 1
    print(type(anak))

print(round(jumlah/anak))

