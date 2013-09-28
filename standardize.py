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

def opendatasoft(d, portal):
    return {
        u"uri": u"http://%s/explore/dataset/%s" % (portal, d['datasetid']),
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

def go():
    for portal in os.listdir(os.path.join('portals', 'ckan')):
        portal_dir = os.path.join('portals', 'ckan', portal)
        for dataset in os.listdir(portal_dir):
            raw = json.load(open(os.path.join(portal_dir, dataset)))
            yield ckan(raw, portal, dataset)

    for portal in os.listdir(os.path.join('portals', 'socrata')):
        portal_dir = os.path.join('portals', 'socrata', portal)
        for dataset in os.listdir(portal_dir):
            raw = json.load(open(os.path.join(portal_dir, dataset)))
            yield socrata(raw, portal, dataset)

    for portal in os.listdir(os.path.join('portals', 'opendatasoft')):
        data = json.load(open(os.path.join('portals', 'opendatasoft', portal)))
        for raw in data['datasets']:
            yield opendatasoft(raw, portal)
