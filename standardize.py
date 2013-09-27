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
