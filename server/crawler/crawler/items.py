# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InfobaeNoticiaItem(scrapy.Item):
    titulo = scrapy.Field()
    texto = scrapy.Field()
    imagenUrl = scrapy.Field()
    sentiment = scrapy.Field()
    diario = scrapy.Field()

class TelamNoticiaItem(scrapy.Item):
    titulo = scrapy.Field()
    texto = scrapy.Field()
    imagenUrl = scrapy.Field()
    sentiment = scrapy.Field()
    diario = scrapy.Field()

class Pagina12NoticiaItem(scrapy.Item):
    titulo = scrapy.Field()
    texto = scrapy.Field()

class InfobaePortadaItem(scrapy.Item):
    titulo = scrapy.Field()
    url = scrapy.Field()
    diario = scrapy.Field()

class TelamPortadaItem(scrapy.Item):
    titulo = scrapy.Field()
    url = scrapy.Field()
    diario = scrapy.Field()

class Pagina12PortadaItem(scrapy.Item):
    titulo = scrapy.Field()
    url = scrapy.Field()
