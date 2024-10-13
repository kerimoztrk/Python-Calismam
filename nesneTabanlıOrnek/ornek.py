class okul:
    def __init__(self, şube, öğretmen, bölüm, mevcut,maaş):
        self.şube = şube
        self.öğretmen = öğretmen
        self.bölüm = bölüm
        self.mevcut = mevcut
        self.maaş=maaş

    def bilgileri_göster(self):
        print("-" * 45)
        print("Sınıf Bilgileri")
        print("Şube:{}\nÖğretmen:{}\nBölüm:{}\nSınıf Mevcudu:{}"
              .format(self.şube, self.öğretmen, self.bölüm, self.mevcut))
        print("-" * 45)


    def brans_değiş(self):
        yeni_brans = input("Lütfen Yeni Branşınızı Yazınız:")
        print("***Eski Branş***")
        print(self.bölüm)
        self.bölüm = yeni_brans
        print("-" * 45)
        print("Sınıf Bilgileri")
        print("Şube:{}\nÖğretmen:{}\nBölüm:{}\nSınıf Mevcudu:{}"
              .format(self.şube, self.öğretmen, self.bölüm, self.mevcut))
        print("-" * 45)


    def maaş_goster(self):
        print(f"{self.öğretmen}  adlı öğretmenin maaşı {self.maaş} TL")

class müdür(okul):
    print("Yönetici Paneli")

    def __init__(self, şube, öğretmen, bölüm, mevcut,maaş, kıdem):
        super().__init__(şube, öğretmen, bölüm, mevcut, maaş)
        self.kıdem = kıdem

    def bilgileri_göster(self):
        print("≈≈≈")
        print("Yönetici Paneli")
        print("Şube: {}\nÖğretmen: {}\nBölüm: {}\nSınıf Mevcudu: {}\nKıdem: {}".format(self.şube, self.öğretmen, self.bölüm, self.mevcut, self.kıdem))
        print("≈≈≈")

    def zamYap(self):
        print(f"zam ekranına hoşgeldiniz SAYIN {self.öğretmen}")
        zam_miktarı=int(input("Lütfen Maaş mıktarını tl cinsinden giriniz:"))
        self.maaş=int(self.maaş)+int(zam_miktarı)
        print(f"{self.öğretmen}'adlı öğretmenin maaşına {zam_miktarı} tl kadar zam yapıldı")
        print(f"{self.öğretmen}'adlı öğretmenin maaşı{self.maaş}")

sinif_adi = input("Lütfen Şube Numarası giriniz:")
öğretmen = input("Lütfen İsminizi Giriniz:")
bölümAl = input("Lütfen Branşınızı Giriniz:")
mevcut = input("Sınıfı Mevcudunu giriniz:")
maasGir = input("Maaş Miktarını giriniz:")
print("---BU ALANI SADECE YÖNETİCİ İSENİZ DOLDURUNUZ---")
kıdem_al=input("lütfen kıdem seviyenizi giriniz")
if not kıdem_al:
    print("öğretmen modundasınız")

sinif_olustur = input("Sınıf Oluşturunuz:")

while True:
    if not kıdem_al:
        sinif_olustur=okul(sinif_adi,öğretmen,bölümAl,mevcut,maasGir)
        soruSor=input("1-Bilgileri Göster\n2-Maaşı göster\n3-Bransı değiştir")
        
        if soruSor=="1":
            sinif_olustur.bilgileri_göster()
            print("Devam etmek için ENTER tuşuna basın.")
        elif soruSor=="2":
            sinif_olustur.maaş_goster()
            print("Devam etmek için ENTER tuşuna basın.")
        elif soruSor=="3":
            sinif_olustur.brans_değiş()
            print("Devam etmek için ENTER tuşuna basın.")
        else:
            print ("lütfen geçerli bri seçim yap")
    else:
        sinif_olustur=müdür(sinif_adi,öğretmen,bölümAl,mevcut,maasGir,kıdem_al)
        soruSor2=input("1-Bilgileri Göster\n2-zam Yap")
        if soruSor2=="1":
            sinif_olustur.bilgileri_göster()
            print("Devam etmek için ENTER tuşuna basın.")
        elif soruSor2=="2":
            sinif_olustur.zamYap()
            print("Devam etmek için ENTER tuşuna basın.")
        else:
            print("çıkış yap")