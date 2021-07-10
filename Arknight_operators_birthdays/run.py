from scrapy import cmdline

cmdline.execute("scrapy crawl Ark -o ark.json -t json".split())