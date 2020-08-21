import scrapy
from ..items import MobileItem

class MobSpider(scrapy.Spider):
    name = 'mob'
    page_num = 2
    start_urls = ['https://www.flipkart.com/mobiles/android~os/pr?sid=tyy%2C4io&page=1']

    def parse(self, response):
        items = MobileItem()
        all_mobiles = response.css('._1UoZlX')
        for h in all_mobiles:
            name = (h.css('._3wU53n::text').extract())
            memory=(h.css('.tVe95H:nth-child(1)::text').extract())
            display=(h.css('.tVe95H:nth-child(2)::text').extract())
            camera=(h.css('.tVe95H:nth-child(3)::text').extract())
            battery=(h.css('.tVe95H:nth-child(4)::text').extract())
            processor = (h.css('.tVe95H:nth-child(5)::text').extract())
            warranty = (h.css('.tVe95H:nth-child(6)::text').extract())
            rating=(h.css('.hGSR34::text').extract())
            review=(h.css('._1VpSqZ+ span::text').extract())
            reviews=[a.replace('\xa0','') for a in review]
            prices=(h.css('._2rQ-NK::text').extract())
            price1=[p.replace('₹','') for p in prices]
            price=[p1.replace(',','') for p1 in price1]
            items['name']=name
            items['memory'] = memory
            items['display'] = display
            items['camera'] = camera
            items['battery'] = battery
            items['processor'] = processor
            items['warranty'] = warranty
            items['rating'] = rating
            items['reviews'] = reviews
            items['price'] = price
            yield items

        next_page = 'https://www.flipkart.com/mobiles/android~os/pr?sid=tyy%2C4io&page=' + str(MobSpider.page_num) + ''
        if (MobSpider.page_num <= 215):
            MobSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)

