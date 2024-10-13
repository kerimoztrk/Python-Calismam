def su_hesapla(kilo):
    e_hesapla=kilo*0.04
    k_hesapla=kilo*0.03

    cinsiyet=input("Lütfen cinsiyetinizi giriniz : Kadın/Erkek    :").lower()

    if cinsiyet =="erkek":
        print("-"*30)
        print("Cinsiyetiniz: ",cinsiyet)
        print(e_hesapla,"Litre Su içmelisiniz.")
        print("-"*30)
    elif not cinsiyet:
        print("lütfen cinsiyetinizi belirtin")
    
    elif cinsiyet=="kadın":
        print("-"*30)
        print("Cinsiyetiniz: ",cinsiyet)
        print(k_hesapla,"Litre Su içmelisiniz...")
        print("-"*30)
 

kilo_al = int(input("lütfen kilonuzu giriniz:"))

su_hesapla(kilo_al)