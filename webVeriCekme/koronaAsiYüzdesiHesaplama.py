import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "aa"
}

# URL'ye GET isteği gönder
response = requests.get("https://covid19.saglik.gov.tr/", headers=headers)

# Durum kodunu yazdır
print(response.status_code)

# Durum kodunu kontrol ederek 200 olup olmadığını kontrol edin
if response.status_code == 200:
    print("İstek başarılı!")
else:
    print(f"İstek başarısız oldu, durum kodu: {response.status_code}")


soup = BeautifulSoup(response.content, 'html.parser')

yazdir = soup.find_all("div",{"class":"svg-turkiye-haritasi-tamamlanan"})



print("EN AZ İKİ DOZ AŞI OLMUŞ 18 YAŞ VE ÜSTÜ NÜFUS (%)")
while True:
    
    for i in yazdir:
        print("-"*10)
        print(i.text)
    input("devam etsin mi?")


