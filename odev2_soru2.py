def f(x):
    return x ** 3 + 4 * x ** 2 - 10

a = 1  # Aralık başlangıcı
b = 2  # Aralık sonu
epsilon = 1e-6  # Hata payı
iteration = 0  # İterasyon sayısı

while True:
    iteration += 1
    fa = f(a)
    fb = f(b)
    c = (a + b) / 2  # Aralığın orta noktası

    fc = f(c)

    if abs(fc) < epsilon or iteration >= 4:
        print(f"Bulunan çözüm: {c}")
        break

    if fa * fc < 0:  # Kök aralığı değiştirme koşulu
        b = c
    else:
        a = c

    print(f"Iterasyon {iteration} çözüm: {c}")
