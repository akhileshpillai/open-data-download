def test_socrata():
    nonstandard = json.loads('''

{
  "id" : "jx86-2vch",
  "name" : "Libraries State Of Hawaii",
  "attribution" : "Hawaii State Public Library System",
  "attributionLink" : "http://hawaii.sdp.sirsi.net/custom/web/",
  "averageRating" : 0,
  "category" : "Social Services",
  "createdAt" : 1340753242,
  "description" : "Listing of the Public Libraries in the State of Hawaii",
  "displayType" : "table",
  "downloadCount" : 39,
  "licenseId" : "CC_30_BY",
  "numberOfComments" : 0,
  "oid" : 800553,
  "publicationAppendEnabled" : false,
  "publicationDate" : 1340760809,
  "publicationGroup" : 368596,
  "publicationStage" : "published",
  "rowClass" : "",
  "rowsUpdatedAt" : 1340760761,
  "rowsUpdatedBy" : "a5cm-ukuw",
  "signed" : false,
  "tableId" : 368658,
  "totalTimesRated" : 0,
  "viewCount" : 121,
  "viewLastModified" : 1346795848,
  "viewType" : "tabular",
  "columns" : [ {
    "id" : 11832075,
    "name" : "Library Name",
    "dataTypeName" : "text",
    "fieldName" : "library_name",
    "position" : 2,
    "renderTypeName" : "text",
    "tableColumnId" : 3285776,
    "width" : 244,
    "cachedContents" : {
      "non_null" : 55,
      "smallest" : "AIEA PUBLIC LIBRARY",
      "null" : 0,
      "largest" : "WAIPAHU PUBLIC LIBRARY",
      "top" : [ {
        "count" : 20,
        "item" : "PEARL CITY PUBLIC LIBRARY"
      }, {
        "count" : 19,
        "item" : "PEARL CITY PUBLIC LIBRARY (BOOKMOBILE SERV)"
      }, {
        "count" : 18,
        "item" : "PRINCEVILLE PUBLIC LIBRARY"
      }, {
        "count" : 17,
        "item" : "SALT LAKE PUBLIC LIBRARY"
      }, {
        "count" : 16,
        "item" : "THELMA PARKER MEMORIAL PUBLIC AND SCHOOL LIBR"
      }, {
        "count" : 15,
        "item" : "WAHIAWA PUBLIC LIBRARY"
      }, {
        "count" : 14,
        "item" : "WAIALUA PUBLIC LIBRARY"
      }, {
        "count" : 13,
        "item" : "WAIANAE PUBLIC LIBRARY"
      }, {
        "count" : 12,
        "item" : "WAIKIKI PUBLIC LIBRARY"
      }, {
        "count" : 11,
        "item" : "WAILUKU PUBLIC LIBRARY"
      }, {
        "count" : 10,
        "item" : "WAILUKU PUBLIC LIBRARY (BOOKMOBILE SERV)"
      }, {
        "count" : 9,
        "item" : "WAIMANALO PUBLIC AND SCHOOL LIBRARY"
      }, {
        "count" : 8,
        "item" : "WAIMEA PUBLIC LIBRARY"
      }, {
        "count" : 7,
        "item" : "WAIPAHU PUBLIC LIBRARY"
      } ]
    },
    "format" : {
    }
  }, {
    "id" : 11832076,
    "name" : "County",
    "dataTypeName" : "text",
    "fieldName" : "county",
    "position" : 3,
    "renderTypeName" : "text",
    "tableColumnId" : 3285777,
    "width" : 172,
    "cachedContents" : {
      "non_null" : 55,
      "smallest" : "HAWAII",
      "null" : 0,
      "largest" : "MAUI",
      "top" : [ {
        "count" : 20,
        "item" : "HONOLULU"
      }, {
        "count" : 19,
        "item" : "MAUI"
      }, {
        "count" : 18,
        "item" : "KAUAI"
      }, {
        "count" : 17,
        "item" : "HAWAII"
      }, {
        "count" : 16,
        "item" : "KAPOLEI"
      } ]
    },
    "format" : {
    }
  }, {
    "id" : 11832077,
    "name" : "Phone",
    "dataTypeName" : "number",
    "fieldName" : "phone",
    "position" : 4,
    "renderTypeName" : "number",
    "tableColumnId" : 3285778,
    "width" : 160,
    "cachedContents" : {
      "non_null" : 55,
      "smallest" : "8082335676",
      "sum" : "444743354622",
      "null" : 0,
      "average" : "8086242811.309091",
      "largest" : "8089880459",
      "top" : [ {
        "count" : 20,
        "item" : "8083274327"
      }, {
        "count" : 19,
        "item" : "8085535483"
      }, {
        "count" : 18,
        "item" : "8084536566"
      }, {
        "count" : 17,
        "item" : "8088316831"
      }, {
        "count" : 16,
        "item" : "8088876067"
      }, {
        "count" : 15,
        "item" : "8086226345"
      }, {
        "count" : 14,
        "item" : "8086374876"
      }, {
        "count" : 13,
        "item" : "8086964257"
      }, {
        "count" : 12,
        "item" : "8087338488"
      }, {
        "count" : 11,
        "item" : "8082435766"
      }, {
        "count" : 10,
        "item" : "8082599925"
      }, {
        "count" : 9,
        "item" : "8083386848"
      }, {
        "count" : 8,
        "item" : "8086750358"
      } ]
    },
    "format" : {
      "precisionStyle" : "standard",
      "precision" : "0",
      "noCommas" : "true",
      "align" : "right",
      "mask" : "### ### ####"
    }
  }, {
    "id" : 11832078,
    "name" : "Location 1",
    "dataTypeName" : "location",
    "fieldName" : "location_1",
    "position" : 5,
    "renderTypeName" : "location",
    "tableColumnId" : 3285779,
    "width" : 220,
    "cachedContents" : {
      "non_null" : 55,
      "smallest" : {
        "longitude" : "-158.0795862200091",
        "latitude" : "21.334475140598556",
        "human_address" : "{\"address\":\"1020 MANAWAI ST.\",\"city\":\"KAPOLEI\",\"state\":\"HI\",\"zip\":\"96707\"}"
      },
      "null" : 0,
      "largest" : {
        "longitude" : "-156.91995999975404",
        "latitude" : "20.826880000211986",
        "human_address" : "{\"address\":\"P.O.BOX 550\",\"city\":\"LANAI CITY\",\"state\":\"HI\",\"zip\":\"96763\"}"
      },
      "top" : [ {
        "count" : 20,
        "item" : {
          "longitude" : "-157.96932780118144",
          "latitude" : "21.396231125890772",
          "human_address" : "{\"address\":\"1138 WAIMANO HOME RD.\",\"city\":\"PEARL CITY\",\"state\":\"HI\",\"zip\":\"96782\"}"
        }
      }, {
        "count" : 19,
        "item" : {
          "longitude" : "-157.96932780118144",
          "latitude" : "21.396231125890772",
          "human_address" : "{\"address\":\"1138 WAIMANO HOME ROAD\",\"city\":\"PEARL CITY\",\"state\":\"HI\",\"zip\":\"96782\"}"
        }
      }, {
        "count" : 18,
        "item" : {
          "longitude" : "-159.47221345506117",
          "latitude" : "22.21472300641227",
          "human_address" : "{\"address\":\"4343 EMMALANI DRIVE\",\"city\":\"PRINCEVILLE\",\"state\":\"HI\",\"zip\":\"96722\"}"
        }
      }, {
        "count" : 17,
        "item" : {
          "longitude" : "-157.91304976662335",
          "latitude" : "21.344754391393508",
          "human_address" : "{\"address\":\"848 ALA LILIKOI ST.\",\"city\":\"HONOLULU\",\"state\":\"HI\",\"zip\":\"96818\"}"
        }
      }, {
        "count" : 16,
        "item" : {
          "longitude" : "-155.66926496402888",
          "latitude" : "20.020065885779587",
          "human_address" : "{\"address\":\"67-1209 MAMALAHOA HIGHWAY\",\"city\":\"KAMUELA\",\"state\":\"HI\",\"zip\":\"96743\"}"
        }
      }, {
        "count" : 15,
        "item" : {
          "longitude" : "-158.02624743045132",
          "latitude" : "21.49737833298599",
          "human_address" : "{\"address\":\"820 CALIFORNIA AVE.\",\"city\":\"WAHIAWA\",\"state\":\"HI\",\"zip\":\"96786\"}"
        }
      }, {
        "count" : 14,
        "item" : {
          "longitude" : "-158.1226631344713",
          "latitude" : "21.57386806582214",
          "human_address" : "{\"address\":\"67-068 KEALOHAUNI ST.\",\"city\":\"WAIALUA\",\"state\":\"HI\",\"zip\":\"96791\"}"
        }
      }, {
        "count" : 13,
        "item" : {
          "longitude" : "-158.19192952790928",
          "latitude" : "21.45047868915799",
          "human_address" : "{\"address\":\"85-625 FARRINGTON HWY.\",\"city\":\"WAIANAE\",\"state\":\"HI\",\"zip\":\"96792\"}"
        }
      }, {
        "count" : 12,
        "item" : {
          "longitude" : "-157.8162377501692",
          "latitude" : "21.274112645991977",
          "human_address" : "{\"address\":\"400 KAPAHULU AVE.\",\"city\":\"HONOLULU\",\"state\":\"HI\",\"zip\":\"96815\"}"
        }
      }, {
        "count" : 11,
        "item" : {
          "longitude" : "-156.50467549585838",
          "latitude" : "20.885056942896483",
          "human_address" : "{\"address\":\"251 HIGH ST.\",\"city\":\"WAILUKU\",\"state\":\"HI\",\"zip\":\"96793\"}"
        }
      }, {
        "count" : 10,
        "item" : {
          "longitude" : "-156.50467549585838",
          "latitude" : "20.885056942896483",
          "human_address" : "{\"address\":\"251 HIGH STREET\",\"city\":\"WAILUKU\",\"state\":\"HI\",\"zip\":\"96793\"}"
        }
      }, {
        "count" : 9,
        "item" : {
          "longitude" : "-157.71560293714333",
          "latitude" : "21.34697840938136",
          "human_address" : "{\"address\":\"41-1320 KALANIANAOLE HWY.\",\"city\":\"WAIMANALO\",\"state\":\"HI\",\"zip\":\"96795\"}"
        }
      }, {
        "count" : 8,
        "item" : {
          "longitude" : "-159.66636000001384",
          "latitude" : "21.954859999589473",
          "human_address" : "{\"address\":\"P.O. BOX 397\",\"city\":\"WAIMEA\",\"state\":\"HI\",\"zip\":\"96796\"}"
        }
      }, {
        "count" : 7,
        "item" : {
          "longitude" : "-158.00307190175627",
          "latitude" : "21.38539475389757",
          "human_address" : "{\"address\":\"94-275 MOKUOLA STREET.\",\"city\":\"WAIPAHU\",\"state\":\"HI\",\"zip\":\"96797\"}"
        }
      } ]
    },
    "format" : {
    },
    "subColumnTypes" : [ "human_address", "latitude", "longitude", "machine_address", "needs_recoding" ]
  } ],
  "grants" : [ {
    "inherited" : false,
    "type" : "viewer",
    "flags" : [ "public" ]
  } ],
  "license" : {
    "name" : "Creative Commons Attribution 3.0 Unported",
    "logoUrl" : "images/licenses/cc30by.png",
    "termsLink" : "http://creativecommons.org/licenses/by/3.0/legalcode"
  },
  "metadata" : {
    "custom_fields" : {
      "Hawaii Line of Business" : {
        "Division name" : "Hawaii State Public Library System",
        "Division shortname, acronym" : "HSPLS",
        "Department Agency short name, acronym" : "DOE",
        "State of Hawaii Data Book Category" : "Education",
        "Department/Agency" : "Education",
        "Line of Business" : "Education"
      },
      "Data Reference" : {
        "Period of Coverage" : "",
        "Records Reporting System RSN" : "20244",
        "Date Updated" : "2002",
        "Date Released" : "2002",
        "Reference for Technical Information" : "",
        "Frequency" : "",
        "Unit of Analysis" : "",
        "Data dictionary/variable list" : ""
      }
    },
    "renderTypeConfig" : {
      "visible" : {
        "table" : true
      }
    },
    "availableDisplayTypes" : [ "table", "fatrow", "page" ],
    "rdfSubject" : "0",
    "rowIdentifier" : "0",
    "rdfClass" : ""
  },
  "owner" : {
    "id" : "4hgi-fxu8",
    "displayName" : "Paola Saibene",
    "emailUnsubscribed" : false,
    "privacyControl" : "login",
    "profileLastModified" : 1375144359,
    "screenName" : "Paola Saibene"
  },
  "query" : {
  },
  "rights" : [ "read" ],
  "tableAuthor" : {
    "id" : "a5cm-ukuw",
    "displayName" : "OIMT Open Data Coordinator",
    "emailUnsubscribed" : false,
    "privacyControl" : "login",
    "profileImageUrlLarge" : "/images/profile/9184/3960/oimt_logo_only_large.PNG",
    "profileImageUrlMedium" : "/images/profile/9184/3960/oimt_logo_only_thumb.PNG",
    "profileImageUrlSmall" : "/images/profile/9184/3960/oimt_logo_only_tiny.PNG",
    "profileLastModified" : 1373654005,
    "roleName" : "administrator",
    "screenName" : "OIMT Open Data Coordinator",
    "rights" : [ "create_datasets", "edit_others_datasets", "edit_sdp", "edit_site_theme", "moderate_comments", "manage_users", "chown_datasets", "edit_nominations", "approve_nominations", "feature_items", "federations", "manage_stories", "manage_approval", "change_configurations", "view_domain", "view_others_datasets", "edit_pages", "create_pages", "view_goals", "view_dashboards", "edit_goals", "edit_dashboards", "create_dashboards" ]
  },
  "tags" : [ "library" ],
  "flags" : [ "default" ]
}
    ''')



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
    observed = parse.socrata(nonstandard)
    del observed['raw_metadata']
    nose.tools.assert_dict_equal(observed, expected)
