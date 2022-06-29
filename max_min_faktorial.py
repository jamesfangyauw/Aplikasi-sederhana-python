def maksimum(list) :
    nilai_terbesar = list[0]
    
    if len(list) > 1 :
     next_nilai_terbesar = maksimum(list[1:])
     if next_nilai_terbesar > nilai_terbesar :
          nilai_terbesar = next_nilai_terbesar
          return nilai_terbesar
    return nilai_terbesar

list = []
banyak_anggota= int(input("masukan banyak anggota= "))
for i in range (banyak_anggota) :
    anggota= int(input("masukan anggota ="))
    list.append(anggota)
    
print(f"{list} -> {maksimum(list)}")