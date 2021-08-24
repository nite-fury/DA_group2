import scrapy


class QuotesSpider(scrapy.Spider):
    name = "photo"

    def start_requests(self):
        urls = [
            'http://172.18.58.238/index.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


def parse(self, response):
    raw_image_url = response.css('.image img ::atr(src)').getall()
    clean_image_urls = []
    for img_url in raw_image_url:
        clean_image_urls.appendresponse.urljoin(img_url)

    # clean_image urls as LIST

    yield {
        'image_urls': clean_image_urls
    }
