import math

def toplama(x, y):
    return x + y

def çıkarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bölme(x, y):
    if y == 0:
        return "Hata: sıfıra bölünemez"
    return x / y

def karekok(x):
    if x < 0:
        return "Hata: negatif sayının karekökü alınamaz"
    return math.sqrt(x)

def faktoriyel(x):
    if x < 0:
        return "Hata: negatif sayının faktöriyeli yok"
    return math.factorial(x)

def us_alma(x, y):
    return x ** y

while True:
    print("\n📟 Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Karekök")
    print("6. Faktöriyel")
    print("7. Üs alma")
    print("0. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "0":
        print("Çıkılıyor...")
        break

    elif secim in ["1", "2", "3", "4", "7"]:
        x = float(input("Birinci Sayı: "))
        y = float(input("İkinci Sayı: "))
        if secim == "1":
            print("Sonuç:", toplama(x, y))
        elif secim == "2":
            print("Sonuç:", çıkarma(x, y))
        elif secim == "3":
            print("Sonuç:", carpma(x, y))
        elif secim == "4":
            print("Sonuç:", bölme(x, y))
        elif secim == "7":
            print("Sonuç:", us_alma(x, y))

    elif secim == "5":
        x = float(input("Sayı: "))
        print("Sonuç:", karekok(x))

    elif secim == "6":
        x = int(input("Sayı: "))
        print("Sonuç:", faktoriyel(x))

    else:
        print("❌ Geçersiz seçim!")