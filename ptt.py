import random
def kargo_gonder():
    alıcı = input("Alıcının İsmini Giriniz: ")
    soyadı = input("Alıcının Soyİsmini Giriniz: ")
    adres = input("Alıcının Adresini Giriniz: ")
    agırlık = input("Kargonun Ağırlığını Giriniz: ")
    print(f"Gönderdiğiniz {alıcı},{soyadı} Kargosu {adres} yola çıkmıştır!")
def para_gonder():
    alıcı = input("Alıcının İsmini Giriniz: ")
    iban = input("Alıcının İbanını Giriniz: ")
    para = float(input("Gönderilcek Miktarı Giriniz: "))
    print(f"{alıcı},Olan Kişinin {para},miktar kadarıyla {iban},Gönderilmiştir")
def fatura_ode():
    Ad = input("İsminizi Giriniz: ")
    Soyisim = input("Soyİsminizi Giriniz: ")
    fatura_numarası = int(input("Fatura Numarasını Giriniz: "))
    print (f"Sayın {Ad},{Soyisim} Girdiğiniz {fatura_numarası} fatura Ödenmiştir.")
while True:
    print("\nİşlem Seçiniz")
    print("1 - Kargo İşlemleri")
    print("2 - Havale-Para Transfer işlemleri")
    print("3 - Fatura İşlemleri")
    print("4 - İşlem Yapmamak İçin 0 Yazınız")
    
    secim = input("Seçimizi Yapınız: ")
    if secim == "1":
        kargo_gonder()
    elif secim == "2":
        para_gonder()
    elif secim == "3":
        fatura_ode()
    elif secim == "0":
        print("Çıkış yapıldı. İyi günler!")
        break
    else:
        print("Geçersiz İşlem Girdiniz")