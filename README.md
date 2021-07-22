# Arknights_birthdays_operators_search
使用scrapy框架爬取prts上的干员生日信息并保存到本地，从而可以方便的使用干员-生日双向查询功能

## 新改动
1. 增加了图形界面。
2. 通过设置并行请求数提高了爬虫速度，在网络状况良好的情况下能更快完成信息爬取。

## 可改进的地方
1. 可在middlewares处设置随机UA，使并发爬虫更容易通过