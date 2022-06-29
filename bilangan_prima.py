def menu() :
  print(" menu bilangan prima")
  print(" silakan pilih menu dibawah ini : \n1. cek bilangan prima \n2. daftar bilangan prima \n3. exit")
  pilih = int(input(" masukan inputan anda = "))
  return pilih

def is_prima(x) :
 if x < 2 :
   return False
 for i in range(2,x) :
   if x%i == 0 :
    return False
 return True

def list_prima (awal, akhir) :
  list_deretPrima = []
  for x in range(awal, akhir+1):
    if is_prima(x) :
      list_deretPrima.append(x)
    
  return list_deretPrima


