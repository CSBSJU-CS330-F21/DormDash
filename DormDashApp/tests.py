#!/usr/bin/python
#encoding:utf-8
import HTMLParser
import urlparse
import cookielib
import string
import urllib
import urllib2
import string
import re
from jpype import *
from sms import Sms,Sms2
import os.path,sys
from django.core.management import setup_environ
ROOT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0,ROOT_PATH[0])
import settings
set = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

class CheckWeb:
       def CheckAnalytics(self):
               try:
                       hosturl = 'https://****************'
                       posturl = 'https://*****************'
               #h = urllib2.urlopen(hosturl)
                       postData = {'email' : '*********','password' : '**************'}
                       postData = urllib.urlencode(postData)
                       request = urllib2.Request(posturl, postData)
                       response = urllib2.urlopen(request)
                       text1 = response.read()
                       return text1
               except:
                       text1 = 'error'
                       return text1
       def CheckAppcpa(self):
               try:
               #hosturl = 'http://www.DormDash.com'
                       posturl = 'http://www.DormDash.com'
                       cj = cookielib.LWPCookieJar()
                       cookie_support = urllib2.HTTPCookieProcessor(cj)
                       opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
                       urllib2.install_opener(opener)
               #h = urllib2.urlopen(hosturl)
                       headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0','Referer' : 'http://www.appcpa.co/appcpaLogin/login.jsp'}
                       postData = {'type' : '0','email' : '000@000.com','password' : '*****','checked' : 'false','tempppp' : '0.8753980695792317'}//
                       postData = urllib.urlencode(postData)
                       request = urllib2.Request(posturl, postData, headers)
                       response = urllib2.urlopen(request)
                       text2 = response.read()
                       return text2
               except:
                       text2 = 'error'
                       return text2
       def CheckGame(self):
               #hosturl = 'http://www.*****.com/'
               try:
                       posturl = 'http://www.***.com'
                       cj = cookielib.LWPCookieJar()
                       cookie_support = urllib2.HTTPCookieProcessor(cj)
                       opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
                       urllib2.install_opener(opener)
               #h = urllib2.urlopen(hosturl)
                       postData = {'type' : '0','email' : '000@000.com','password' : '*****','checked' : 'false','tempppp' : '0.8753980695792317'}
                       postData = urllib.urlencode(postData)
                       request = urllib2.Request(posturl, postData)
                       response = urllib2.urlopen(request)
                       text3 = response.read()
                       return text3
               except:
                       text3 = 'error'
                       return text3
if __name__ == '__main__':
       allweb = CheckWeb()
       analy = allweb.CheckAnalytics()
       if analy != '1': 
               print 'no'
       else:
               print 'yes'
       appcp = allweb.CheckAppcpa()
       if appcp != 'success': 
               print 'no'
       else:
               print 'yes'
       gam = allweb.CheckGame()
       if gam != '1':
               print 'no'
       else:
               print 'yes'
