import os

print("Hadi bütçemizi düzenleyelim...")

dosya_adi = "butce.txt"

def dosya_olustur():
    if not os.path.exists(dosya_adi): #eger butce.txt yoksa oluşturur.
        try:
            with open (dosya_adi, "w", encoding = "utf-8") as dosya:
                dosya.write("")
        except (IOError, OSError): #input-output ve işletim sistemi hatalarını yakalar.
            print("Dosya oluşturulamadı. Lütfen dosya izinlerinizi kontrol ediniz.")
            return 

def butce_gor():
    #dosyada butce verısı var mı kontrol eder yoksa kullanıcıdan ıster.
    if not os.path.exists(dosya_adi) or os.path.getsize(dosya_adi) == 0: 
        return veri_al()
    try:        
        with open (dosya_adi, "r", encoding = "utf-8") as dosya: #eğer dosya varsa 
            ilk_satir = dosya.readline().strip()   #ilk satıra bakar. Bütçe verisini buladıysa yeniden veri almaya yonlendırır.
            return int(ilk_satir)
    except ValueError: #deger hatasını kontrol eder.
        print("Dosyadaki bütçe değeri geçersiz, lütfen yeniden girin.")
        return veri_al()
    except OSError:  #dosya hatası var mı yok mu kontrol eder.
        print("Dosya hatası.")
        return veri_al()

def veri_al():      #kullanıcıdan bütçesini öğrenip dosyaya yazar.
    while True:
        giris = input("Aylık toplam bütçenizi giriniz lütfen: ")
        try:
            butce = int(giris)
            break
        except ValueError:  #değer hatası kontrol ediliyor.
            print("Lütfen geçerli bir sayı giriniz.")
    try:
        with open (dosya_adi, "w", encoding = "utf-8") as dosya:
            dosya.write(str(butce) + "\n")
    except OSError:    #sistem hatası kontrol ediliyor.
        print("Sistem hatası.")        
    
    return butce

def gider_ekle():
    gider = input("Gider ismini yazınız lütfen: ")  # gider ve
    while True:
        tutar_giris = input("Bu ürünün tutarı ne kadar?: ") # tutarını kullanıcıdan alıp,
        try:
            tutar = int(tutar_giris)
            break
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    with open (dosya_adi, "a", encoding = "utf-8") as dosya: #dosyadaki verileri silmeden dosyanın sonuna ekler.
            dosya.write(f"ürün: {gider}, tutar: {tutar}\n")
    print(f"Gider eklendi: {gider} ({tutar} TL)")
    

def gider_hesapla():
    toplam_gider = 0
    if not os.path.exists(dosya_adi):
        return 0
    try:
        with open (dosya_adi, "r", encoding = "utf-8") as dosya:
            for satir in dosya:
                satir = satir.strip() #baştaki sondaki boşlukları atar.
                if not satir.startswith("ürün:"):
                    continue
                if "tutar:" not in satir:
                    continue
                try:
                    parcala = satir.split(",")
                    tutari_bol = parcala[1].split(":") #aslında liste görünümündeki yapı içindeki tutar verisine ulaşmak için indexe 
                    tutar =int(tutari_bol[1].strip()) #göre veriye ulaşma yapılıyor.
                    if tutar <= 0:
                        print("geçersiz işlem. Tutar negatif veya 0 olamaz. Lütfen geçerli bir sayı giriniz.")
                        continue
                    toplam_gider += tutar 
                except (IndexError, ValueError):  #hata bulursa devam edebilmesini sağlar. 
                    continue
    except OSError:
        print("Dosya hatası.")
        return 0
        
    print(f"Bu ayki toplam gideriniz: {toplam_gider}")
    return toplam_gider

def kalan_paramiz(butce, toplam_gider):
    try:
        b = int(butce)
        c = int(toplam_gider)
    except (TypeError, ValueError): #tip ve değer hatası kontrolü.
        print("Bütçe veya tutar sayısal değil.")
        return

    sonuc = b - c   #ilk butceden gıderı cıkartır ve 

    if sonuc <0:
        print(f"Bakiye: {sonuc} Dikkat - bakiyeye düştünüz.")
        return

    print(f"Finansal olarak şu an son durumunuz: {sonuc} TL") #son tutarı kullanıcıya gosterır.


def menu():
    dosya_olustur()
    butce = butce_gor()
    print("DEBUG:", type(butce), butce)  #çalıştırma sırasında alınan bir hatanın tespiti amacı bu satır kullanılmıştır.


    while True:
        print("""
        
        1. Bütçeyi Güncelle
        2. Gider Ekleyiniz
        3. Gider Hesaplayınız
        4. Kalan Paranızı Görün
        5. Çıkış
        
        """)
        
        islem = input("Yapmak istediğiniz işlemi seçiniz: (1-5): ")
            

        if islem == "1":
            butce = veri_al()
        elif islem == "2":
            gider_ekle()
        elif islem == "3":
            gider_hesapla()
        elif islem == "4":
            toplam = gider_hesapla()
            kalan_paramiz(butce,toplam)
        elif islem == "5":
            break
        else:
            print("Hatalı işlem. Lütfen yapmak istediğiniz işlemi seçiniz.")

if __name__ == "__main__":
    menu()





