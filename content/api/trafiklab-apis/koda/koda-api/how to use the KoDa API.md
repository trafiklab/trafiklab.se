---
title: "Usage"
date: 2021-07-10
---

# How to use the KoDa API

## Quick Test
To test that the API is live and the server is not down try 
[https://api.koda.trafiklab.se/KoDa/api/v2/hello](https://api.koda.trafiklab.se/KoDa/api/v2/hello)

## Normal Usage

The API has two primary mode of accessing the data the first is to download the GTFS files as the were prresented at Trafiklab at the time of download the other access method is from the Cassandra database

## Request of access keys

An access key is required to gain access to the KoDa API.  The access key is requested thruogh the Samtrafikens and Trafiklabs open data API administrartion web pages. [https://need.correct.url/here](https://https://need.correct.url/here)

## GTFS Real Time file download
The following request to koda.linkoping-ri.se will create and return a tar.bz2 archive for the VehiclePositions feed for Östgötatrafiken for April 02, 2020. 
The archive name is: `otraf-VehiclePositions-2020-04-02.tar.bz2` and it will be stored in the `./otraf/VehiclePositions/2020/04` folder.
If the same request is repeated the stored file will be returned. For the GTFSStatic feed the original file is returned which is a .zip file.

  `wget 'https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-rt/otraf/VehiclePositions?date=2020-04-02&key=aVery53kRETk3Y'`

To request only data for one hour add the `hour` parameter. 
The archive name returned will be: `otraf-VehiclePositions-2020-05-25_12.tar.bz2` 

  `wget 'https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-rt/otraf/VehiclePositions?date=2020-05-25&hour=12&key=aVery53kRETk3Y'`
  
  `wget 'https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-rt/otraf/TripUpdates?date=2020-05-26&hour=12&key=aVery53kRETk3Y'`

Note: curl can be used as well but compression should be turned off as it results in corrupted files.
  
Valid values for feed are:
* VehiclePositions - file format is tar.bz2
* TripUpdates - file format is tar.bz2
* ServiceAlerts - file format is tar.bz2
* GTFSStatic - file format is zip; this is the original file downloaded from the GTFS Regional Static API.

Valid values for company are:
* dintur - Västernorrlands län: Only GTFSStatic
* dt - Dalatrafik
* klt - Kalmar länstrafik
* krono - Kronobergs Länstrafik: Only GTFSStatic
* otraf - Östgötatrafiken
* sj - SJ + Snälltåget + Tågab: Only GTFSStatic
* skane - Skånetrafiken
* sl - Stockholm län: All feeds without VehiclePositions
* ul - Uppsala län
* varm - Värmlandstrafik+Karlstadbuss
* vt - Västtrafik: Only GTFSStatic
* xt - X-trafik

