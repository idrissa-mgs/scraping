import scrapy
import os
from bs4 import BeautifulSoup
from scrapy.loader import ItemLoader
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from items import JumiaSnItem

class a2b(scrapy.Spider):
    """
    Cette classe implémente un spider pour a2b. Elle hérite donc de la classe
    Spider de Scrapy.
    Obligatoirement cette classe doit posséder une méthode parse ainsi que name,
    allowed_domains et start_urls.
    """
    name = 'jumia_sn'
    allowed_domains = ['jumia.sn']
    start_urls = ['https://www.jumia.sn/mlp-informatique/ordinateurs-pc/']

    handle_httpstatus_list = [503, 502, 403]

    # To avoid "duplicate request"
    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    def parse(self, response):
        if response.status in self.handle_httpstatus_list:
            print('ERROR:', response.status, )
            #print('ERROR:', response.text )

        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all("a", {"class": "core"})
            #title = price = categories = description = link = None
            if products:
                for product in products:
                    #title = product['data-name']
                    link = "https://www.jumia.sn"+ product['href']
                    yield scrapy.Request(link, callback=self.parse_product)

            next_page = soup.find("a", {"class":"pg", "aria-label" : "Page suivante"})
            if next_page:
                next_url = next_page['href']
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url, callback=self.parse)



    def parse_product(self, response):

        if response.status in self.handle_httpstatus_list:
            print('ERROR:', response.status, )
            #print('ERROR:', response.text )

        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            # items = soup.find_all('a', {"class": "link"})
            if response.status in self.handle_httpstatus_list:
                print('ERROR:', response.status)
            if soup:
                #link
                link = response.url
                # titre
                title = None
                title = soup.find_all("h1", {"class": "-fs20 -pts -pbxs"})
                if title:
                    title = title[0].text
                # price
                price = None
                price = soup.find_all("span", {"class": "-b -ltr -tal -fs24", "dir": "ltr"})
                if price:
                    price = price[0].text.strip()
                dico_cat = {}
                categories = soup.find_all("a", {"class": 'cbs'})
                if categories:
                    for i, cat in enumerate(categories[1:-1]):
                        dico_cat[f'category {i + 1}'] = cat.text
                # description
                description = ''
                desc = soup.find('div', {"class":"markup -mhm -pvl -oxa -sc"})
                if desc:
                    description = desc.text.replace('\xa0', ' ').strip()

                # image
                images = []
                img = soup.find_all("img", {"class":"-fw _ni"})
                if img:
                    for im in img:
                        images.append(im['src'])
                    images = [x for x in images if 'jpg' in x ]
                item = ItemLoader(item=JumiaSnItem(), response=response)
                item.add_value('title', title)
                item.add_value('link', link)
                item.add_value('price', price)
                item.add_value('categories', dico_cat)
                item.add_value('description', description)

                item.add_value('images_url', images)

                yield item.load_item()
