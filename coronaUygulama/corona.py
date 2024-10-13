ates_durumu= float((input("Lütfen ateş durumunuzu girin")))
öksürük=input("Öksürüğünüz var mı? E/H:").lower()
basAgrısı=input("Baş ağrınız varmı ? E/H:").lower()
gün=int(input("Şikayetleriniz kaç gündür var?"))

if ates_durumu>=39:
    if gün>=3:
        print("****Uyarı Hastaneye gidiniz")
    else:
        print("Ateş durumu sınırda,Decam ederse lütfen en yakın sağlık kurmuna gidiniz..")

if (ates_durumu>=39) and (öksürük=="e") and (basAgrısı=="e") and (gün>=3):
    print("******ACİL Lütfen en yakın sağlık kurulusuna gidiniz..")
    print("******ACİLLLLL")

elif (ates_durumu<39) and (öksürük=="e") and (basAgrısı=="e") and (gün>=3):
    print("***Durumunuz bu şekilde devam ederse lütfen sağlık kurumuna gidiniz")

else :
    print("Ateş durumunuz 39 derecenin üstüne çıkarsa lütfen sağlık kurumuna gidiniz")
    print(f"Ateşiniz:{ates_durumu}")