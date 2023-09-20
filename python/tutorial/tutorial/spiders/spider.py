import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["kennesaw.edu"]
    start_urls = ["https://kennesaw.edu"]

    def parse(self, response):
        pass
