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

        u"title" : u"Libraries State Of Hawaii",
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

def test_opendatasoft():
    nonstandard = json.load(open(os.path.join('fixtures', 'dataratp.opendatasoft.com')))['datasets'][0]
    expected = {
        u"uri": u"https://dataratp.opendatasoft.com/explore/dataset/",
        u"portal_software": u"opendatasoft",
        u"portal": u"dataratp.opendatasoft.com",
        u"dataset_id": u"correspondances_stations_lignes_sur_le_reseau_ratp",

        u"title" : u"Correspondances stations/lignes sur le r\xe9seau RATP",
        u"description" : u"<p>\n\tCe fichier permet d\u2019associer les stations et les points d\u2019arr\xeat du r\xe9seau RATP aux lignes qui desservent ces points.Nouveau: Ce fichier inclut le r\xe9seau BUS RATP et ses 12.000 points d'arr\xeats.\n</p>"
        u"keywords": [u'RATP', u'Transport'],

        u"publishing_organization": u"RATP",
        u"source_url":  u"http://data.ratp.fr/fr/les-donnees/fiche-de-jeu-de-donnees/dataset/correspondances-stationslignes-sur-le-reseau-ratp.html",
        u"license": u"ODBL - https://www.data.gouv.fr/Licence-Ouverte-Open-Licence",

        u"columns": [],
    }
    del observed['raw_metadata']
    nose.tools.assert_dict_equal(observed, expected)
