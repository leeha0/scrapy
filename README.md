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
scrapy shell <fetchUrl>
> print(response.text)
> response.css(<CSS Selector>)[]
> ::attr, ::text
> extract(), extract_first()
```

* [Scrapinghub](https://scrapinghub.com/) - Turn websites into data