import random

print("Hoşgeldiniz..")

skorunuz = 0
bilgisayar_skoru = 0

for i in range(3):

    print(f"            {i+1}. Tur          ")

    secim = input(["taş", "kağıt", "makas"]) #kullanıcı seçim yapar.

    bilgisayar_secimi = random.choice(["taş", "kağıt", "makas"]) #bilgisayar seçimi.

    print(f"seçtiğiniz taş: {secim}, bilgisayarın seçimi: {bilgisayar_secimi}") #seçilen taşlar ekranda gösterirlir. 

    #Taşların kontrolü yapılır ve kazanan ekrana yazdırılır. 
    if bilgisayar_secimi == secim:
        print("Berabere")
    elif (
        (secim == "taş" and bilgisayar_secimi == "makas") 
        or (secim == "kağıt" and bilgisayar_secimi == "taş") 
        or (secim == "makas" and bilgisayar_secimi == "kağıt")
    ):
        print("Tebrikler kazandınız..!")
        skorunuz +=1
    else:
        print("Bilgisayar kazandı.")
        bilgisayar_skoru +=1

print(f"Sonuç: Siz: {skorunuz} - Bilgisayar: {bilgisayar_skoru}")

