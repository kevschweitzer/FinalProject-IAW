import scrapy
from crawler.items import TelamNoticiaItem
from crawler.items import TelamPortadaItem
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
    name = 'telamPortada'
    start_urls = ['http://www.telam.com.ar/politica','http://www.telam.com.ar/economia']


    def parse(self, response):

        #Creo el item
        item = TelamPortadaItem()

        #Obtengo todos los headline
        headlines = response.xpath('//div[@class="highlighted clearfix"]')
        for h in headlines:
            item['titulo'] = h.select("a/h2/text()").extract()
            item['url'] = h.xpath("a/@href").extract()

            #Paso las listas a string
            textoTitulo = ""
            textoUrl = ""
            if item['titulo']:
                textoTitulo += ''.join(item['titulo'])
                textoUrl += ''.join(item['url'])
                item['titulo'] = textoTitulo
                item['url'] = textoUrl
                yield item

            #Filto por categoria politica o economia, el resto no me interesan
            #if (textoUrl.startswith("/politica")) or (textoUrl.startswith("/economia")):
