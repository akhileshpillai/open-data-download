import json, os

import nose.tools
nose.tools.assert_dict_equal.im_class.maxDiff = None

import standardize

def test_socrata():
    nonstandard = json.load(open(os.path.join('fixtures', 'jx86-2vch')))
    expected = {
        "uri": "https://data.hawaii.gov/d/jx86-2vch",
        "portal_software": "socrata",
        "portal": "data.hawaii.gov",
        "dataset_id": "jx86-2vch",

        "name" : "Libraries State Of Hawaii",
        "description" : "Listing of the Public Libraries in the State of Hawaii",
        "keywords": ["library"],

        "publishing_organization": "Hawaii State Public Library System",
        "source_url":  "http://hawaii.sdp.sirsi.net/custom/web/",
        "license": "Creative Commons Attribution 3.0 Unported",

        "columns": [],
    }
    observed = standardize.socrata(nonstandard)
    del observed['raw_metadata']
    nose.tools.assert_dict_equal(observed, expected)
