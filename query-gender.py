import re

import pandas

from standardize import iter_datasets, map_reduce

def has_gender(string):
    wacky_string = ' ' + string.lower().replace('_', ' ') + ' '
    return re.match(r'^.* (men|man|males?|girls?|boys?) .*$', wacky_string) != None

def has_female(string):
    wacky_string = ' ' + string.lower().replace('_', ' ') + ' '
    return re.match(r'^.* (women|woman|females?|girls?) .*$', wacky_string) != None

# Subset the datasets
def gendered(pair):
    uri, column_names = pair
    columns_blob = ' '.join(column_names)
    return has_gender(columns_blob)

def gendered_columns(column_names):
    return filter(has_gender, column_names)

# How many "male" and "female"?
def how_many(pair):
    '''
    Args:
        A tuple of (uri, column_names)
    Returns:
        A dictionary
    '''
    uri, column_names = pair
    n_gendered = len(filter(has_gender, column_names))
    n_female   = len(filter(has_female, column_names))
    return {
        'uri': uri,
        'n_gendered': n_gendered,
        'n_female': n_female,
    }

def go():
    # load the data into memory
    datasets = list(iter_datasets())

    # Subset
    columns = list(map_reduce(lambda d: (d['uri'], d['columns']), datasets = datasets))
    gendered_datasets = filter(gendered, columns)

    g_dict = dict(zip((d[0] for d in gendered_datasets), zip(map(how_many, gendered_datasets), map(gendered_columns, (d[1] for d in gendered_datasets)), (d[1] for d in gendered_datasets))))
    for k,v in g_dict.items():
        g_dict[k] = v[0]
        g_dict[k]['gendered_columns'] = v[1]
        g_dict[k]['all_columns'] = v[2]

    g_df = pandas.DataFrame(g_dict)[['uri', 'n_gendered', 'n_female']]

    # Results
    print '%d datasets appear to have gender in the column names:' % len(gendered_datasets)
    print [d[0] for d in gendered_datasets]
    print ''
