import re
import pandas
from standardize import iter_datasets, map_reduce

def standard_license(raw_license):
    r = raw_license.lower()
    if re.match('.*(Dom.nio P.blico|domaine public|public domain|cczero).*', r):
        return 'Public domain'
    elif re.match('.*(odbl|open database license).*', r):
        return 'ODbL'
    elif re.match(r'.*(especificada|sp.cifi.e|specified).*$', r):
        return 'Not specified'
    elif re.match(r'^(cc|creative commons)(.*)', r):
        return creative_commons(re.match(r'^(cc|creative commons)(.*)', r).group(2))
    elif re.match(r'^.*(open data).*', r):
        return 'Other open data license'
    elif r == u'GNU Free Documentation License':
        return 'GFDL'
    elif re.match(r'^.*(open|oiuverte|libre|ouverte|aberta|abierta).*', r):
        return 'Other open license'
    else:
        # print raw_license
        return 'Other'

def creative_commons(r):
    attribution = ''
    share_alike = ''
    non_commercial = ''
    no_derivative = ''

    if re.match(r'.*(attribution|by).*', r):
        attribution = '-BY'

    if re.match(r'.*(share.?alike|sa).*', r):
        share_alike = '-SA'

    if re.match(r'.*(non.?commerical|nc).*', r):
        non_commercial = '-NC'

    if re.match(r'.*(derivative|nd).*', r):
        no_derivative = '-ND'

    if 'universal' in r:
        return 'Public domain'
    else:
        a = 'CC' + attribution + share_alike + no_derivative + non_commercial
        if a == 'CC':
            print r
        return a

'''
# datasets = list(iter_datasets())
official = [dataset for dataset in datasets if dataset['portal'] not in {'datahub.io', 'opendata.socrata.com', 'datastore.opendatasoft.com'}]
for dataset in official:
    del dataset['raw_metadata']


df = pandas.DataFrame(official)
licenses = df.groupby(['license']).count()['uri']
# license_portals = df.groupby(['license', 'portal']).count()['uri']
'''
