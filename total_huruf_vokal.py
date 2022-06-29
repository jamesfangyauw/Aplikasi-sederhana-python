huruf_vokal = {
    'a' : 0,
    'i' : 0,
    'u' : 0,
    'e' : 0,
    'o' : 0,
}
total_karakter_vokal = 0
total_huruf = 0
karakter = input("masukan kalimat atau kata= ").lower()
for huruf in karakter :
    if huruf in ["a", 'i', 'u', 'e','o'] :
        huruf_vokal[huruf] +=1
        total_karakter_vokal +=1
    total_huruf+=1
print(total_huruf)
print(huruf_vokal)
print(total_karakter_vokal)

