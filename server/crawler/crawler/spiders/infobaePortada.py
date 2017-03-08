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


#Obtengo los titulos y url de cada noticia de la portada de infobae.
#Las noticias que guardo en la bd es solo las de economia y politica
class InfobaePortadaSpider(BaseSpider):
    name = 'infobaePortada'
    start_urls = ['http://www.infobae.com/']


    def parse(self, response):
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
