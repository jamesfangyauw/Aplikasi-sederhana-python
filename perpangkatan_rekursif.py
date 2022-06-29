def perpangkat(bilangan, pangkat) :
 if pangkat>1 :
     return bilangan*perpangkat(bilangan, pangkat-1)
 return bilangan

bilangan = int(input("masukan bilangan = "))
pangkat = int(input("masukan pangkat = "))
print(perpangkat(bilangan, pangkat))