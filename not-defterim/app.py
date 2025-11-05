import os
import json


print("Hoşgeldiniz....")

dosya_adi = "notlar.json"

def dosyayi_yukle():
    if not os.path.exists(dosya_adi): #eger dosya adı yoksa 
        return [] #boş liste döndürür
    with open (dosya_adi, "r", encoding="utf-8") as f: #dosya varsa dosyayı açar
        return json.load(f) #python listesine çevirir.

def dosyaya_kaydet(veri):
    with open (dosya_adi, "w", encoding="utf-8") as f:   #eski veriyi siler yeni notu ekler.
        json.dump(veri, f, ensure_ascii=False, indent=4) #düzgün yazı formatı için girinti verdik. json.dump() bu listeyi JSON formatına çevirip notlar.json dosyasına kaydeder.
#veri bir listedir. veri = [] gibi. 
    print("Kayıt işlemi başarılı..")

def not_ekle():
    notlar = dosyayi_yukle()
    yeni_not = input("Notunuzu giriniz: ")
    notlar.append(yeni_not)
    dosyaya_kaydet(notlar)
    print("İşlem başarılı.")

def not_listele():
    notlar = dosyayi_yukle()
    for i, not_ in enumerate(notlar, start=1):
        print(f"{i}.{not_}")   #not_ olma sebebi not pythonda yerleşik bir kelimedir. İsim çakışmasını önlemek için sonuna _ ekledik.
    

def not_sil():
    notlar = dosyayi_yukle()
    s = input("Hangi notu silmek istersiniz: ")
    notlar.remove(s)  #remove direk notu siler.
    dosyaya_kaydet(notlar)
    print(f"{s} notu listeden silinmiştir.")

    
    #s = input("Kaçıncı notu silmek istersiniz: ")
    #notlar.pop(s - 1)  #pop() indexe göre siler pythonda normalde index 0'dan başladığı için -1 diyoruz.
    #dosyaya_kaydet(notlar)
    #print(f"{s}. not listeden silinmiştir.")
    
    


def not_guncelle():
    notlar = dosyayi_yukle()
    not_listele()
    secim = int(input("Kaçıncı notu güncellemek istediğinizi seçin: "))
    yeni_notunuz = input("Notunuzu giriniz: ")
    notlar[secim-1]= yeni_notunuz  #index 0 dan başladığı için -1 verdik. 
    dosyaya_kaydet(notlar)
    print("Güncelleme başarılı.")





def menu():
    while True:
        print("""
        
        1. Not ekle
        2. Not Sil 
        3. Not güncelle 
        4. Notları göster
        5. Çıkış yap
        
        """)

        islem = input("Yapmak istediğiniz işlemi seçiniz: (1-5): ")

        if islem == "1":
            not_ekle()
        elif islem == "2":
            not_sil()
        elif islem == "3":
            not_guncelle()
        elif islem == "4":
            not_listele()
        elif islem == "5":
            exit()
        else:
            print("Hatalı seçim yaptınız lütfen yapmak istediğiniz işlemi seçin.")

def main():
    menu()

if __name__ == "__main__":
    main()

    

