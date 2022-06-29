def faktorial (bilangan) :
    pass
bilangan = int(input("masukan bilangan = "))
print(faktorial(bilangan))

def faktorial(bilangan) :
    if bilangan < 2:
        return 1
    if bilangan > 1 :
        return bilangan*faktorial(bilangan-1)