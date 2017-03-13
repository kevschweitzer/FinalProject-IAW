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
import repustate


#Obtengo el titulo y el contenido de cada nota de infobae obteniendo la url de la noticia desde la base de datos
class InfobaeSpider(scrapy.Spider):
    name = 'infobae'
    start_urls = []

    #Me conecto a la base de datos y obtengo las urls de las noticias de portada de infobae
    def __init__(self):
        self.db = MongoClient() #localhost por defecto
        self.urls = self.db.proyectofinal.portadas.find({"diario":"Infobae"},{"_id": 0, "titulo": 0}) #use appropriate finding criteria here according to the structure of data resides in that collection

    #El start_urls se va a completar con las urls obtenidas desde la base de datos
    def start_requests(self):
        for url in self.urls:
            texto ="http://www.infobae.com"
            texto += ''.join(url["url"])
            yield Request(texto, self.parse)



    def parse(self, response):

        #Creo el item
        item = InfobaeNoticiaItem()

        #Estoy obteniendo el titulo del articulo
        item['titulo'] = response.xpath('//h1/text()')[0].extract()

        #En infobae, los parrafos con el texto estan bajo la class = row
        #Obtengo todos los row
        row = response.xpath('//div[@class="row"]')
        #Por cada row, me meto en el div y luego en el p. Obtengo el texto
        #Ver que en lugar de usar /text() , uso //text esto me permite ir a todo los hijos
        #Es decir, en caso de que exista un tag <strong>texto</strong>, voy a obtener el texto de todos modos. Sin saltearlo
        texto = ""
        for r in row:
            parrafo = r.xpath('div/p//text()').extract()
            #Si lo extraido tiene contenido, luego guardo printeo como un string.
            #El join sirve para concatenar los elementos de la lista
            if parrafo:
                texto += ''.join(parrafo)

        #Guardo el texto de la noticia
        item['texto'] = texto

        imagenUrl = response.xpath('//div[@class="single-image"]//img/@data-original').extract()
        if len(imagenUrl):
            item['imagenUrl'] =  imagenUrl[0]

        #Calculo el sentiment
        client = repustate.Client(api_key='0378996fbd7c59fd4d5837125fe07f255550587d')
        resultado = client.sentiment(text=item['texto'].encode('utf-8'),lang='es')
        #El resultado es un diccionario con la key status y con la key score
        if resultado['status'] == "OK":
            item['sentiment'] = resultado['score']
            #Retorno el item
            yield item
