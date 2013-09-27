from time import sleep
import os, json

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
        os.makedirs(directory)
    except OSError:
        pass

    portal_url
