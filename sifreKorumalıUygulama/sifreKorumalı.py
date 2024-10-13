import subprocess as sp

psw="123456"
kullanıcıSifresi=input("Lütfen Şifrenizi Giriniz:")

if kullanıcıSifresi==psw:
      

    while True:
            print("*** UYGULAMA AÇMA EKRANINA HOŞGELDİNİZ ***")
            secimYap=input("1-Notepat\n2-Word\n3-Google\n4-Hesap Makinesi\n")
           

            if secimYap=="1":
        
                sp.call("notepad.exe")
                input("Devam edilsin mi?")
            elif secimYap=="2":
                sp.call("C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE")
                input("Devam edilsin mi?")
            elif secimYap=="3":
                sp.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
                input("Devam edilsin mi?")
            elif secimYap=="4":
                sp.call("calc.exe")
                input("Devam edilsin mi?")
else:print("hatalı sifre!")
