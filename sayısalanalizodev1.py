import math
x = math.pi/5
gercekdeger = math.cos(x)
yaklasım1 = 1
hata1 = abs(gercekdeger - yaklasım1)
yaklasım2 = 1 - ((x ** 2) / 2)
hata2 = abs(gercekdeger - yaklasım2)
print("Gerçek Değer: ", gercekdeger)
print("Tek Terimli Yaklaşım: ", yaklasım1)
print("İki Terimli Yaklaşım: ", yaklasım2)
print("Tek Terimli Hata: ", hata1)
print("İki Terimli Hata: ", hata2)
