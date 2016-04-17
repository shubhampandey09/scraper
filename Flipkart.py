import scrapy


class Flipkart(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ('http://www.flipkart.com/mobiles/pr?p%5B%5D=sort%3Dpopularity&sid=tyy%2C4io&filterNone=true&q=mobile')
    def parse(self, response):
        urls = response.xpath('//div[@class="pu-title fk-font-13"]/a/@href').extract()
        print urls
        for url in urls:
            absolute_url = response.urljoin(url)
            request = scrapy.Request(absolute_url, callback=self.parse_mobile)
            yield request


        next_page_url = response.xpath('//a[text()="Next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        request = scrapy.Request(absolute_next_page_url)
        yield request

    def parse_mobile(self, response):
        review = response.xpath('//p[@class="review-title"]').extract()
        url = response.url
        product = {'Review': review, 'Url': url}
        yield product


