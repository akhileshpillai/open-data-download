# https://twitter.com/CKANproject/status/378182161330753536
import ckanapi
import pprint

demo = ckanapi.RemoteCKAN('http://demo.ckan.org')
groups = demo.action.group_list(id='data-explorer')
pprint.pprint(groups)
