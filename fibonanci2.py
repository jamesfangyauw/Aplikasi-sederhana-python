angka1,angka2=0,1
total = 1
ulang = 1

while (ulang == 1):
 angka1,angka2=0,1
 total = 1
 jumlah=int(input("masukan jumlah bilangan = "))
 for i in range(jumlah) :
    if i < 2 :
        print(i, end=" ")
    else :
        angka_selanjutnya=angka1+angka2
        print(angka_selanjutnya, end=" ")
        angka1 =angka2
        angka2 = angka_selanjutnya
        if angka_selanjutnya < 10 :
            total = total + angka_selanjutnya
        else :
            if 10 <=angka_selanjutnya <100 :
                digit_puluhan=angka_selanjutnya//10
                digit_satuan = angka_selanjutnya%10
                total = total + digit_puluhan + digit_satuan
            elif 100 <= angka_selanjutnya <1000 :
                digit_ratusan = angka_selanjutnya//100 
                digit_puluhan=(angka_selanjutnya%100)//10
                digit_satuan = ((angka_selanjutnya%100)%10)
                total = total + digit_ratusan + digit_puluhan + digit_satuan
            else :
                if 1000 <= angka_selanjutnya < 10000 :
                    digit_ribuan = angka_selanjutnya//1000
                    digit_ratusan = (angka_selanjutnya%1000)//100
                    digit_puluhan = ((angka_selanjutnya%1000)%100)//10
                    digit_satuan = (((angka_selanjutnya%1000)%100)%10)
                    total = total + digit_ribuan + digit_ratusan + digit_puluhan + digit_satuan
                elif 10000 <= angka_selanjutnya < 100000 :
                    digit_puluhan_ribu = angka_selanjutnya // 10000
                    digit_ribuan = ((angka_selanjutnya % 10000)//1000)
                    digit_ratusan = (((angka_selanjutnya % 10000)%1000)//100)
                    digit_puluhan = ((((angka_selanjutnya % 10000)%1000)%100)//10)
                    digit_satuan = ((((angka_selanjutnya % 10000)%1000)%100)%10)
                    total = total + digit_puluhan_ribu + digit_ribuan + digit_ratusan + digit_puluhan + digit_satuan                            

 print("\ntotal semua digit pada deret ialah", total)
 ulang = int(input("apakah anda ingin mengulang program ? (1/0)"))



 


         

    
