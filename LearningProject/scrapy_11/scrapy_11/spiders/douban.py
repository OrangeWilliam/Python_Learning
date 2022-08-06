import scrapy

class douban(scrapy.Spider):
    name="douban"

    def start_requests(self):
        for keyword in  ['你好李焕英','夏洛特烦恼','羞羞的铁拳']:
            url= f"https://www.douban.com/search?q={keyword}"
            yield scrapy.FormRequest(
                url=url,
                method="GET",
                callback=self.parse_search)

    def parse_search(self, response, **kwargs):
        print(response)