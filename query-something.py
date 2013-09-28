import re
import pandas
from standardize import iter_datasets, map_reduce

def standard_license(raw_license):
    r = raw_license.lower()
    if re.match('.*(public domain|cczero).*', r):
        return 'Public domain'
    elif re.match('.*(odbl|open database license).*', r):
        return 'ODbL'
    elif re.match(r'.*(especificada|sp.cifi.e|specified).*$', r):
        return 'Not specified'
    elif re.match(r'^(cc|creative commons)(.*)', r):
        return creative_commons(re.match(r'^(cc|creative commons)(.*)', r).group(2))
    else:
        return raw_license
        return 'Other'

def creative_commons(r):
    attribution = ''
    share_alike = ''
    non_commercial = ''
    if re.match(r'.*(attribution|by).*', r):
        attribution = '-BY'
    elif re.match(r'.*(share-alike|sa).*', r):
        share_alike = '-SA'
    elif re.match(r'.*(non-commerical|nc).*', r):
        non_commercial = '-NC'

    return 'CC' + attribution + share_alike + non_commercial

'''
# datasets = list(iter_datasets())
official = [dataset for dataset in datasets if dataset['portal'] not in {'datahub.io', 'opendata.socrata.com', 'datastore.opendatasoft.com'}]
for dataset in official:
    del dataset['raw_metadata']


df = pandas.DataFrame(official)
licenses = df.groupby(['license']).count()['uri']
# license_portals = df.groupby(['license', 'portal']).count()['uri']
'''
