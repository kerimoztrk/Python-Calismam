import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "aa"
}
response = requests.get("https://www.carrefoursa.com/sivi-yaglar/c/1111", headers=headers)

print(response.status_code)

if response.status_code == 200:
    print("İstek başarılı!")
else:
    print(f"İstek başarısız oldu, durum kodu: {response.status_code}")


soup = BeautifulSoup(response.content,'html.parser')
for i in soup.find("ul", {"class": "product-listing product-grid container-fluid add_to_cart"}).find_all("li",{"class":"product-listing-item"}):
    baslikAl=i.find("span",{"class":"item-name"}).text
    fiyatAl=i.find("span",{"class":"item-price js-variant-discounted-price"}).text
    ürünLinkAl=i.find("a").get("href")
    print(f"Ürün Adı:{baslikAl}\nFiyat:{fiyatAl}\nÜrün Linki: carrefoursa.com{ürünLinkAl}\n")
    print("-"*50)

