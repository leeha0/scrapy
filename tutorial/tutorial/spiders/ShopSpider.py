import scrapy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # CRITICAL, ERROR, WARNING, INFO, DEBUG


class ShopSpider(scrapy.Spider):
    name = 'shop'

    def __init__(self, *args, **kwargs):
        logger.info('__init__ Spider')
        logger.info(kwargs)

        # Require : query
        if 'query' not in kwargs:
            raise KeyError('\"query\" Argument Empty.')

        try:
            self.query = str(kwargs['query'])
        except Exception:
            raise TypeError('\"query\" must be String.')

        # Input Base Url
        self.baseUrl = ''
        self.maxDocumentCount = 10000
        self.params = {
            'origQuery': self.query,
            'pagingIndex': 1,
            'pagingSize': 80,
            'viewType': 'list',
            'sort': 'rel',
            'frm': 'NVSHATC',
            'query': self.query,
        }

        # Optional : page, to
        if 'page' in kwargs:
            try:
                self.params['pagingIndex'] = int(kwargs['page'])
            except Exception:
                raise TypeError('\"page\" must be Integer.')

        if 'maxDocumentCount' in kwargs:
            try:
                self.maxDocumentCount = int(kwargs['maxDocumentCount'])
            except Exception:
                raise TypeError('\"maxDocumentCount\" must be Integer.')

    def start_requests(self):
        requestUrl = self.baseUrl + '?' + (''.join(['%s=%s&' % (key, value) for (key, value) in self.params.items()]))
        logger.info('Crawling Start.')

        yield scrapy.Request(url=requestUrl, callback=self.parse)

    def parse(self, response):
        logger.info('Parse %s' % response.url)
        self.maxDocumentCount -= self.params['pagingSize']
        for product in response.css('ul.goods_list > li._itemSection'):
            yield {
                'data-mall-txt': product.css('p.mall_txt > a.btn_detail::attr(data-mall-name)').extract_first(),
                'data-mall-seq': product.css('::attr(data-mall-seq)').extract_first(),
                'data-expose-id': product.css('::attr(data-expose-id)').extract_first(),
                'data-expose-rank': product.css('::attr(data-expose-rank)').extract_first(),
            }

        # Check Has Next Page
        has_next = response.css('div.co_paginate > a.next').extract_first()

        if has_next:
            if self.maxDocumentCount < 0:
                logger.info('Crawling Done.')
            else:
                # Add PagingIndex
                self.params['pagingIndex'] = self.params['pagingIndex'] + 1
                nextUrl = self.baseUrl + '?' + (
                    ''.join(['%s=%s&' % (key, value) for (key, value) in self.params.items()]))
                yield scrapy.Request(url=nextUrl, callback=self.parse)
        else:
            logger.info('Crawling Done.')
