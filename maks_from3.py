# def maks(a,b,c) :
#     lst = [a,b,c]
#     return lst
# a=int(input('masukan nilai a= '))
# b=int(input('masukan nilai b= '))
# c=int(input('masukan nilai c= '))
# print(maks(a,b,c))
# print(max(a,b,c))#fungsi max untuk mencari yang terbesar dalam list
# lst = maks(a,b,c)
# lst.sort() #untuk mengurutkan dari yang terkecil 
# print(lst[2]) #mencetak yang terbesar yaitu index ke dua setelah diurutkan 

def angka_terbesar (a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b

  return c

def angka_terkecil (a, b, c):
  if a < b and a < c:
    return a
  elif b < a and b < c:
    return b

  return c

def nilai_tengah (a, b, c):
  if (b > a > c) or (c > a > b):
    return a
  elif (a > b > c) or  (c > b > a):
    return b
  
  return c

a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

i1 = angka_terkecil(a, b, c)
i2 = nilai_tengah(a, b, c)
i3 = angka_terbesar(a, b, c)

print(f'Urutan: {i1}, {i2}, {i3}')


