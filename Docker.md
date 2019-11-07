## Test with Docker

This project has two [docker](https://docs.docker.com/) containers to help you generate the mapfile and view the created WMS.

```
docker-compose up
```

And open the capabilities: http://localhost/cgi-bin/mapserv?map=/app/osm-default.map&REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0

You will need to execute some command to import OSM data and create a mapfile. After this you can view your map in eg qgis.

### import data

Download a bpf file to the data dir and import


```
docker-compose exec postgis bash 
cd data
wget  https://download.bbbike.org/osm/bbbike/Amsterdam/Amsterdam.osm.pbf
imposm import -connection postgis://osm:osm@localhost/osm -read /app/data/Amsterdam.osm.pbf -mapping /app/imposm3-mapping.json -write -overwritecache -optimize   
imposm import -mapping /app/imposm3-mapping.json -connection postgis://osm:osm@localhost/osm -deployproduction

```


### Generate mapfile & download shapefiles

```
docker-compose exec webserver bash
make --always-make -f docker.mk #repeat to regenerate
STYLE=bing make --always-make -f docker.mk 
cd data
make 
```