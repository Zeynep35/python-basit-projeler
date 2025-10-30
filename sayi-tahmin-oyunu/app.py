import random #rastgele sayı için bu modülü içeri aktariyoruz.
print("Sayı tahmin oyununa hoşgeldiniz..!")

sayi = random.randint(0,100) #0 ile 100 arasında rastgele bir sayi üretir.
tahmin = -1 #başlangıç değeri farklı olmalı.

while sayi != tahmin:   #sayi ve tahmin aynı olmadığı sürece döngüye devam etmesini istiyoruz.
    
    tahmin = int(input("Tahminizi giriniz.")) #kullanıcıdan tahmin alıyoruz.
    if tahmin < sayi:
        print("Daha büyük bir sayı giriniz.")
    elif tahmin > sayi:
        print("Daha küçük bir sayı giriniz.")
    else:
        print("Tebrikler doğru bildiniz.")





