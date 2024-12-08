import matplotlib.pyplot as plt
import requests

from bs4 import BeautifulSoup

url = "https://www.aviasales.ru/search/KZN1801DXB1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

html_content = response.text  # HTML-код страницы
soup = BeautifulSoup(html_content, 'html.parser')
l = soup.find("div")
print(l)
x = []
y = []
plt.xlabel("дата")
plt.ylabel()
plt.title()
plt.plot(x,y, "--b",  color = "green", marker = "o", markersize = 7)
plt.legend()
plt.show()

