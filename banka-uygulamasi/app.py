print("X bankasına hoşgeldiniz")

accounts = { "A": 1000, "B":200}

gonderici = input("Gönderici ismini yazınız: ")
alici = input("Alıcı isminizi yazınız: ")
tutar =int(input("Göndermek istediğiniz tutarı giriniz: "))

def bakiye_gor():
    kullanici = input("Kullanıcı id'inizi giriniz: (A/B)")

    if kullanici in accounts:
        print(f"Toplam bakiyeniz: {accounts[kullanici]} TL")
    else:
        print("Hatalı kullanıcı id'si girdiniz.")

def para_transferi():

    gonderici = input("Gönderici id isminizi yazınız: (A/B)")
    alici = input("Alıcı isminizi yazınız: (A/B)")
    tutar =int(input("Göndermek istediğiniz tutarı giriniz: "))

    if accounts[gonderici] >= tutar:
        accounts[gonderici] -= tutar
        accounts[alici] += tutar
        print(f"Transfer işlemi başarılı gerçekleşti. Kalan bakiyeniz: {accounts[gonderici]}")
    else:
        print("Yetersiz bakiye.")



def menu():
    while True:
        print(
            """
            1. Bakiye gör
            2. Para transferi yap
            3. Çıkış
            """
        )

        islem = input("Yapmak istediğiniz işlemi seçiniz: (1-3): ")

        if islem == "1":
            bakiye_gor()
        elif islem == "2":
            para_transferi()
        elif islem == "3":
            print("Hoşçakalın..")
            break
        else:
            print("Hatalı seçim yaptınız lütfen yapmak istediğiniz işlemi seçin.")

def main():
    menu()

if __name__ == "__main__":
    main()