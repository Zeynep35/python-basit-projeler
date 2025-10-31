import time 

print("Hoşgeldiniz..")

while True:
    calısma_suresi = 25 * 60 #25 dakikalık bir pomodoro bölümünü önce saniyeye çeviriyoruz.
    dinlen = 5 * 60 
    
    for i in range(1500):
        calısma_suresi-=1  #geriye sayımı burada yapıyoruz.
        print(calısma_suresi)
        time.sleep(1)   #her döngüde bir saniye bekleme süresi ekliyor.

    for i in range(300):
        dinlen-=1  #geriye sayımı burada yapıyoruz.
        print(dinlen)
        time.sleep(1) 
    
    cevap = input("Dersin bitmesini istiyorsanız q'a basınız.")
    
    if cevap == "q":
        break
    
    


