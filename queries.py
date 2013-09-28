from standardize import map_reduce

columns = map_reduce(lambda d: d['uri'], d['columns'])
