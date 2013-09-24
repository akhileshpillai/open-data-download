from time import sleep
import os, json

import ckanapi # https://twitter.com/CKANproject/status/378182161330753536
import pprint

from portals import ckan

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

    portal = ckanapi.RemoteCKAN(portal_url)
    datasets = portal.action.package_list()

    for dataset in datasets:
        filename = os.path.join(directory, id)
        if os.path.exists(filename):
            print 'Already downloaded %s from %s' % (id, portal_url)
        else:
            print 'Downloading %s from %s' % (id, portal_url)
            dataset_information = portal.action.package_show(id=id)
            fp = open(filename, 'w')
            json.dump(dataset_information, fp)
            fp.close()
            sleep(3)
