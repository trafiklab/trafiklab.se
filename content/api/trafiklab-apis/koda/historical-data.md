---
title: Historical data 
weight: 200 
date: 2021-12-14
---

The _KoDa API_ provides downloads for both static and realtime historical data.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS and GTFS-RT documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

Static historical data can be found
at https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-static/{operator}?date={date}&key={api_key}
Realtime historical data can be found
at https://api.koda.trafiklab.se/KoDa/api/v2/gtfs-rt/{operator}/{feed}?date={date}&key={api_key}

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [HERE](/docs/using-trafiklab/getting-api-keys) 
on how to get it. `{operator}` should be one of the operator abbreviations as used in the GTFS Regional API. `{feed}` 
can be `ServiceAlerts`, `TripUpdates` or `VehiclePositions`. `Date` is the date for which you want to download the data, 
in `YYYY-MM-DD` format.

Additionally, you can pass the `hour=[00-23]` parameter to the realtime data endpoint to obtain data for a specific
hour. {{% /note %}}

| **API key level** |                                                       **Calls**                                                        |
|:-----------------:|:----------------------------------------------------------------------------------------------------------------------:|
|      General      | No limit but we ask our users to spread out their downloads by not downloading more than 2 or 3 files at the same time |

{{% page-ref "koda-api-specification.md" %}}

## Using the downloaded static data

The static data is exactly like a GTFS file you would download through the GTFS Regional API.

## Using the downloaded realtime data

The downloaded data is compressed using 7-zip. This format has been chosen because it provides solid compression while
also being fast to decompress. You can open these files using a variety of (command line) programs and libraries:

- 7-zip for Windows: https://www.7-zip.org/
- p7zip for Linux systems using APT package manager: `apt-get install p7zip-full`, usable through the `7z` command after
  installation.
- p7zip for Linux systems using yum package manager: `yum install p7zip`, usable through the `7z` command after
  installation.

Each archive contains a directory structure before the actual data. Because of this, you can extract multiple archives
into the same folder without overwriting or mixing files from different archives.

Each protobuf file has a filename containing the registration date/time. This is however only a convenience. Use the
timetamp contained in the protobuf file to get time of the original publication.

### Waiting for data archives to be created

7-zip archives are not created automatically, but are instead created on-demand. The file will be created upon the first
request. This request, and all other requests for the file will it's being created, will receive an `HTTP 202 Accepted`
response. If you receive this response, you can poll the URL every 30 seconds until you receive an `HTTP 200` response
along with the actual data. If someone else already requested the file earlier, you might be able to download the file
immediately.

Depending on the amount of data, creation of an archive can take between 1 and 60 minutes. If you need large amounts of
data, you can test a few dates to see if the data has been created already. Alternatively, you could run a small script
that sends HTTP HEAD requests to create all the files without actually downloading them. Such a script could test a URL
and wait until it receives an HTTP 200 response code for that URL, then move on to the next file. This way, all files
would be ready to download by the time you actually need the data.

{{% info %}} We are in the process of triggering every file automatically, to make all files available directly. This
means you might not encounter `HTTP 202` accepted responses for certain operators, feeds and/or dates. You should
however keep the possibility of this response code in mind while developing applications. {{% /info %}}

{{% warning %}} Starting more than 2 tasks simultaneously can have a negative impact on the time it takes to create the
files. Therefore, we recommend users who need a large number of files to only create two or three tasks at once, and to
not request all files at once. {{% /warning %}}