import random

tas = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
kagit = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

oyun_gorselleri = [tas, kagit, makas]

kullanici_secimi = int(input("Ne seçiyorsun? 0 için Taş, 1 için Kağıt, 2 için Makas yaz.\n"))
if kullanici_secimi >= 0 and kullanici_secimi <= 2:
    print(oyun_gorselleri[kullanici_secimi])

bilgisayar_secimi = random.randint(0, 2)
print(f"Bilgisayar seçti:")
print(oyun_gorselleri[bilgisayar_secimi])

if bilgisayar_secimi == 0 and kullanici_secimi == 2:
    print("Kaybettin!")
elif kullanici_secimi == 0 and bilgisayar_secimi == 2:
    print("Kazandın!")
elif kullanici_secimi >= 3 or kullanici_secimi < 0:
    print("Geçersiz bir sayı girdin. Kaybettin!")
elif bilgisayar_secimi > kullanici_secimi:
    print("Kaybettin!")
elif kullanici_secimi > bilgisayar_secimi:
    print("Kazandın!")
elif bilgisayar_secimi == kullanici_secimi:
    print("Berabere!")