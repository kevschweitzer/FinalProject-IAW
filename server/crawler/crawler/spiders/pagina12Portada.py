import scrapy
from crawler.items import Pagina12NoticiaItem
from crawler.items import Pagina12PortadaItem
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
    name = 'pagina12Portada'
    start_urls = ['http://www.pagina12.com.ar/']


    def parse(self, response):
        #Creo el item
        item = Pagina12PortadaItem()


        #Obtengo todos los headline
        headlines = response.xpath("//div[@class='article-title']")
        print headlines
        for h in headlines:
            item['titulo'] = h.select("a/text()").extract()
            item['url'] = h.xpath("a/@href").extract()
            print item['titulo'],item['url']
            #Paso las listas a string
            textoTitulo = ""
            textoUrl = ""
            if item['titulo']:
                textoTitulo += ''.join(item['titulo'])
                textoUrl += ''.join(item['url'])
                item['titulo'] = textoTitulo
                item['url'] = textoUrl

            #Filto por categoria politica o economia, el resto no me interesan
            #if (textoUrl.startswith("/politica")) or (textoUrl.startswith("/economia")):


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
