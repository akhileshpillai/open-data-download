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
    datasets = portal.action.package_list()

    for dataset in datasets:
        filename = os.path.join(directory, dataset)
        if os.path.exists(filename):
            print 'Already downloaded %s from %s' % (dataset, portal_url)
        else:
            print 'Downloading %s from %s' % (dataset, portal_url)
            dataset_information = portal.action.package_show(id = dataset)
            fp = open(filename, 'w')
            json.dump(dataset_information, fp)
            fp.close()
            sleep(3)

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

if __main__ == '__main__':
    p = create()
    start(p)
    join(p)
