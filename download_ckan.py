# https://twitter.com/CKANproject/status/378182161330753536
import ckanapi
import pprint
from time import sleep

from portals import ckan

def download(portal, directory):
    '''
    Args:
        portal: A string for the root of the portal (like "http://demo.ckan.org")
        directory: The directory to which stuff should be saved
    Returns:
        Nothing
    '''
    portal = ckanapi.RemoteCKAN(portal)
    datasets = portal.action.package_list()
    for dataset in datasets:
        _save_dataset(id)
        sleep(3)

def _save_dataset(id)
        portal.action.package_show(id=id)
