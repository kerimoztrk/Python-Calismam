import sqlite3

db=sqlite3.connect("veresiye.db")

yetki=db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS kisiler(isim,borc)")


while True:
    print("********VERESİYE DEFTERİNE HOŞGELDİNİZ***********")
    sor=input("1-BORÇLU EKLE \n2-BORÇLULARI GÖR\nGirdi: ")

    if sor=="1":
        borcluİsim=input("Lütfen Borçluların ismini giriniz")
        borcMiktarı=input("Lütfen Borç Miktarını giriniz:")
        yetki.execute(f"INSERT INTO kisiler VALUES('{borcluİsim}','{borcMiktarı}')")
        db.commit()
        print(f"İşlem tamamlandı,Borçlu kişinin adı: {borcluİsim}")

    elif sor=="2":
        yetki.execute("SELECT * FROM kisiler")
        yazdır=yetki.fetchall()
        say=1
        for i in yazdır:
            print("-----------Borçlu bilgisi-----------")
            print(f"{say}Borçlunun ismi:{i[0]}\nBorçlu olduğu miktar:{i[1]}\n")
            say+=1
        input("Devam edilsin mi?")