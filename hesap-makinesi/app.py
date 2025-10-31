print("Hoşgeldiniz...")

sayi1 = int(input("İlk sayıyı giriniz lütfen: ")) #kullanıcıdan sayı girmesini istiyoruz.
sayi2 = int(input("İkinci sayıyı giriniz lütfen: "))

islem = input("yapmak istediğiniz işlemi seçiniz: + , - , * , /") #Kullanıcı işlem seçer.

#İşlem sonucunu ekrana yazdırma işlemi.
try:
    if islem == "+":
        print(f"Toplam işleminin sonucu: {sayi1 + sayi2} ")
    elif islem == "-":
        print(f"Çıkarma işleminin sonucu: {sayi1 - sayi2} ")   
    elif islem == "*":
        print(f"Çarpma işleminin sonucu: {sayi1 * sayi2} ")
    elif islem == "/":
        print(f"Bölme işleminin sonucu: {sayi1 / sayi2} ")
    else:
        print("Geçersiz işlem girdiniz. Tekrar deneyiniz.")
except ZeroDivisionError:
    print("Hata: Bir sayı sıfıra bölünemez!")





