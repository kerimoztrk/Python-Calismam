

vize_notu=int(input("vize Notunu Giriniz: "))


final_notu=int(input("final Notunu Giriniz: "))

ortalamaAl=(final_notu+vize_notu)/2

if ortalamaAl>85:
    print("Tebrikler AA aldınız",ortalamaAl)
elif ortalamaAl>=65:
    print("Tebrikler BB aldınız: ")
elif ortalamaAl>=50:
    print("Tebrikler cc aldınız: ")
else:
    print("Malesef Ders tekrarı: ",ortalamaAl)