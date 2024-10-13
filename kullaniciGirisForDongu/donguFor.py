for i in range(3):

    sifre = input("Lütfen bir şifre belirleyiniz: ")

    if not sifre:
        print("Bu alan boş bırakılamaz...!")
    elif len(sifre) in range(3,8):
        print("yeni sifreniz",sifre)
        break
    elif i==2:
        print("3 kere yanlış girdiniz Lütfen 15 dk bekleyiniz.")
    else:
        print("Sifreniz 3 ile 8 karakter arasıdna değil")