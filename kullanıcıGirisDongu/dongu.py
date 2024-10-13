dbKullaniciAdi="admin"
dbParola=1234

while True:

    kullaniciAdi=input("Lütfen Kullanıcı adını giriniz:")
    kullaniciParola=int(input("Lütfen Sifrenizi Giriniz: "))


    if dbKullaniciAdi==kullaniciAdi and dbParola== kullaniciParola:
        print("hoşgeldiniz: ", kullaniciAdi)
        break
    elif dbKullaniciAdi != kullaniciAdi and dbParola == kullaniciParola:
        print("kullanıcı adınız yanlış")
    elif dbKullaniciAdi == kullaniciAdi and dbParola != kullaniciParola:
        print("Şifreniz Hatalı !")
        print("Şifre değiştirilsin mi ? : E/H")
        cevap=input()
        if cevap == "E":
            print("Şifreniz Değiştiriliyor....")
            yeniSifre = int(input("sayısal şekilde yeni şifrenizi giriniz."))
            dbParola = yeniSifre

    else:
        print("kullanici adi ve şifresi hatalı")