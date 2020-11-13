# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import itemadapter
class JumiaSnPipeline(object):
    def process_item(self, item, spider):

        adapter = itemadapter.ItemAdapter(item)
        items = ["title", "link", 'price', 'categories', 'description']
        for my_item in items:
            it_ = adapter.get(my_item)
            if it_:
                if isinstance(it_, list):
                    adapter[my_item] = adapter[my_item][0]
        return item




from scrapy.exceptions import DropItem
