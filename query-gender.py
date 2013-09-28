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

    df = pandas.DataFrame(map(how_many, gendered_datasets))[['uri', 'n_gendered', 'n_female']]

    # Results
    print '%d datasets appear to have gender in the column names:' % len(gendered_datasets)
    print [d[0] for d in gendered_datasets]
    print ''
