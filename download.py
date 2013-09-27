#!/usr/bin/env python2
from multiprocessing import Process
import os

import portals
from download_ckan import download as ckan
from download_socrata import download as socrata
from download_opendatasoft import download as opendatasoft

ROOT_DIR = 'portals'

def create(portal_type, func, portal_urls):
    '''
    Args:
        portal_type: "ckan", "opendatasoft" or "socrata"
        func: function to download all datasets given a portal and directory
        portal_urls: List of portal domains
    Returns:
        A list of processes
    '''
    processes = {}

    for portal in portal_urls:
        args = (portal, os.path.join(ROOT_DIR, portal_type))
        processes[(portal_type, portal)] = Process(target = func, args = args)

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

    # p = create('ckan', ckan, portals.ckan)
    # p = create('opendatasoft', opendatasoft, portals.opendatasoft)
    p = create('socrata', socrata, portals.socrata)

    def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        kill(p)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    start(p)
    join(p)

if __name__ == '__main__':
    main()
