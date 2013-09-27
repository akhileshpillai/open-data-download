def socrata(d, portal, id):
    if id != d['id']:
        raise ValueError('The id argument must match the id in the json file.')

    return {
        u"uri": u"https://%s/d/%s" % (portal, id),
        u"portal_software": u"socrata",
        u"portal": portal,
        u"dataset_id": d['id'],

        u"title" : d['name'],
        u"description" : d['description'],
        u"keywords": d['tags'],

        u"publishing_organization": d['attribution'],
        u"source_url":  d['attributionLink'],
        u"license": d['license']['name'],

        u"columns": [col['name'] for col in d['columns']],
        u"raw_metadata": d,
    }

def opendatasoft(d, portal, id):
    if id != d['datasetid']:
        raise ValueError('The id argument must match the dataset_id in the json file.')

    return {
        u"uri": u"http://%s/explore/dataset/%s" % (portal, id),
        u"portal_software": u"opendatasoft",
        u"portal": portal,
        u"dataset_id": d['datasetid'],

        u"title" : d['metas']['title'],
        u"description" : d['metas']['description'],
        u"keywords": d['metas']['keyword'],

        u"publishing_organization": d['metas']['publisher'],
        u"source_url":  d['metas']['references'],
        u"license": d['metas']['license'],

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
        u"description" : d['notes'],
        u"keywords": [col['name'] for col in d['tags']],

        u"publishing_organization": '',
        u"source_url":  d['url'],
        u"license": d['license_title'],

        u"columns": [],
        u"raw_metadata": d,
    }
