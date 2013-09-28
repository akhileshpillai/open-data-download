import os, json

def socrata(d, portal, id):
    if id != d['id']:
        print id
        raise ValueError('The id argument must match the id in the json file.')

    return {
        u"uri": u"https://%s/d/%s" % (portal, id),
        u"portal_software": u"socrata",
        u"portal": portal,
        u"dataset_id": d['id'],

        u"title" : d['name'],
        u"description" : d.get('description'),
        u"keywords": d.get('tags', []),

        u"publishing_organization": d.get('attribution',''),
        u"source_url":  d.get('attributionLink',''),
        u"license": d.get('license', {'name': ''})['name'],

        u"columns": [col['name'] for col in d['columns']],
        u"raw_metadata": d,
    }

def opendatasoft(d, portal):
    return {
        u"uri": u"http://%s/explore/dataset/%s" % (portal, d['datasetid']),
        u"portal_software": u"opendatasoft",
        u"portal": portal,
        u"dataset_id": d['datasetid'],

        u"title" : d['metas']['title'],
        u"description" : d['metas'].get('description'),
        u"keywords": d['metas'].get('keyword'),

        u"publishing_organization": d['metas'].get('publisher'),
        u"source_url":  d['metas'].get('references'),
        u"license": d['metas'].get('license'),

        u"columns": [col['name'] for col in d['fields']],
        u"raw_metadata": d,
    }

def ckan(d, portal, name):
    if name != d['name']:
        raise ValueError('The name argument must match the name in the json file.')

    return {
        u"uri": u"http://%s/dataset/%s" % (portal, name),
        u"portal_software": u"ckan",
        u"portal": portal,
        u"dataset_id": d['id'],

        u"title" : d['title'],
        u"description" : d.get('notes'),
        u"keywords": [col['name'] for col in d.get('tags', [])],

        u"publishing_organization": '',
        u"source_url":  d.get('url'),
        u"license": d.get('license_title'),

        u"columns": [],
        u"raw_metadata": d,
    }

def iter_datasets():
    import os

    opendatasoft_dir = os.path.join('portals', 'opendatasoft')
    if os.path.isdir(opendatasoft_dir):
        for portal in os.listdir(opendatasoft_dir):
            data = json.load(open(os.path.join('portals', 'opendatasoft', portal)))
            for raw in data['datasets']:
                try:
                    yield opendatasoft(raw, portal)
                except:
                    print 'Error at http;//%s' % portal
                    raise

    socrata_dir = os.path.join('portals', 'socrata')
    if os.path.isdir(socrata_dir):
        for portal in os.listdir(socrata_dir):
            portal_dir = os.path.join('portals', 'socrata', portal)
            for dataset in os.listdir(portal_dir):
                raw = json.load(open(os.path.join(portal_dir, dataset)))
                try:
                    yield socrata(raw, portal, dataset)
                except:
                    print 'Error at https://%s/d/%s' % (portal, dataset)
                    raise

    ckan_dir = os.path.join('portals', 'ckan')
    if os.path.isdir(ckan_dir):
        for portal in os.listdir(ckan_dir):
            portal_dir = os.path.join('portals', 'ckan', portal)
            for dataset in os.listdir(portal_dir):
                raw = json.load(open(os.path.join(portal_dir, dataset)))
                try:
                    yield ckan(raw, portal, dataset)
                except:
                    print 'Error at https://%s/data/%s' % (portal, dataset)
                    raise

def map_reduce(mapper, reducer = None):
    def mapping():
        for dataset in iter_datasets():
            for result in mapper(dataset):
                yield result

    if reducer == None:
        return mapping()
    else:
        return reduce(reducer, mapping())
