import json, os

import nose.tools
nose.tools.assert_dict_equal.im_class.maxDiff = None

import standardize

def test_socrata():
    nonstandard = json.load(open(os.path.join('fixtures', 'jx86-2vch')))
    expected = {
        u"uri": u"https://data.hawaii.gov/d/jx86-2vch",
        u"portal_software": u"socrata",
        u"portal": u"data.hawaii.gov",
        u"dataset_id": u"jx86-2vch",

        u"name" : u"Libraries State Of Hawaii",
        u"description" : u"Listing of the Public Libraries in the State of Hawaii",
        u"keywords": ["library"],

        u"publishing_organization": u"Hawaii State Public Library System",
        u"source_url":  u"http://hawaii.sdp.sirsi.net/custom/web/",
        u"license": u"Creative Commons Attribution 3.0 Unported",

        u"columns": [u'Library Name', u'County', u'Phone', u'Location 1'],
    }
    observed = standardize.socrata(nonstandard, u'data.hawaii.gov', u'jx86-2vch')
    del observed['raw_metadata']
    nose.tools.assert_dict_equal(observed, expected)
