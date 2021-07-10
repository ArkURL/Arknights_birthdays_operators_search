import scrapy
from Arknight_operators_birthdays.items import ArkItem

class ArkSpider(scrapy.Spider):
    name = "Ark"

    allowed_domains = ["prts.wiki"]     #prts域名，须填入一个正确的域名才能有效限制爬取范围

    start_urls = ["http://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88"]    #一级页面

    def parse(self,response):
        #获得干员名
        operators_name = response.xpath("//div[@class='smwdata']/@data-cn").extract()
        for opts in operators_name:
            next_url ='http://prts.wiki/w/'+opts #二级页面url名
            print(next_url)
            yield scrapy.Request(url=next_url,callback=self.parse_item)


    def parse_item(self,response):
        data = response.xpath("//tr/td/div[@class='poem']/p/text()")
        #使用非捕获组获取普通干员的生日及机械干员们的出厂日
        birthday = data.re(r"(?:【生日】|【出厂日】)[ ]?(\w*)")
        #获取干员名，以便在后续加入到item
        name = response.xpath('//div[@class="charname anicss"]/text()').extract()
        #创建item对象
        item = ArkItem()
        #获取到的是一个列表，只需要提取出其中的第一个元素
        item['name'] = name[0]
        #生日或出厂日同理
        item['birthday'] = birthday[0]
        yield item
        print(item)