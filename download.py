#!/usr/bin/env python
import os
import threading

from download_ckan import download as ckan
import portals

ROOT_DIR = 'portals'

threads = {}

for portal in portals.ckan:
    args = ("http://" + portal, os.path.join(ROOT_DIR, 'ckan', portal))
    threads[('ckan', portal)] = threading.Thread(target = ckan, args = args)


'''
    thr.start() # will run "foo"
    thr.is_alive() # will return whether foo is running currently
    thr.join()
'''
