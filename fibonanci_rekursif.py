def fibonanci(n) :
    if n < 1 :
        return [n]
    listsebelumN = fibonanci(n-1)
    angka1 = listsebelumN[-2] if len(listsebelumN) > 2 else 0
    angka2 = listsebelumN[-1] if len(listsebelumN) > 2 else 1
    return listsebelumN + [angka1 + angka2]

panjang = int(input("masukan panjang deret fibonanci = "))
print(fibonanci(panjang-1))



# def fibonacci (n):
#   if n < 3 :
#       return [n]

#   return fibonacci(n - 1) + [n]

# print(fibonacci(10))

# def fibonacci (n):
#   if n < 1:
#     return [n]

#   listSebelumN = fibonacci(n - 1)
#   angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
#   angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

#   print('listSebelumN', listSebelumN)
#   print(f'angka1: {angka1}, angka2: {angka2}')

#   return listSebelumN + [n]

# print(fibonacci(3))