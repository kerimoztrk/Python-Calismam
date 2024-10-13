telRehberi=dict()

def telNoEkle(x):
    print("***NUMARA EKLEME EKRANINA HOŞGELDİNİZ****")
    numaraİsimAl=input("Lütfen kayıt edilecek kişinin adını yazınız : ")
    numraNoAl=input("Lütfen Telefon Numarasını Giriniz:")

    x=telRehberi.setdefault(numaraİsimAl,numraNoAl)
    print(f"{numaraİsimAl} adlı kişi rehberinize eklendi...")
    input("devam edilsin mi?")


def telRehberGöster(x):
    print("Rehbere hoşgeldiniz. ")
    kisiSayisi=len(x)
    print(f"Rehberinizdeki kayıtlı kişi sayısı= {kisiSayisi}")

    for isim,deger in x.items():
        print(isim,":",deger)
    input("devam edilsin mi?")

def numaraSil(x):
    print("Kişi silme ekranına hoşgeldiniz.")
    silinecekKisi=input("Silinecek Kişiyi giriniz.")
    x=telRehberi.pop(silinecekKisi)

while True:
    print("*****Hoşgeldiniz*****")
    print("****Seçim yapınız****")
    secimYap=int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n"))

    if secimYap==1:
        telNoEkle(telRehberi)
    elif secimYap==2:
        numaraSil(telRehberi)
    elif secimYap==3:
        telRehberGöster(telRehberi)
    else:
        print("lütfen uygun tuşlara basınız")