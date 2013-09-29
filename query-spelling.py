import re

import pandas
import lxml.html
import enchant, enchant.tokenize

from standardize import iter_datasets, map_reduce

not_english = {
    'parisdata.opendatasoft.com': 'fr_FR',
    'dati.lombardia.it': 'it_IT',
}

def mapper(dataset):
    '''
    Args:
        dataset: A dictionary of dataset metadata
    Returns:
        An iterator yielding a tuple of (uri, column name, word) for
        each missspelled word in the name or description columns
    '''
    language = not_english[dataset['portal']] if dataset['portal'] in not_english else 'en_US'
    d = enchant.Dict(language)
    t = enchant.tokenize.get_tokenizer('en_US')

    for column in ['title', 'description']:
        text = dataset[column]

        if text == None:
            continue

        if column == 'description':
            try:
                text = lxml.html.fromstring(text).text_content()
            except:
                pass

        for pair in t(text):
            if not d.check(pair[0]):
                yield (dataset['portal'], dataset['uri'], column, pair[0])

def reducer(a, b):
    '''
    Args:
        a: A dict of uri -> number of misspellings
        b: a tuple of (uri, column name, misspelling)
    '''

# datasets = list(iter_datasets())
def query(datasets):
    open_portals = {'datahub.io', 'opendata.socrata.com', 'datastore.opendatasoft.com'}
    official = [dataset for dataset in datasets if dataset['portal'] not in open_portals]
    mr = map_reduce(mapper, datasets = datasets)
    rows = []
    for item in mr:
        rows += list(item)
    return pandas.DataFrame(rows, columns = ['portal', 'uri', 'column', 'word'])
