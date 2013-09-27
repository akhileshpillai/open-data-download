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

def test_socrata_fail():
    nose.tools.assert_raises(ValueError, lambda: standardize.socrata({'id': 'one id'}, 'data.gov.uk', 'different id'))

def test_opendatasoft():
    nonstandard = json.load(open(os.path.join('fixtures', 'dataratp.opendatasoft.com')))['datasets'][0]
    expected = {
        u"uri": u"http://dataratp.opendatasoft.com/explore/dataset/correspondances_stations_lignes_sur_le_reseau_ratp",
        u"portal_software": u"opendatasoft",
        u"portal": u"dataratp.opendatasoft.com",
        u"dataset_id": u"correspondances_stations_lignes_sur_le_reseau_ratp",

        u"title" : u"Correspondances stations/lignes sur le r\xe9seau RATP",
        u"description" : u"<p>\n\tCe fichier permet d\u2019associer les stations et les points d\u2019arr\xeat du r\xe9seau RATP aux lignes qui desservent ces points.Nouveau: Ce fichier inclut le r\xe9seau BUS RATP et ses 12.000 points d'arr\xeats.\n</p>",
        u"keywords": [u'RATP', u'Transport'],

        u"publishing_organization": u"RATP",
        u"source_url":  u"http://data.ratp.fr/fr/les-donnees/fiche-de-jeu-de-donnees/dataset/correspondances-stationslignes-sur-le-reseau-ratp.html",
        u"license": u"ODBL - https://www.data.gouv.fr/Licence-Ouverte-Open-Licence",

        u"columns": [u'station', u'ligne', u'type_ligne'],
    }
    observed = standardize.opendatasoft(nonstandard, u'dataratp.opendatasoft.com', u'correspondances_stations_lignes_sur_le_reseau_ratp')
    del observed['raw_metadata']
    nose.tools.assert_dict_equal(observed, expected)

def test_opendatasoft_fail():
    nose.tools.assert_raises(ValueError, lambda: standardize.opendatasoft({'datasetid': 'one id'}, 'data.gov.uk', 'different id'))

def test_ckan():
    nonstandard = json.load(open(os.path.join('fixtures', 'housing-design-quality-2006')))
    expected = {
        u"uri": u"http://data.gov.uk/dataset/housing-design-quality-2006",
        u"portal_software": u"ckan",
        u"portal": u"data.gov.uk",
        u"dataset_id": u"",

        u"title" : u'Housing design quality in the East Midlands, West Midlands and South West from CABE 2006',
        u"description" : u'An assessment of the design quality of 100 schemes in the East Midlands, West Midlands and South West. The assessment was carried out in 2006. Assessments were based on the Building for Life criteria. Schemes that were eligible for auditing included those that were larger than 20 units in size; completed between January 2003 and August 2006 (the date of the audit); and built by one of the top 10 housebuilders in the region, based on the number of units completed within the same period. Data on each scheme includes scheme name, location, developer, scores for individual Building for Life criteria and total scores. Six out of the 20 criteria which could not be assessed on site are incomplete, due to the poor response to a survey by developers. \r\n',
        u"keywords": [u'building-for-life', u'design', u'housing', u'housing-quality'],

        u"publishing_organization": u"",
        u"source_url":  u"www.cabe.org.uk/publications/housing-audit-2006",
        u"license": u'UK Open Government Licence (OGL)',

        u"columns": [],
    }
    observed = standardize.ckan(nonstandard, u'data.gov.uk', u'housing-design-quality-2006')
    del observed['raw_metadata']
    nose.tools.assert_dict_equal(observed, expected)
