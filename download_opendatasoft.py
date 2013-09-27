from time import sleep
import os, json
from urllib import urlretrieve

def download(portal_url, directory):
    '''
    Args:
        portal: A string for the root of the portal (like "http://demo.ckan.org")
        directory: The directory to which stuff should be saved
    Returns:
        Nothing
    '''
    # http://parisdata.opendatasoft.com/api/datasets/1.0/search?rows=1000000

    # Make sure the directory exists.
    try:
        os.makedirs(directory)
    except OSError:
        pass

    try:
        urlretrieve('http://' + portal_url + '/api/datasets/1.0/search?rows=1000000', os.path.join(directory, portal_url))
    except:
        print '**Error downloading %s**' % (portal_url)
    else:
        print '  Downloaded %s' % (portal_url)

if __name__ == '__main__':
    download('parisdata.opendatasoft.com', 'portals/opendatasoft')
