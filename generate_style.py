#!/usr/bin/env python
from styles.default import vars
import sys
from optparse import OptionParser


styles = {
    'default': {},
    'outlined': {
        'display_motorway_outline': {
            0: 0,
            7: 1
        },
        'motorway_ol_width': {
            0: 0.5,
            10: 1
        },
        'motorway_ol_clr': '0 0 0',
        'display_trunk_outline': {
            0: 0,
            7: 1,
        },
        'trunk_ol_width': {
            0: 0.5,
            10: 1
        },
        'trunk_ol_clr': '0 0 0',
        'display_primary_outline': {
            0: 0,
            9: 1
        },
        'primary_ol_width': {
            0: 0.5,
            11: 1
        },
        'primary_ol_clr': '0 0 0',
        'display_secondary_outline': {
            0: 0,
            10: 1
        },
        'secondary_ol_width': {
            0: 0.5,
            13: 1
        },
        'secondary_ol_clr': '0 0 0',
        'display_tertiary_outline': {
            0: 0,
            12: 1
        },
        'tertiary_ol_width': {
            0: 0.5,
            15: 1
        },
        'tertiary_ol_clr': '0 0 0',
        'display_other_outline': {
            0: 0,
            14: 1
        },
        'other_width': {
            0: 0,
            11: 0.5,
            14: 2.5,
            15: 4,
            16: 6,
        },
        'other_ol_width': {
            0: 0.5,
            17: 1
        },
        'other_ol_clr': '0 0 0',
        'display_pedestrian_outline': {
            0: 0,
            13: 1
        },
        'pedestrian_ol_width': {
            0: 0.5,
            17: 1
        },
        'pedestrian_ol_clr': '0 0 0',
    },
    'centerlined': {
        'display_motorway_centerline': {
            0: 0,
            10: 1
        },
        'motorway_centerline_clr': {
            0: '255 253 139'
        },
        'motorway_centerline_width': {
            0: 1,
            12: 1.5,
            14: 2
        },
        'display_trunk_centerline': {
            0: 0,
            10: 1
        },
        'trunk_centerline_clr': {
            0: '255 255 255'
        },
        'trunk_centerline_width': {
            0: 1,
            12: 1.5,
            14: 2
        }
    },
    'google': {
        'motorway_clr': "253 146 58",
        'trunk_clr': "255 195 69",
        'primary_clr': {
            0: '193 181 157',
            9: "255 253 139"
        },
        'secondary_clr': {
            0: '193 181 157',
            10: "255 253 139"
        },
        'tertiary_clr': {
            0: '193 181 157',
            12: "255 253 139"
        },
        'other_clr': {
            0: '193 181 157',
            14: "255 255 255"
        },
        'pedestrian_clr': '250 250 245',
        'forest_clr': "203 216 195",
        'industrial_clr': "209 208 205",
        'education_clr': "222 210 172",
        'hospital_clr': "229 198 195",
        'residential_clr': "242 239 233",
        'land_clr': "242 239 233",
        'park_clr': '181 210 156',
        'ocean_clr': '153 179 204',
        'waterarea_clr': '153 179 204',
        'river_clr': '153 179 204',
        'stream_clr': '153 179 204',
        'canal_clr': '153 179 204',

        'motorway_ol_clr': '186 110 39',
        'trunk_ol_clr': '221 159 17',
        'primary_ol_clr': '193 181 157',
        'secondary_ol_clr': '193 181 157',
        'tertiary_ol_clr': '193 181 157',
        'other_ol_clr': '193 181 157',
        'pedestrian_ol_clr': '193 181 157',
        'display_buildings': 0
    },
    'michelin': {
        'motorway_clr': '228 24 24',
        'trunk_clr': '228 24 24',
        'primary_clr': {
            0: '"#aaaaaa"',
            9: '228 24 24'
        },
        'secondary_clr': {
            0: '"#aaaaaa"',
            10: '252 241 20'
        },
        'tertiary_clr': {
            0: '"#aaaaaa"',
            12: '252 241 20'
        },
        'other_clr': {
            0: '"#aaaaaa"',
            13: '"#ffffff"'
        },
        'display_primary_outline': {
            0: 0,
            11: 1
        },
        'display_secondary_outline': {
            0: 0,
            12: 1
        },
        'display_tertiary_outline': {
            0: 0,
            13: 1
        },
        'display_other_outline': {
            0: 0,
            14: 1
        },

        'motorway_ol_width': 0.5,
        'trunk_ol_width': 0.5,
        'primary_ol_width': 0.2,
        'secondary_ol_width': 0.2,
        'tertiary_ol_width': 0.2,
        'other_ol_width': 0.2,

        'pedestrian_clr': '"#fafaf5"',
        'forest_clr': '188 220 180',
        'industrial_clr': '"#ebe5d9"',
        'education_clr': '"#ded1ab"',
        'hospital_clr': '"#e6c8c3"',
        'residential_clr': '255 234 206',
        'land_clr': '"#ffffff"',
        'park_clr': '"#dcdcb4"',
        'ocean_clr': '172 220 244',
        'waterarea_clr': '172 220 244',
        'river_clr': '172 220 244',
        'stream_clr': '172 220 244',
        'canal_clr': '172 220 244',

        'motorway_ol_clr': '0 0 0',
        'trunk_ol_clr': '0 0 0',
        'primary_ol_clr': '0 0 0',
        'secondary_ol_clr': '0 0 0',
        'tertiary_ol_clr': '0 0 0',
        'other_ol_clr': '0 0 0',
        'pedestrian_ol_clr': '0 0 0',
        'footway_clr': '"#7f7f7f"'
    },
    'bing': {
        'motorway_clr': '"#BAC3A8"',
        'trunk_clr': '"#F2935D"',
        'primary_clr': {
            0: '"#aaaaaa"',
            9: '"#FEF483"'
        },
        'secondary_clr': {
            0: '"#aaaaaa"',
            10: '"#FCFCCC"'
        },
        'tertiary_clr': {
            0: '"#aaaaaa"',
            12: '"#ffffff"'
        },
        'other_clr': {
            0: '"#aaaaaa"',
            13: '"#ffffff"'
        },
        'pedestrian_clr': '"#fafaf5"',
        'forest_clr': '"#dcdcb4"',
        'industrial_clr': '"#ebe5d9"',
        'education_clr': '"#ded1ab"',
        'hospital_clr': '"#e6c8c3"',
        'residential_clr': '"#f6f1e6"',
        'land_clr': '"#f6f1e6"',
        'park_clr': '"#dcdcb4"',
        'ocean_clr': '"#b3c6d4"',
        'waterarea_clr': '"#b3c6d4"',
        'river_clr': '"#b3c6d4"',
        'stream_clr': '"#b3c6d4"',
        'canal_clr': '"#b3c6d4"',

        'motorway_ol_clr': '"#39780f"',
        'trunk_ol_clr': '"#bf6219"',
        'primary_ol_clr': '"#d17f40"',
        'secondary_ol_clr': '"#bbb8b4"',
        'tertiary_ol_clr': '"#b7ac9a"',
        'other_ol_clr': '"#b7ac9a"',
        'pedestrian_ol_clr': '193 181 157',
        'footway_clr': '"#7f7f7f"'
    },
    'osm2pgsql': {
        'waterarea_data': {
            0: '"way from (select way,osm_id , OSM_NAME_COLUMN as name, waterway as type from OSM_PREFIX_polygon where \\\"natural\\\"=\'water\' or landuse=\'basin\' or landuse=\'reservoir\' or waterway=\'riverbank\') as foo using unique osm_id using srid=OSM_SRID"'
        },
        'waterways_data': {
            0: '"way from (select way,waterway as type,osm_id, OSM_NAME_COLUMN as name from OSM_PREFIX_line where waterway IN (\'river\', \'stream\', \'canal\')) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'places_data': {
            0: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'country\',\'continent\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            3: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'country\',\'continent\',\'city\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            8: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'city\',\'town\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            11: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'city\',\'town\',\'village\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
            13: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place is not NULL and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
        },
        'railways_data': {
            0: '"way from (select way, osm_id, tunnel, railway as type from OSM_PREFIX_line where railway=\'rail\') as foo using unique osm_id using srid=OSM_SRID"'
        },
        'landusage_data': {
            0: '"way from (select way, osm_id, name, type from (select way, st_area(way) as area, osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'residential\')\
         order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
            6: '"way from (select way, osm_id, name, type from (select way , st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'industrial\',\'commercial\',\'residential\')\
         order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
            9: '"way from (select way, osm_id, name, type from (select way, st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
         \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
         \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
         \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
            12: '"way from (select way, osm_id, name, type from (select way , st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
         \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
         \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
         \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"'
        },
        'roads_data': {
            0: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            8: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            9: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\',\'secondary\',\'motorway_link\',\'trunk_link\',\'primary_link\')order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            10: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\',\'secondary\',\'tertiary\',\'motorway_link\',\'trunk_link\',\'primary_link\',\'secondary_link\',\'tertiary_link\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            11: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway is not null order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
            14: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway||(case when bridge=\'yes\' then 1 else 0 end)||(case when tunnel=\'yes\' then 1 else 0 end) as type from OSM_PREFIX_line where highway is not null order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
        },

    }
}


# these are the preconfigured styles that can be called when creating the final mapfile,
# e.g. with `make STYLE=google`. This will create an osm-google.map mapfile
style_aliases = {

    # map with no road casing and few colors, suited for using as a basemap when overlaying
    # other layers without risk of confusion between layers.
    "default": "default",

    # a style resembling the google-maps theme
    "google": "default,outlined,google",

    # same style as above, but using data coming from an osm2pgsql schema rather than imposm
    "googleosm2pgsql": "default,outlined,google,osm2pgsql",
    "bing": "default,outlined,bing",
    "michelin": "default,outlined,centerlined,michelin"
}


parser = OptionParser()
parser.add_option("-l", "--level", dest="level", type="int", action="store", default=-1,
                  help="generate file for level n")
parser.add_option("-g", "--global", dest="full", action="store_true", default=False,
                  help="generate global include file")
parser.add_option("-s", "--style",
                  action="store", dest="style", default="default",
                  help="comma separated list of styles to apply (order is important)")

(options, args) = parser.parse_args()

items = vars.items()
for namedstyle in style_aliases[options.style].split(','):
    items = items + styles[namedstyle].items()

style = dict(items)

if options.full:
    print "###### level 0 ######"
    for k, v in style.iteritems():
        if type(v) is dict:
            print "#define _%s0 %s" % (k, v[0])
        else:
            print "#define _%s0 %s" % (k, v)

    for i in range(1, 19):
        print
        print "###### level %d ######" % (i)
        for k, v in style.iteritems():
            if type(v) is dict:
                if not v.has_key(i):
                    print "#define _%s%d _%s%d" % (k, i, k, i-1)
                else:
                    print "#define _%s%d %s" % (k, i, v[i])
            else:
                print "#define _%s%d %s" % (k, i, v)

if options.level != -1:
    level = options.level
    for k, v in style.iteritems():
        print "#undef _%s" % (k)

    for k, v in style.iteritems():
        print "#define _%s _%s%s" % (k, k, level)
