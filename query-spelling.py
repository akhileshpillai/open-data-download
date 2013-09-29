import re

import pandas
import enchant, enchant.tokenize

from standardize import iter_datasets, map_reduce

# datasets = list(iter_datasets())
# columns = list(map_reduce(lambda d: (d['uri'], d['columns']), datasets = datasets))

d = enchant.Dict('en_US')
t = enchant.tokenize.get_tokenizer('en_US')
def mapper(dataset):
    '''
    Args:
        dataset: A dictionary of dataset metadata
    Returns:
        An iterator yielding a tuple of (uri, column name, word) for
        each missspelled word in the name or description columns
    '''
    for column in ['title', 'description']:
        for pair in t(dataset[column]):
            if not d.check(pair[0]):
                yield (dataset['uri'], column, pair[0])

def reducer(a, b):
    '''
    Args:
        a: A dict of uri -> number of misspellings
        b: a tuple of (uri, column name, misspelling)
    '''
