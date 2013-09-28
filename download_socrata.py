from time import sleep
import os, json

from lxml.html import fromstring
from urllib2 import urlopen
from requests import get

APP_TOKEN = 'gTddlqVLsV4DkBlXnDSwnTazB'

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
        os.makedirs(os.path.join(directory, portal_url))
    except OSError:
        pass

    url = u'https://' + portal_url + u'/browse/embed?limitTo=datasets&q=&utf8=%E2%9C%93&view_type=table'
    html = fromstring(urlopen(url).read())
    search_bases = html.xpath(u'//a[text()="This site only"]/@href')

    if len(search_bases) == 0:
        search_base = url
    else:
        search_base = u'https://' + portal_url + search_bases[0]

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
    url = "http://%s/views/%s.json?app_token=%s" % (portal_url, id, APP_TOKEN)
    filename = os.path.join(directory, portal_url, id)
    if os.path.exists(filename):
        pass # print 'Already downloaded %s from %s' % (dataset, portal_url)
    else:
        try:
            r = get(url)
            if r.status_code != 200:
                raise Exception('Something went wrong when I was accessing Socrata.')
            fp = open(filename, 'w')
            fp.write(r.text)
            f.close()
        except:
            print '**Error at https://%s/d/%s' % (portal_url, id)
        else:
            print '  Downloaded https://%s/d/%s' % (portal_url, id)
        sleep(7)

def parse_search_page(search_base, number):
    'Get 4x4s out of a search page.'
    html = fromstring(urlopen(search_base + '&page=%d' % number).read())
    hrefs = html.xpath('//td[@class="nameDesc"]/a/@href')
    return [href.split('/')[-1] for href in hrefs]

if __name__ == '__main__':
    # download(u'data.hawaii.gov', u'portals/socrata')
    download(u'data.nola.gov', u'portals/socrata')
