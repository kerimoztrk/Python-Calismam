import random
import time

kullanicilar=list()


def kullaniciEkle(x):
    print("-"*30)
    print("KUllanici ekleme ekranına Hoşgeldiniz.")
    ekle=input("Lütfen eklenecek Kullanıcıyı yazınız : ")
    kullanicilar.append(ekle)
    input("Devam etmek için ENTER tuşuna basın")

def kullaniciGör(x):
    print("-"*30)
    sayac=1
    for i in x:
        print(str(sayac)+"-Kullanıcı Adı: ",i)
        sayac+=1
    print("-"*30)
    input("Devam etmek için ENTER tuşuna basın")

def KullaniciSec(x):
    sayac=1
    kisiSec=int(input("Kaç Kişi Seçilsin?: "))
    rastgeleSec=random.sample(x,kisiSec)

    for i in rastgeleSec:
        print(str(sayac)+"-Kullanıcı Adı: ",i)
        sayac+=1
        print("Diğer Kişi seçme alanı hesaplanıyor...")
        time.sleep(3)
    print("-"*30)
    input("Devam etmek için ENTER tuşuna basın")

def karistir(x):
    sayac=1
    random.shuffle(x)
    for i in x:
        print(str(sayac)+"-Kullanıcı Adı: ",i)
        sayac+=1
    input("Devam etmek için ENTER tuşuna basın")
        



while True:

    print("*******ÇEKİLİŞ UYGULAMASINA HOS GELDİNİZ*******")
    secim=int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seçin\n"))

    if secim ==1:
        kullaniciEkle(kullanicilar)
    elif secim==2:
        kullaniciGör(kullanicilar)
    elif secim==3:
        karistir(kullanicilar)
    elif secim==4:
        print("Kişi seçme alanı hesaplanıyor...")
        time.sleep(2)
        KullaniciSec(kullanicilar)
    else:
        print("lütfen geçerli bir tercih yapınız.")