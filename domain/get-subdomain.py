#!/usr/bin
#-*- coding: utf-8 -*-
#DATA:2017年5月9日
#AUTHOR:lcamry
#blog：http://www.cnblogs.com/lcamry
#QQ:646878467
#usage:python get-subdomain.py mogujie.com
import sys,os
import urllib2
from lxml import html

class submain():
    def __init__(self,submain):
        self.submain = submain
        self.url_360 = 'http://webscan.360.cn/sub/index/?url=%s' %self.submain
        self.url_link = 'http://i.links.cn/subdomain/'
        self.url_baidu = 'https://www.baidu.com/s?wd=site:%s&pn=20'%self.submain
        self.link_post = 'domain=%s&b2=1&b3=1&b4=1' %self.submain
        self.sublist = []
    def get_360(self):
        scan_data = urllib2.urlopen(self.url_360).read()
        html_data = html.fromstring(scan_data)
        submains = html_data.xpath("//dd/strong/text()")
        return self.sublist.extend(submains)
    def get_links(self):
        link_data = urllib2.Request(self.url_link,data=self.link_post)
        link_res = urllib2.urlopen(link_data).read()
        html_data = html.fromstring(link_res)
        submains = html_data.xpath("//div/div[@class='domain']/a//@href")
        submains = [i.replace('http://','') for i in submains]
        return self.sublist.extend(submains)

#    def get_baidu(self):
#        scan_baidu_data = urllib2.urlopen(self.url_baidu).read()
#        html_baidu_data = html.fromstring(scan_baidu_data)

#        return self.sublist.extend(submains)
    def scan_domain(self):
        self.get_360()
        self.get_links()
        return list(set(self.sublist))
if __name__ == '__main__':
    domain = sys.argv[1]
    submain = submain(domain).scan_domain()
    f=open("lcamry.txt",'a+')
    print "blog:http://www.cnblogs.com/lcamry"
    print "lcamry qq:646878467"
    print "start,processing"
    print "..................."
    for line in  submain:
        f.write(line)
        f.write('\n')
    print "It has done!Please get more from lcamry.txt"