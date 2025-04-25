print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Hazine Adasına Hoş Geldin!")
print("Görevin: Hazineyi bulmak!")

choice1 = input('Bir yol ayrımındasın. Hangi yöne gitmek istersin? "sol" ya da "sağ" yaz: ').lower()

if choice1 == "sol":
    choice2 = input('Bir göle geldin. Gölün ortasında bir ada var. '
                    '"bekle" yazarak bir tekne bekleyebilir ya da "yüz" yazarak yüzebilirsin: ').lower()
    
    if choice2 == "bekle":
        choice3 = input('Sağ salim adaya ulaştın. Karşında 3 kapılı bir ev var;biri kırmızı, biri sarı, biri mavi. Hangi rengi seçiyorsun?').lower()
        
        if choice3 == "kırmızı":
            print("Canavarlarla dolu bir odaya girdin. Oyun Bitti 🐺")
        elif choice3 == "sarı":
            print("Hazinenin yerini buldun! Oyunu Kazandın! 🎉")
        elif choice3 == "mavi":
            print("Burası ateş dolu bir oda. Oyun Bitti 🔥")
        else:
            print("Geçersiz bir kapı seçtin. Oyun Bitti ❌")
    else:
        print("Saldırgan bir alabalık sana saldırdı. Oyun Bitti 🐟")
else:
    print("Bir çukura düştün. Oyun Bitti 🕳️")