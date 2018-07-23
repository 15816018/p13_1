from django.shortcuts import render
import requests
import bs4
import re
import random

#http://127.0.0.1:8000/sekaiisan/

def appmain(request):
    img = None
    init_url = 'http://whc.unesco.org'
    while img == None:
        id = random.randrange(3000)
        res = requests.get('http://whc.unesco.org/en/list/'+str(id)+'/')
        soup = bs4.BeautifulSoup(res.text,"lxml")
        img = soup.find('img',class_='unveil')
    print(img)

    exp = soup.find('p').getText() #概要文を取得
    title = soup.find('h6').getText() #名称を取得
    imgSrc = init_url + img['data-src'] #画像ソースを取得
    search_url = 'https://www.bing.com/images/search?q='+ title.replace(' ','+') #画像検索URL

    return render(request, 'demo/sekaiisan.html', {'name': title, 'detail': exp, 'image': imgSrc, 'bing_search': search_url})
