# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/'
    #         # 'http://quotes.toscrape.com/page/2/'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.psrse)

    def parse(self, response):
        self.log('visited: ' + response.url)

        for quote in response.css('div.quote'):
            item = {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            yield item

        next_page = response.css('li.next a::attr(href)').extract_first()
        # next_page = response.urljoin(next_page)
        # yield scrapy.Request(url=next_page, callback=self.parse)
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        # details view
        # urls = response.css('div.quote > span > a::attr(href)').extract()
        # for url in urls:
        #     url = response.urljoin(url)
        #     yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'name': response.css('h3.author-title::text').extract_first(),
            'birth_datte': response.css('span.author-born-date::text').extract_first(),
        }

        # file write
        # page = response.url.split('/')[-2]
        # filename = 'shop-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
