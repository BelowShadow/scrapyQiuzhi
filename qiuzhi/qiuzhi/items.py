# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiuzhiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serialNumber = scrapy.Field() #序号
    jobName = scrapy.Field() #工作名称
    company = scrapy.Field() #公司名称
    salary = scrapy.Field()  # 工资
    company_position = scrapy.Field() #工作地点
    degreeNeed= scrapy.Field() #学位要求
    workExperience = scrapy.Field() #工作经验要求
    publishedTime = scrapy.Field() #发布日
    job_Description    = scrapy.Field() #职位描述


    pass
