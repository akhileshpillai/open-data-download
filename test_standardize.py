def test_socrata():
    nonstandard = json.loads('''

    ''')
    expected =
    observed = parse.socrata(nonstandard)
    nose.tools.assert_dict_equal(observed, expected)
