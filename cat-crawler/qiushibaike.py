# -*- coding:utf-8 -*-
import urllib2
import datetime
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/%s' % page

# request headers
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
headers = {
    'User-Agent': user_agent
}

try:
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request)

    content = response.read()

    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?>(.*?)</a>.*?<div.*?class="content.*?>(.*?)<!--(.*?)-->.*?</div>.*?<div class="stats.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        author = item[0].strip()
        if '<img' in item[0]:
            author = item[0].split('>')[1].strip()
        print "author:  ", author
        print "content: ", item[1].strip().replace("<br/>", "\n")
        print "time:    ", datetime.datetime.fromtimestamp(int(item[2].strip())).isoformat(" ")
        print "good:    ", item[3].strip()
        print "comment: ", item[4].strip()
        print "-" * 150
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

