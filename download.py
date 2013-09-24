#!/usr/bin/env python

from download_ckan import download as ckan
import portals

ckan("http://demo.ckan.org", '/tmp/ckan')
