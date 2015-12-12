# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from places_crawler.items import PlacesCrawlerItem


class LocuridinroSpider(scrapy.Spider):
    name = "locuridinro"
    allowed_domains = ["locuridinromania.ro"]
    start_urls = (
        u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-alba', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-arad'
    )

    def parse(self, response):
        responseSelector = Selector(response)

        for sel in responseSelector.xpath('//article'):
            item = PlacesCrawlerItem()
            name = sel.xpath('header/a/@title').extract()
            item['name'] = name[0] if name else ""
            item['link'] = sel.xpath('header/a/@href').extract()
            item['short_decription'] = sel.xpath('div[@class="entry-content"]').extract()

            yield item
