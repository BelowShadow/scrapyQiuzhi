# -*- coding: utf-8 -*-
import scrapy
#这是调度器
from qiuzhi.items import QiuzhiItem  #引用items里定义的DoubanItem数据结构

class QiuzhiSpider(scrapy.Spider):

    name = 'qiuzhi_spider'

    #爬虫爬的域名
    allowed_domains = ['zhaopin.baidu.com']
    #入口url
    start_urls = ['https://zhaopin.baidu.com/quanzhi?query=%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86+%E6%8B%9B%E8%81%98&city_sug=%E5%8C%97%E4%BA%AC&zp_fr=aladdin-5463-zp_exact_new']

    # 在这里解析
    def parse(self, response):
        job_list = response.xpath("//div[@class='listitem']//a//div")
        number = 0
        for i_item in job_list:
            qiuzhi_itme =QiuzhiItem()
            qiuzhi_itme['jobName'] = i_item.xpath(".//div[@class='title']/text()").extract_first()  # 获取第一个数据
            qiuzhi_itme['company'] = i_item.xpath(".//span[@class='inlineblock companyname']/text()").extract_first()  # 获取第一个数据
            qiuzhi_itme['salary'] = i_item.xpath(".//span[@class='inlineblock num']/text()").extract_first()  # 获取第一个数据
            qiuzhi_itme['company_position'] = i_item.xpath(".//div[@class='detail']//span[1]/text()").extract_first()  # 获取第一个数据
            qiuzhi_itme['degreeNeed'] = i_item.xpath(".//div[@class='detail']//span[3]/text()").extract_first()  # 获取第一个数据

            qiuzhi_itme['workExperience'] = i_item.xpath(".//div[@class='detail']//span[5]/text()").extract_first()  # 获取第一个数据

           # douban_item['publishedTime'] = i_item.xpath(".//div[@class='title']/text()").extract_first()  # 获取第一个数据
           # qiuzhi_itme['job_Description'] = i_item.xpath(".//div[@class='title']/text()").extract_first()  # 获取第一个数据

           # qiuzhi_itme['company'] = i_item.xpath(".//div[@class='title']/text()").extract_first()  # 获取第一个数据
            yield qiuzhi_itme
