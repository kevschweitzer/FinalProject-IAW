import scrapy
from crawler.items import InfobaeNoticiaItem
from crawler.items import InfobaePortadaItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from pymongo import MongoClient
from scrapy.http.request import Request
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging












"""


class TelamSpider(scrapy.Spider):
    name = 'Telam'
    start_urls = ['http://www.telam.com.ar/notas/201703/181480-agremiados-habia-advertido-a-la-afa-en-diciembre-sobre-la-situacion-decante-de-los-clubes.html']

    def parse(self, response):

        #Estoy obteniendo el titulo del articulo
        title = response.xpath('//h2/text()')[0].extract()
        print title

        #En Telam, los parrafos con el texto estan bajo la class = editable-content
        #Obtengo el contenido. Esta todo junto, gracias Telam :)
        contenido = response.xpath('//div[@class="editable-content clearfix"]')
        #Notar el uso de ./text() EL PUNTO, esto me permite tomar el texto DENTRO del div.
        parrafo = contenido.xpath('./text()').extract()
        if parrafo:
            print ''.join(parrafo)




class Pagina12Spider(scrapy.Spider):
    name = 'Pagina12'
    start_urls = ['https://www.pagina12.com.ar/23841-camino-a-un-paro-masivo']

    def parse(self, response):

        #Estoy obteniendo el titulo del articulo
        title = response.xpath('//div[@class="article-title"]/text()')[0].extract()
        print title

        #En Telam, los parrafos con el texto estan bajo la class = editable-content
        #Obtengo el contenido. Esta todo junto, gracias Telam :)
        contenido = response.xpath('//div[@class="article-text"]')
        #Notar el uso de ./text() EL PUNTO, esto me permite tomar el texto DENTRO del div.
        parrafos = contenido.xpath('./p')
        for p in parrafos:
            texto = p.xpath("./text()").extract()
            if texto:
                print ''.join(texto)


class InfobaePortadaSpider(BaseSpider):
    name = 'infobaePortada'
    start_urls = ['http://www.infobae.com/']

    #Creo el item
    item = InfobaePortadaItem()


    #Obtengo todos los headline
    headlines = response.xpath("//*[contains(concat(' ', normalize-space(@class), ' '), ' headline ')]")
    for h in headlines:
        item['titulo'] = h.select("a/text()").extract()
        item['url'] = h.xpath("a/@href").extract()

        #Paso las listas a string
        textoTitulo = ""
        textoUrl = ""
        if item['titulo']:
            textoTitulo += ''.join(item['titulo'])
            textoUrl += ''.join(item['url'])
            item['titulo'] = textoTitulo
            item['url'] = textoUrl
        #Filto por categoria politica o economia, el resto no me interesan
        if (textoUrl.startswith("/politica")) or (textoUrl.startswith("/economia")):
            yield item
"""
