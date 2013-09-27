def socrata(d):
    return {
        "uri": "",
        "portal_software": "socrata",
        "portal": "",
        "dataset_id": d['id'],

        "name" : d['name'],
        "description" : d['description'],
        "keywords": d['tags'],

        "publishing_organization": d['attribution'],
        "source_url":  d['attributionLink'],
        "license": d['license'],

        "columns": [col['name'] for col in d['columns']],
        "raw_metadata": d,
    }
