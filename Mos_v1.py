import requests
from bs4 import BeautifulSoup
import time
import csv

store_name = []
store_address = []
store_tel = []

for i in range(0, 14):
	base_url = "http://www.mos.com.tw/shop/search.aspx?area=_&page="+str(i)+"&f="
	res = requests.get(base_url, timeout=5)
	html = res.text

	soup = BeautifulSoup(html.replace("\n", "").strip(), "html.parser")

	items = soup.find("ul", class_="shopList")


	data_name = items.find_all("h1")
	for data in data_name:
		store_name.append(data.text)
		print(store_name)

	data_address = items.find_all("p", class_="address")
	for data in data_address:
		store_address.append(data.text)
		print(store_address)

	data_tel =items.find_all("p", class_="tel")
	for data in data_tel:
		store_tel.append(data.text)
		print(store_tel)

with open('shop_list_mos.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址', '門市電話']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        newrow.append(store_tel[n])
        csvwriter.writerow(newrow)

	




