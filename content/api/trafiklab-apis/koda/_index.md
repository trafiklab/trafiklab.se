---
title: KoDa 
layout: "single"
weight: 50 
date: 2021-12-14
---

KoDA, short for Kollektivtrafikens Datalabb is a dataset and API created by RISE and Vinnova in cooperation with
Trafiklab. It aims to provide historic data about public transport, along with tools to learn how to use this data in
combination with machine learning.

## About KoDa

Kollektivtrafikens Datalabb (KoDa) aims to collect, store, and provide a historical open data record of the real time
and static data that is provided by in the Trafiklab.se open data service. The GTFS static and GTFS realtime data from
many Swedish public transportation authorities’ (PTAs) that currently delivered such are stored in a common database and
becomes an open, annotated, dataset for both local and nationwide applications related to public transport.

The KoDa dataset is envisioned to be the base for application areas within the public transport sector, but it can also
be used in other sectors where other actors can create value by analysing public transport data. A platform for
interacting with the dataset has been developed to enable users to work with data analysis and AI development using the
KoDa public transport dataset as the base.

Public transport is not only an independent business that has its challenges,it can also be seen as a sensor in traffic.
The KoDa data can be used by external actors to get information on the current and historical traffic flows of a city
and thereby be able to monitor effects of changes made to the traffic environment. Accessibility and mobility are a
challenge area where more actors need more and better tools to support the transition to a more mobile & sustainable
society. The KoDa data- and toolset can be a used for the development of applications in that field.

More information about KoDa can be found at [the RiSE projekt page (in Swedish)](https://www.ri.se/sv/vad-vi-gor/projekt/koda).

Some example code in python can be found here: [https://github.com/KoDa-project/pykoda](https://github.com/KoDa-project/pykoda).

## What does this dataset contains?

The KoDA API provides raw GTFS and GTFS-RT data downloads, which are organized per operator, feed, and date. The 
datasets provided by the KoDA API contains historic versions of our high quality and detailed GTFS Regional data, both 
static and real-time, going back to February 5th, 2020. 

{{% info %}} **Looking for older data?**

GTFS Sverige 2 contains historical data dating back to 2012.
{{% /info %}}

{{% warning %}} Some data was not available from the start for all operators, therefore there are some feeds that start
at a later date:

- SL VehiclePositions are available from December 1st, 2020. {{% /warning %}}

### Data format

The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the GTFS-Realtime
(GTFS-RT) standard, and is stored in the protobuf format.

### Updates

Data is being stored as soon as it becomes public, and is accessible from the next day.

### Operators covered by this dataset

All operators covered by the GTFS Regional dataset are covered by KoDA.

### Breaking changes

The data in this feed will change according to any changes in the GTFS static or GTFS realtime data.

## Historical data

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

| **API key level** |                                                   **Maximum calls**                                                    |
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