while(True) :
 from bilangan_prima import menu, is_prima, list_prima #untuk import fungsi di file lain, harus 1 direktori
 pilih = menu()
 if pilih == 1 :
    y= int(input("masukan bilangan = "))
    is_prima(y)
    print(is_prima(y))
 elif pilih == 2 :
    a = int(input('masukan batas awal bilangan = '))
    b = int(input('masukan batas akhir bilangan ='))
    list_prima(a,b)
    print(list_prima(a,b)) 
 elif pilih == 3 :
     exit()
 else :
     print("pilihan anda tidak ada")