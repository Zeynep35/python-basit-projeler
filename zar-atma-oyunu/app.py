import random

while True:  #Kullanıcı devam ettiği sürece devam edebilmesi için True değerini verdik.
    zar = random.randint(1,6) #1 ile 6 arasında sayı üretir.
    print(f"Zar sonucu: {zar}")

    zar2 = input("Tekrar zar atmak ister misiniz? Evet ise e tuşuna basınız, hayır ise h tuşu.")

    if zar2 != "e":   #zar2 e değilse döngüden çıkar. 
        print("Hoşçakalın...")
        break #Döngüyü sonlandırır.

