# Scrapy
```
Scrapinghub 테스트를 위한 프로젝트
```

## Install

### install Scrapy 
```
pip install Scrapy
scrapy startproject tutorial
```

### Deploy
```
pip install shub
shub login
> Enter Your Key
shub deploy 
> Enter Your Project ID
```

## Etc
```
scrapy genspider quote toscrape.com

scrapy shell <fetchUrl>
> print(response.text)
> response.css(<CSS Selector>)[]
> ::attr, ::text
> extract(), extract_first()

scrapy runspider quotes.py -o items.json
scrapy crawl quote
```

* [Scrapinghub](https://scrapinghub.com/) - Turn websites into data