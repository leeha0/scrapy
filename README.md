# Scrapy-Test
```
Scrapinghub 테스트를 위한 프로젝트
```

* [Scrapinghub](https://scrapinghub.com/) - Turn websites into data

## Getting Started

### Prerequisites 
Python 2.7 or Python3.4

### Installing
* Install Scrapy Lib
```
pip install Scrapy
```
* Create Tutorial Project
```
scrapy startproject tutorial
```

## Deploy
### Installing
* Install shub Lib
```
pip install shub
```
* Setting 
```
shub login
> Enter Your Key
```
* Deploy
```
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