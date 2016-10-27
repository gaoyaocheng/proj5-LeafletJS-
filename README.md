# proj5-leaflet

## Overview
Make a map application (using LeafletJS or another mapping API) that is initially focused on the on the location of the user
When the user clicks (or taps on a mobile device), application creates a marker at that location. In 'open' state that marker displays the address
Applicaton will also place pins for a configurable set of points of interest (POI) , some restaurants of Eugene.
## Authors 

version by  YaoCheng Gao

## Status

Use mapquest reverse geocoding plugin for leaflet to get the address when user clicks or taps on map
Use leaflet geolocation to get the user location when user initially open the map
to get user location have to use https protocol, so I generate sever ssl certificate ca.crt and myserver.key
for 2 command:
    openssl req -nodes -newkey rsa:2048 -sha256 -keyout myserver.key
    openssl req -new -x509 -key myserver.key -out ca.crt -days 3650
## Access
use https protocol to access the application
URL: https://ip:8000/

## To run automated tests 
* `nosetests`

There are currently nose tests for vocab.py, letterbag.py, and jumble.py. 
now add trie test for trietree.py to nose tests

## To Install and Run
    bash ./configure
    make test    # make all test, should pass 
    make service # service run background




