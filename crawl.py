from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import time
import json
from pprint import pprint
from bs4 import UnicodeDammit
from random import randint
import codecs
import requests
import os

f = open('web.txt','w')
json1 = []
shop_links=[]

url = 'http://www.ipeen.com.tw/taiwan/channel/F'
headers = {}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
page = response.read()

soup = BeautifulSoup(page,'html5lib')
#get category
categories = soup.select('.head a')
# print(categories)
#get small cate
# restaurants = soup.select('td.detail ul li a')
# for i in categories[0:8]:
#     print(i.string)
# for i in range(20):
#     x = restaurants[i].select('li a')
#     print (x[0]['href'])
# temp = restaurants[0].select('li a')
# #EX:/search/taiwan/000/1-0-27-27
# #print (temp[0]['href'])
# links = 'http://www.ipeen.com.tw' + temp[0]['href']
# print (links)
for category in categories[0:1]:
    category_name = category.string
    for num in range(0,2):
        links = 'http://www.ipeen.com.tw' + category['href'] + '?=' + str(num)
        res = requests.get(links)
        soup_search = BeautifulSoup(res.text.encode('utf-8'),'html5lib')
        shop_table = soup_search.select('article.serItem div h3 a')
        for i in shop_table:
            if "www" not in str(i['href']):
                link = 'http://www.ipeen.com.tw' + (i['href'])
                shop_links.append(link)
                # print(shop_links)
        for web in shop_links:
            meal_list = []
            store_page = requests.get(web)
            soup_store = BeautifulSoup(store_page.text.encode('utf-8'),'html5lib')
            meals = soup_store.select('div.recommend ul li')

            for meal in meals:
                meal_list.append(meal.string[:meal.string.find('(')])
            # print (meal_list)
            try:
                restaurant_name = soup_store.find('span',{'itemprop':'name'}).string
            except Exception as e:
                restaurant_name = " "
            try:
                tel = soup_store.find('p',{'class':'tel i'}).a.string
            except Exception as e:
                tel = " "
            try:
                addr = soup_store.find('p',{'class':'addr i'}).a.string
            except Exception as e:
                addr = " "
            try:
                hours = soup_store.find('div',{'class':'hours'}).p.string
            except Exception as e:
                hours = " "
            print (restaurant_name,tel,addr,hours,category_name)
    # print (restaurant_name + "," + tel + "," + addr + "," + hours)
    # json1.append({'restaurant_name':soup_store.find('span',{'itemprop':'name'}).string,'category':categories[0],'tel':soup_store.find('p',{'class':'tel i'}).string,'address':soup_store.find('p',{'class':'addr i'}).string,'hours':soup_store.find('div',{'class':'hours'}).p.string})

"""for category in len(categories):
    for restaurant in len(restaurants):
        print (restaurants[restautant]['href'])"""
"""for web in len(soup.select('td.detail')):
    print"""
