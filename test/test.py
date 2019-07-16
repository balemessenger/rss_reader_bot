import datetime
import time
from time import mktime
from dateutil import parser

import feedparser

d = feedparser.parse('https://www.varzesh3.com/rss/all')
from DB.db_handler import update_last_check, get_all_rss

# d = feedparser.parse('http://www.irinn.ir/fa/rss/allnews')
rss = get_all_rss()[0]
entries = d.entries
entries = entries[::-1]
# print(entries[0])
last_rss = None


# print(len(entries))

def convert_utc_to_int(utc_time):
    datetime_number = str(utc_time.tm_year)
    datetime_number += str(utc_time.tm_mon)
    datetime_number += str(utc_time.tm_mday)
    datetime_number += str(utc_time.tm_hour)
    datetime_number += str(utc_time.tm_min)
    datetime_number += str(utc_time.tm_sec)
    datetime_number = int(datetime_number)
    return datetime_number


for i in entries:
    print("sss",i.published)
    # print(mktime(i.published_parsed))
    ip = i.published_parsed
    dt = parser.parse(i.published)
    a=dt.strftime("%Y%m%d%H%M%S")

    import pytz, datetime

    # last_updated = datetime.datetime.fromtimestamp((mktime(i.published_parsed)))
    number = convert_utc_to_int(ip)

    print(number)
    print(type(number))
    update_last_check(rss, number)

    # print(last_updated)
    if not last_rss:
        last_rss = i
    # print(type(i.published_parsed))
    # last_date = rss.last_updated.timetuple()
    # print(last_date)
    # print(i.published_parsed > last_date)
    # print(i.published_parsed > last_date)
    if i.published_parsed > rss.last_updated:
        # print(i.published_parsed,">>",last_rss.published_parsed)
        # last_updated = datetime.datetime.fromtimestamp(mktime(i.published_parsed))
        # update_last_check(rss, last_updated)
        print(i.title)
print(entries[0].published_parsed)
# print(d.update)
# print(d['feed']['title'])
