panjang=int(input("masukan panjang bilangan = "))
fibo=[0,1]
print("pada baris ke 1 :", fibo)
for i in range (2, panjang) :
    angka1=fibo[i-2]
    angka2=fibo[i-1]
    angka_selanjutnya=angka1+angka2

    fibo.append(angka_selanjutnya)
    print("pada baris ke ", i, " : ", fibo)