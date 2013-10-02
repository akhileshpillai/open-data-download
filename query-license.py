import re
import pandas
from standardize import iter_datasets, map_reduce

def standard_license(raw_license):
    if not raw_license:
        return 'No license'

    r = raw_license.lower()

    if re.match('.*(Dom.nio P.blico|domaine public|public domain|cczero).*', r):
        return 'Public domain'
    elif re.match('.*(odbl|open database license).*', r):
        return 'ODbL'
    elif 'dl-de-by-1.0' == r:
        return 'dl-de-by-1.0'
    elif 'dl-de-by-nc-1.0' == r:
        return 'dl-de-by-1.0'
    elif u'Nie je uveden\xe1 licencia'.lower() == r:
        return 'No license'
    elif u"La licence n'est pas fournie".lower() == r:
        return 'No license'
    elif re.match(r'.*(especificada|sp.cifi.e|specified).*$', r):
        return 'No license'
    elif re.match(r'^(cc|creative commons)(.*)', r):
        return creative_commons(re.match(r'^(cc|creative commons)(.*)', r).group(2))
    elif re.match(r'^.*(open data).*', r):
        return 'Other open data license'
    elif r == u'GNU Free Documentation License'.lower():
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

    if re.match(r'.*(non.?commericial|nc).*', r):
        non_commercial = '-NC'

    if re.match(r'.*(derivative|nd).*', r):
        no_derivative = '-ND'

    if 'universal' in r:
        return 'Public domain'
    else:
        return 'CC' + attribution + share_alike + no_derivative + non_commercial

'''
# datasets = list(iter_datasets())
official = [dataset for dataset in datasets if dataset['portal'] not in {'datahub.io', 'opendata.socrata.com', 'datastore.opendatasoft.com'}]
for dataset in official:
    del dataset['raw_metadata']


df = pandas.DataFrame(official)

# 13550 null licenses
pandas.isnull(df['license']).sum()

df['license_standard'] = df['license'].map(standard_license)
licenses = df.groupby(['license_standard']).count()['uri']
# license_portals = df.groupby(['license', 'portal']).count()['uri']
'''


def licensing(datasets):
    open_portals = {'datahub.io', 'opendata.socrata.com', 'datastore.opendatasoft.com'}
    official = [dataset for dataset in datasets if dataset['portal'] not in open_portals]
    return pandas.DataFrame(official)

def licensing_by_portal(datasets):
    df = licensing(datasets)
    licensed = df.groupby(['portal']).apply( lambda df:pandas.Series(
        {'no_license':pandas.isnull(df['license']).sum() + (df['license'] == '').sum(), 'all':df.shape[0]}))
    licensed['prop'] = 1 - float(licensed['no_license']) / float(licensed['all'])
    return licensed

'''
datasets = list(iter_datasets())
l = licensing(datasets)
l['license_standard'] = l['license'].map(standard_license)
a = l[l['license_standard'] == 'Other']['license']

print len(a)
print random.sample(a, 40)
'''
# l[['uri','portal_software','portal','license_standard']].to_csv('licensing.csv')
