import scrapy
from bs4 import BeautifulSoup
from scrapy_11.items import Scrapy11Item


class douban(scrapy.Spider):
    name = "douban"

    def start_requests(self):

        for keyword in  ['你好李焕英','夏洛特烦恼','羞羞的铁拳']:
            url= f"https://www.douban.com/search?q={keyword}"

            yield scrapy.FormRequest(
                url=url,
                method="GET",
                callback=self.parse_search)

    def parse_search(self, response, **kwargs):
        print(response)
        #xpath返回的是选择器列表
        #response.xpath("//div[@class='search-result']")
        #response.xpath("./h1/text()").extract_first()
        soup = BeautifulSoup(response.text.replace("\n", ""), "lxml")
        search_result = soup.select("div[class='search-result']")[0]
        heads = soup.select("div[class='search-result']>h2")
        contents = search_result.select("div[class='result-list']")
        # print(len(heads))
        for i in range(0, len(heads)):
            h = heads[i]
            # print("--------------------------------------")
            # print(i,h.text.strip().replace(":",""))
            content_list = contents[i].select("div[class='result']")
            # print(i,contents[i])
            for content in content_list:
                title_area = content.select("div[class='title']")[0]
                type = title_area.select("h3 span:first-child")
                name = title_area.h3.a
                rate = title_area.select("div[class='rating-info']")
                text_area = content.p

                item = Scrapy11Item()

                item["type"] = type[0].text if type else ""
                item["name"] = name.text if name else ""
                item["rate"] = str([i.text for i in rate[0].select("span")] if rate else [])  # 列表推导式
                item["text_area"] = text_area.text if text_area else ""
                #print(item)
                yield item
