#!/usr/bin/env python
import os
from multiprocessing import Process

from download_ckan import download as ckan
import portals

ROOT_DIR = 'portals'

def start():
    processes = {}

    for portal in portals.ckan:
        args = ("http://" + portal, os.path.join(ROOT_DIR, 'ckan', portal))
        processes[('ckan', portal)] = Process(target = ckan, args = args)

    return processes

def killall(processes):
    for process in processes.values():
        process.terminate()
