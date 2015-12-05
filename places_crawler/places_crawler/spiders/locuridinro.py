# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from places_crawler.items import PlacesCrawlerItem


class LocuridinroSpider(scrapy.Spider):
    name = "locuridinro"
    allowed_domains = ["locuridinromania.ro"]
    start_urls = (
        u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-alba', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-arad', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-arges', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-bacau', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-bihor', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-bistrita-nasaud', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-botosani', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-braila', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-brasov', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-bucuresti', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-buzau', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-calarasi', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-caras-severin', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-cluj', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-constanta', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-covasna', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuir-din-judetul-dambovita', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-dolj', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-galati', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-giurgiu', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-gorj', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-harghita', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-hunedoara', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-ialomita', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-iasi', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-ilfov', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-maramures', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-mehedinti', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuir-din-judetul-mures', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-neamt', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-olt', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-prahova', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-salaj', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-satu-mare', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-sibiu', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-suceava', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-teleorman', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-timis', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-tulcea', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-valcea', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-vaslui', u'http://www.locuridinromania.ro/categorie/locuri-de-vizitat-in-romania/locuri-din-judetul-vrancea'
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
