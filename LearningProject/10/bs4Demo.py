from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
from reqDemo import search_Douban

def jd_search_parse(html):
    soup=BeautifulSoup(html,'lxml')
    item=soup.select("a[href^='/search']")
    for i in item:
        print(i.parent)
    #print(unquote("%E4%BD%A0%E5%A5%BD%E6%9D%8E%E7%84%95%E8%8B%B1"))


if __name__=="__main__":
    html=search_Douban("你好李焕英").text
    jd_search_parse(html)