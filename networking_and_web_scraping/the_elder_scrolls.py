from bs4 import BeautifulSoup
import requests

response = requests.get('https://account.elderscrollsonline.com/store?_ga='
                        '2.55761772.613162147.1607856548-953723473.1604326764')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html5lib")

product_list = {}

for tag in soup.find_all('span', {'class': 'product-info'}):
    for span in tag.descendants:
        if span.name is not None:
            if span['class'][0] == 'product-title':
                product = span.text
            if span['class'][0] == 'product-price':
                price = span.text
            else:
                price = 'No price'
    product_list[product] = price
print(product_list)

