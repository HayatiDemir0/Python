sayı = int(input("Sayı Tahmini Oyununa Hoşgeldiniz Lütfen Bi Sayı Giriniz: "))
if sayı == 45:
    print("Tebrikler Doğru Bildiniz")
elif sayı <= 45:
    print("Daha Büyük Bir Sayı Gir")
elif sayı >= 45:
    print("Daha Küçük bir Sayı Gir")
else:
    print("Game Over")