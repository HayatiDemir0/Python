print("Trafik Işıkların Görevleri!")
kullanıcı = input('Lütfen Bir Renk Giriniz "Kırmızı" "Sarı" "Yeşil:').lower()
if kullanıcı == "kırmızı":
    print("Dur")
elif kullanıcı == "sarı":
    print("Hazır Ol")
elif kullanıcı == "yeşil":
    print("Geç")
else:
    print("Geçersiz Renk Girdiniz")