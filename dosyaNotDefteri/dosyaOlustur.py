import codecs

while True:

            dosyaOlustur=input("Oluşturmak istediğiniz dosyanın adını giriniz. ")

            yeniDosya=dosyaOlustur+".txt"

            veriGir=input(f"Lütfen {yeniDosya} dosyasına veri ekleyin: ")

            with codecs.open(yeniDosya,"w", encoding="utf-8") as dosya:

                dosya.write(veriGir)
                soruSor=input("Dosya üzerine ekleme yapmak ister msiniz?  E/H :").lower()
                if soruSor=="e":
                    open(yeniDosya,"a")
                    yeniVeri=input("Lütfen eklemek istediğiniz veriyi yazınız. :")
                    yeniVeri="\n"+ yeniVeri
                    dosya.write(yeniVeri)
                    print("veriler güncellendi.... ")
                    print(yeniDosya)
                else:print("çıkış yapıldı.")
            print("Veri tabanındaki belgeler")
            info=open(yeniDosya,"r",encoding="utf-8")
            a=info.read()
            print(f"{yeniDosya}'dosyasındaki byte uzunluğu : {len(yeniDosya)}' tır.")
            print(a)
            print("Veri tabanındaki belgeler")

