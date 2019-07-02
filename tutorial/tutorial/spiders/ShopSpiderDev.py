import scrapy


class ShopSpider(scrapy.Spider):
    name = 'shop-dev'

    # origQuery : 검색어
    # pagingIndex : 페이지
    # pagingSize : 출력 결과 수
    # viewType : 보기 옵션
    # sort : 정렬
    # query : 검색어

    def __init__(self):
        self.maxDocumentCount = 10000
        # Input Base Url
        self.baseUrl = ''
        self.params = {
            'origQuery': '',
            'pagingIndex': 1,
            'pagingSize': 80,
            'viewType': 'list',
            'sort': 'rel',
            'frm': 'NVSHATC',
            'query': '',
        }

    def start_requests(self):
        requestUrl = self.baseUrl + '?' + (''.join(['%s=%s&' % (key, value) for (key, value) in self.params.items()]))
        print('RequestUrl %s' % requestUrl)

        yield scrapy.Request(url=requestUrl, callback=self.parse)

    def parse(self, response):
        print('Parse %s' % response.url)
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
        print(has_next)

        # Add PagingIndex
        self.params['pagingIndex'] = 2
        nextUrl = self.baseUrl + '?' + (''.join(['%s=%s&' % (key, value) for (key, value) in self.params.items()]))
        yield scrapy.Request(nextUrl, callback=self.parseDev)

    def parseDev(self, response):
        print('Parse %s' % response.url)
        self.maxDocumentCount -= self.params['pagingSize']
        for product in response.css('ul.goods_list > li._itemSection'):
            yield {
                'data-mall-txt': product.css('p.mall_txt > a.btn_detail::attr(data-mall-name)').extract_first(),
                'data-mall-seq': product.css('::attr(data-mall-seq)').extract_first(),
                'data-expose-id': product.css('::attr(data-expose-id)').extract_first(),
                'data-expose-rank': product.css('::attr(data-expose-rank)').extract_first(),
            }