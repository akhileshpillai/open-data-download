from time import sleep
import os, json

from lxml.html import fromstring
from urllib2 import urlopen
from urllib import urlretrieve

def download(portal_url, directory):
    '''
    Args:
        portal: A string for the root of the portal (like "http://demo.ckan.org")
        directory: The directory to which stuff should be saved
    Returns:
        Nothing
    '''
    # https://data.hawaii.gov/browse/embed?federation_filter=162&limitTo=datasets&q=&utf8=%E2%9C%93&view_type=table

    # Make sure the directory exists.
    try:
        os.makedirs(directory, portal_url)
    except OSError:
        pass

    html = fromstring(urlopen(u'https://' + portal_url + u'/browse/embed?limitTo=datasets&q=&utf8=%E2%9C%93&view_type=table').read())
    search_base = u'https://' + portal_url + html.xpath(u'//a[text()="This site only"]/@href')[0]

    page = 1
    while True:
        ids = parse_search_page(search_base, page)
        if len(ids) == 0:
            break
        else:
            for id in ids:
                download_view(portal_url, directory, id)
            page += 1

def download_view(portal_url, directory, id):
    url = "http://%s/views/%s.json" % (portal_url, id)
    print '  Downloading https://%s/d/%s' % (portal_url, id)
    urlretrieve(url, os.path.join(directory, portal_url, id))

def parse_search_page(search_base, number):
    'Get 4x4s out of a search page.'
    html = fromstring(urlopen(search_base + '&page=%d' % number).read())
    hrefs = html.xpath('//td[@class="nameDesc"]/a/@href')
    return [href.split('/')[-1] for href in hrefs]

if __name__ == '__main__':
    download(u'data.hawaii.gov', u'portals/socrata')
