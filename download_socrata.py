#!/usr/bin/env python2
'''
https://github.com/jasonlally/open-data-browser/blob/dev/data/dataportalapi.py
'''

import os
from urllib import urlretrieve
import portals

def download(portal_url, directory):
    '''
    Args:
        portal: A string for the root of the portal (like "http://demo.ckan.org")
        directory: The directory to which stuff should be saved
    Returns:
        Nothing
    '''
    # Make sure the directory exists.
    try:
        os.makedirs(directory)
    except OSError:
        pass

    url = 'http://' + portal_url + '/api/search/views.json'
    urlretrieve(url, os.path.join(directory, portal_url))

def main():
    for portal in portals.socrata:
        download(portal, os.path.join('portals', 'socrata'))
