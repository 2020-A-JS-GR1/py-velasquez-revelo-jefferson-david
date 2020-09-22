import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        print(titulos)

# scrapy crawl nombre_arania
# Buscar el precio, url de imagen, si está en stock y opcional el número de estrellas

