#Write your code below this row 👇

hasil = 0
for tambah in range(0, 101, 2):
    hasil += tambah
print(hasil)

hasil2 = 0
for tambah2 in range(1, 101):
    if tambah2 %2 == 0:
        hasil2 += tambah2
print(hasil2)