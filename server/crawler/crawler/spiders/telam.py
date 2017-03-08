import scrapy
from crawler.items import TelamNoticiaItem
from crawler.items import InfobaePortadaItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from pymongo import MongoClient
from scrapy.http.request import Request
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import repustate



class TelamSpider(scrapy.Spider):
    name = 'telam'
    start_urls = []


    #Me conecto a la base de datos y obtengo las urls de las noticias de portada de infobae
    def __init__(self):
        self.db = MongoClient() #localhost por defecto
        self.urls = self.db.proyectofinal.telamportadaitem.find({},{"_id": 0, "titulo": 0}) #use appropriate finding criteria here according to the structure of data resides in that collection

    #El start_urls se va a completar con las urls obtenidas desde la base de datos
    def start_requests(self):
        for url in self.urls:
            texto ="http://www.telam.com.ar"
            texto += ''.join(url["url"])
            yield Request(texto, self.parse)


    def parse(self, response):

        #Creo el item
        item = TelamNoticiaItem()

        #Estoy obteniendo el titulo del articulo
        item['titulo'] = response.xpath('//h2/text()')[0].extract()

        #En Telam, los parrafos con el texto estan bajo la class = editable-content
        #Obtengo el contenido. Esta todo junto, gracias Telam :)
        contenido = response.xpath('//div[@class="editable-content clearfix"]')

        #Obtengo la imagenUrl
        imagenUrl = contenido.xpath(".//div[contains(concat(' ', normalize-space(@class), ' '), ' image ')]//img/@src").extract()
        #Si el articulo tiene una imagen asignada, guardo el link a dicha imagenUrl
        #Sino, indico que esa noticia no tiene imagen
        if len(imagenUrl) == 1:
            item['imagenUrl'] = imagenUrl[0]
        else:
            item['imagenUrl'] = "noUrl"

        #Notar el uso de ./text() EL PUNTO, esto me permite tomar el texto DENTRO del div.
        parrafo = contenido.xpath('./text()').extract()
        if parrafo:
            item['texto'] = ''.join(parrafo)

            #Calculo el sentiment
            client = repustate.Client(api_key='0378996fbd7c59fd4d5837125fe07f255550587d')
            resultado = client.sentiment(text=item['texto'].encode('utf-8'),lang='es')
            #El resultado es un diccionario con la key status y con la key score
            if resultado['status'] == "OK":
                item['sentiment'] = resultado['score']
                yield item
