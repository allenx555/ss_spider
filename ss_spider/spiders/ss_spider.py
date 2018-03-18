# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 0016 18:53
# @Author  : allenx555
# @FileName: ss_spider.py
# @Software: PyCharm

import scrapy
from ss_spider.items import SsSpiderItem
import urllib


class ss_spider(scrapy.Spider):

    name = "ss_spider"
    start_urls = []
    allowed_domains = ['en.ishadowx.net', 'isx.yt', 'isx.tn']

    try:
        url = "https://en.ishadowx.net/"
        req = urllib.request.Request(url, None)
        res = urllib.request.urlopen(req, timeout=10)
        res.close()
        start_urls.append(url)
    except urllib.error.HTTPError:
        url = "isx.yt"
        req = urllib.request.Request(url, None)
        res = urllib.request.urlopen(req, timeout=10)
        res.close()
        start_urls.append(url)
    except urllib.error.HTTPError:
        url = "isx.tn"
        req = urllib.request.Request(url, None)
        res = urllib.request.urlopen(req, timeout=1)
        res.close()
        start_urls.append(url)

    def parse(self, response):
        item = SsSpiderItem()
        item['US_IP'] = response.xpath('//*[@id="ipusa"]/text()').extract()[0]
        item['US_Port'] = response.xpath('//*[@id="portusa"]/text()').extract()[0]
        item['US_PW'] = response.xpath('//*[@id="pwusa"]/text()').extract()[0]
        item['JP_IP'] = response.xpath('//*[@id="ipjpa"]/text()').extract()[0]
        item['JP_Port'] = response.xpath('//*[@id="portjpa"]/text()').extract()[0]
        item['JP_PW'] = response.xpath('//*[@id="pwjpa"]/text()').extract()[0]
        item['SG_IP'] = response.xpath('//*[@id="ipsga"]/text()').extract()[0]
        item['SG_Port'] = response.xpath('//*[@id="portsga"]/text()').extract()[0]
        item['SG_PW'] = response.xpath('//*[@id="pwsga"]/text()').extract()[0]
        return item
