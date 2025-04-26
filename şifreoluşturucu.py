import random

harfler = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sayilar = ['0','1','2','3','4','5','6','7','8','9']
semboller = ['!','#','$','%','&','(', ')',',','*','+']

print("PyPassword Şifre Üreticisine Hoşgeldiniz!")
nr_harfler = int(input("Şifrenizde kaç harf olsun istersiniz?\n"))
nr_semboller = int(input("Kaç tane sembol olsun istersiniz?\n"))
nr_sayilar = int(input("Kaç tane sayı olsun istersiniz?\n"))

sifre_listesi = []
for char in range(0, nr_harfler):
    sifre_listesi.append(random.choice(harfler))
    
for char in range(0, nr_semboller):
    sifre_listesi.append(random.choice(semboller))

for char in range(0, nr_sayilar):
    sifre_listesi.append(random.choice(sayilar))

print(sifre_listesi)
random.shuffle(sifre_listesi)
print(sifre_listesi)

sifre = ""
for char in sifre_listesi:
    sifre += char

print(f"Şifreniz: {sifre}")