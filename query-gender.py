from standardize import iter_datasets, map_reduce

# load the data into memory
datasets = list(iter_datasets())

# Sexist datasets
def gendered(pair):
    uri, column_names = pair
    columns_blob = ' ' + ' '.join(column_names).lower().replace('_', ' ') + ' '
    return ' men ' in columns_blob or ' man ' in columns_blob or ' male ' in columns_blob

columns = list(map_reduce(lambda d: (d['uri'], d['columns']), datasets = datasets))
gendered_datasets = filter(gendered, columns)

print '%d datasets appear to have gender in the column names:' % len(gendered_datasets)
print [d[0] for d in gendered_datasets]
print ''
