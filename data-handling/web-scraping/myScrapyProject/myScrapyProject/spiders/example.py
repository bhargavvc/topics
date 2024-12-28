import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
    
    
    
# to run this command "scrapy crawl new_spider -o output.json"