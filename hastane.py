print("Merhaba İzmir Yeşilyurt Hastanesine Hoşgeldiniz!")


def Kardiyoloji():
    print("Merhaba Kardiyoloji Bölümüne Hoşgeldiniz")
    print("\nLütfen Doktor Seçimi Yapınız:")
    print("1. Ayşe\n2. Murat\n3. Demir")
    doktorlar = input("Seçiminiz (1-2-3): ")

    if doktorlar == "1":
        print("Kardiyoloji Bölümünden Ayşe Hanım Seçilmiştir.")
    elif doktorlar == "2":
        print("Kardiyoloji Bölümünden Murat Bey Seçilmiştir.")
    elif doktorlar == "3":
        print("Kardiyoloji Bölümünden Demir Bey Seçilmiştir.")
    else:
        print("Geçersiz seçim!")
        return

    print("Randevu Saatleri:")
    print("1. 14:00\n2. 15:00\n3. 16:00")
    saat_secimi = input("Saat Seçiniz (1-2-3): ")

    if saat_secimi == "1":
        print("14:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat_secimi == "2":
        print("15:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat_secimi == "3":
        print("16:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    else:
        print("Geçersiz randevu seçimi!")


def Dahiliye():
    print("Merhaba Dahiliye Bölümüne Hoşgeldiniz!")
    print("\nLütfen Doktor Seçimi Yapınız:")
    print("1. Sayit\n2. Serdar\n3. Sıla")
    dahiliye = input("Seçiminiz (1-2-3): ")

    if dahiliye == "1":
        print("Dahiliye Bölümünden Sayit Bey Seçilmiştir.")
    elif dahiliye == "2":
        print("Dahiliye Bölümünden Serdar Bey Seçilmiştir.")
    elif dahiliye == "3":
        print("Dahiliye Bölümünden Sıla Hanım Seçilmiştir.")
    else:
        print("Geçersiz seçim!")
        return

    print("Randevu Saatleri:")
    print("1. 15:00\n2. 16:00\n3. 18:00")
    saat = input("Randevu Saati Seçiniz (1-2-3): ")

    if saat == "1":
        print("15:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat == "2":
        print("16:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat == "3":
        print("18:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    else:
        print("Geçersiz randevu seçimi!")


def Göz_Hastalıkları():
    print("Merhaba Göz Hastalıkları Bölümüne Hoşgeldiniz!")
    print("\nLütfen Doktor Seçimi Yapınız:")
    print("1. Anıl\n2. Çağla\n3. Pelin")
    doktor = input("Seçiminiz (1-2-3): ")

    if doktor == "1":
        print("Göz Hastalıkları Bölümünden Anıl Bey Seçilmiştir.")
    elif doktor == "2":
        print("Göz Hastalıkları Bölümünden Çağla Hanım Seçilmiştir.")
    elif doktor == "3":
        print("Göz Hastalıkları Bölümünden Pelin Hanım Seçilmiştir.")
    else:
        print("Geçersiz seçim!")
        return

    print("Randevu Saatleri:")
    print("1. 08:00\n2. 09:30\n3. 11:30")
    saat = input("Randevu Saati Seçiniz (1-2-3): ")

    if saat == "1":
        print("08:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat == "2":
        print("09:30 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat == "3":
        print("11:30 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    else:
        print("Geçersiz randevu seçimi!")


def Ortopedi():
    print("Merhaba Ortopedi Bölümüne Hoşgeldiniz!")
    print("\nLütfen Doktor Seçimi Yapınız:")
    print("1. Hatice\n2. Ümit\n3. Deniz")
    doktor = input("Seçiminiz (1-2-3): ")

    if doktor == "1":
        print("Ortopedi Bölümünden Hatice Hanım Seçilmiştir.")
    elif doktor == "2":
        print("Ortopedi Bölümünden Ümit Bey Seçilmiştir.")
    elif doktor == "3":
        print("Ortopedi Bölümünden Deniz Hanım Seçilmiştir.")
    else:
        print("Geçersiz seçim!")
        return

    print("Randevu Saatleri:")
    print("1. 08:00\n2. 09:00\n3. 10:00")
    saat = input("Randevu Saati Seçiniz (1-2-3): ")

    if saat == "1":
        print("08:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat == "2":
        print("09:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    elif saat == "3":
        print("10:00 saatine randevunuz alınmıştır. Lütfen randevunuza geç kalmayınız.")
    else:
        print("Geçersiz randevu seçimi!")
while True:
    print("\nLütfen İstediğiniz Bölümü Seçiniz:")
    print("1. Kardiyoloji Bölümü")
    print("2. Dahiliye Bölümü")
    print("3. Göz Hastalıkları Bölümü")
    print("4. Ortopedi Bölümü")
    print("5. İşlemi Sonlandır")

    secim = input("Seçiminiz (1-5): ")

    if secim == "1":
        Kardiyoloji()
    elif secim == "2":
        Dahiliye()
    elif secim == "3":
        Göz_Hastalıkları()
    elif secim == "4":
        Ortopedi()
    elif secim == "5":
        print("İşlem sonlandırıldı. Sağlıklı günler dileriz.")
        break
    else:
        print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir değer giriniz.")