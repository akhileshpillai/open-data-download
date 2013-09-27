#!/usr/bin/env python
from time import sleep
import os, json
from multiprocessing import Process

import ckanapi # https://twitter.com/CKANproject/status/378182161330753536

import portals

ROOT_DIR = 'portals'

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

    try:
        datasets = portal.action.package_list()
    except:
        print '**Error searching %s**' % portal_url
        return

    for dataset in datasets:
        filename = os.path.join(directory, dataset)
        if os.path.exists(filename):
            pass # print 'Already downloaded %s from %s' % (dataset, portal_url)
        else:
            print '  Downloading %s from %s' % (dataset, portal_url)
            dataset_information = portal.action.package_show(id = dataset)
            fp = open(filename, 'w')
            json.dump(dataset_information, fp)
            fp.close()
            sleep(3)
    print '**Finished downloading %s**' % portal_url

def check_one(portal_url):
    '''
    Args:
        portal: A string for the root of the portal (like "http://demo.ckan.org")
    Returns:
        A boolean indicating whether the datasets could be searched, and
        maybe an integer indicating how many datasets
    '''

    portal = ckanapi.RemoteCKAN(portal_url)
    try:
        datasets = portal.action.package_list()
    except:
        return False, None
    else:
        return True, len(datasets)

def check_all():
#   p = ['http://' + portal for portal in portals.ckan]
#   return dict(zip(p, map(check_one, p)))
    for portal in portals.ckan[1:]:
        for protocol in ['http://']:
            works, count = check_one(protocol + portal)
            works_str = 'TRUE' if works else 'FALSE'
            print portal + ',' + works_str + ',' + ('NA' if count == None else str(count))

def create():
    processes = {}

    for portal in portals.ckan:
        args = ("http://" + portal, os.path.join(ROOT_DIR, 'ckan', portal))
        processes[('ckan', portal)] = Process(target = download, args = args)

    return processes

def start(processes):
    'Start all of the processes.'
    for process in processes.values():
        process.start()

def join(processes):
    'Wait for all of the processes to end.'
    for process in processes.values():
        process.join()

def kill(processes):
    'Kill all of the processes.'
    for process in processes.values():
        process.terminate()

def main():
    import signal
    import sys

    p = create()

    def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        kill(p)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    start(p)
    join(p)

if __name__ == '__main__':
    # main()
    check_all()
