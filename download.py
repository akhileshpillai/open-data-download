#!/usr/bin/env python
import os

from download_ckan import download as ckan
import portals

ROOT_DIR = 'portals'

for portal in portals.ckan:
    ckan("http://" + portal, os.path.join(ROOT_DIR, 'ckan', portal))
