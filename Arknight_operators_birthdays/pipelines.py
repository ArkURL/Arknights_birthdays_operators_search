# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class ArknightOperatorsBirthdaysPipeline:
    #   自己创建的方法
    def __init__(self):
        self.file = open('../arknights.json', 'wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    #   自己创建的方法，启动spider时调用
    def open_spider(self, spider):
        print("spider启动")

    #  默认生成的方法，用于处理信息
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    #   自己创建的方法，关闭spider时调用
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print("spider调用结束")