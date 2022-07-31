from bs4 import BeautifulSoup
import json

def parse_douban_result(html):
    result=[]
    soup=BeautifulSoup(html.replace("\n",""),"lxml")
    search_result=soup.select("div[class='search-result']")[0]
    heads = soup.select("div[class='search-result']>h2")
    contents = search_result.select("div[class='result-list']")
    #print(len(heads))
    for i in range(0,len(heads)):
        h=heads[i]
        #print("--------------------------------------")
        #print(i,h.text.strip().replace(":",""))
        content_list=contents[i].select("div[class='result']")
        #print(i,contents[i])
        for content in content_list:
            title_area=content.select("div[class='title']")[0]
            type = title_area.select("h3 span:first-child")
            name = title_area.h3.a
            rate = title_area.select("div[class='rating-info']")
            text_area=content.p

            type=type[0].text if type else ""
            name = name.text if name else ""
            rate = str([i.text for i in rate[0].select("span")] if rate else [])#列表推导式
            text_area = text_area.text if text_area else ""

            result.append((type,name,rate,text_area))

    return result







if __name__=="__main__":
    with open("search.html","r",encoding="utf-8") as f:
        res=parse_douban_result(f.read())
        print(res)
        print(len(res))