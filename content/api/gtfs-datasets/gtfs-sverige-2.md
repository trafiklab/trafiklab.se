---
title: GTFS Sverige 2
layout: "single"
weight: 5
aliases:
  - "/api/gtfs-sverige-2"
  - "/api/trafiklab-apis/gtfs-sverige-2/"
  - "/api/trafiklab-apis/gtfs-sverige-2/static-data/"
  - "/api/trafiklab-apis/gtfs-sverige-2/historical-data/"
  - "/api/trafiklab-apis/gtfs-sverige-2/extra-files/"
  - "/api/trafiklab-apis/gtfs-sverige-2/licence/"
---

GTFS Sverige 2 is a GTFS dataset which covers all public transport in Sweden. GTFS Sverige 2 is our national feed. 

## What does this dataset contain?
It contains all public transport in the entire country of Sweden. The data is correct, but lacks the details which are 
included in the GTFS Regional dataset.

### Data format 
The data is in the GTFS format, and makes use of the GTFS Extensions.

### Updates
The static data in this dataset is updated when changes are made, at most one time per day.

### Operators covered by this dataset
All operators which operate in Sweden are covered by GTFS Sverige 2.

### Breaking changes 
This dataset has the **stable** status. This means that we will communicate when fields are added, 
or changed. When breaking changes occur, you will get three months or more to update your implementations.

### Historical data 
The historical data contains information for a period of more than 5 years. It is an excellent 
dataset to analyse evolutions over time.

## Static data
The static _GTFS Sverige 2_ dataset contains files describing all planned public transport data for Sweden. File and field explanations can be found [in the GTFS overview](/api/gtfs-datasets).

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

The dataset can be found
at [https://api.resrobot.se/gtfs/sweden.zip?key={apikey}](https://api.resrobot.se/gtfs/sweden.zip?key={apikey}).

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys)
on how to get one. {{% /note %}}

#### API key levels
<div style="max-width: 270px">

| Level             | Maximum calls per minute | Maximum calls per month |
|:------------------|:------------------------:|:-----------------------:|
| Bronze            |            1             |           50            |
| Temporary upgrade |            2             |           200           |

</div>

## Historical data

Historical GTFS data can be found
at [https://data.samtrafiken.se/trafiklab/gtfs-sverige-2/](https://data.samtrafiken.se/trafiklab/gtfs-sverige-2/).
This archive is updated every time a new GTFS feed is published. The latest version is not available in this
archive, only through the 'usual' API endpoint.

#### Differences between historical systems

Keep in mind that the GTFS Sverige 2 feed has been updated a few times in the time period covered by the archive. This
might affect your data processing when you want to handle data over a timespan of multiple years. There have been
migrations between databases, systems and service providers, for example in 2016. There might be small changes in naming
and data quality between the feeds created by different systems which your analytics need to handle.

#### Example differences

* Up till 2016 stop ids used 7 digits. This was changed to 9 digits by replacing the '74' prefix with '7400'.
* Up till 2016 all trains where grouped in one route per type, this was changed to one route per trip.
* Up till 2016 trains used their type as route name, for example "SJ Intercity". This was changed to the train number,
  for example 7689

## Extra files

Extra files are files which provide additional information about the information in the GTFS files. They are not part of
the GTFS standard, but contain the information which is needed to link the GTFS files to internal operator systems, or
other data which is delivered by the operator. These files can be downloaded without an API key.

### feed\_info.txt

URL: [https://api.resrobot.se/samtrafiken/gtfs/feed\_info.txt](https://api.resrobot.se/samtrafiken/gtfs/feed_info.txt)

This file is included in the GTFS standard, but is also offered as a separate download. This way you can check if the
feed has been updated before downloading it.

### trafikverket\_stops.txt

URL: [https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trafikverket\_stops.txt](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trafikverket_stops.txt)

This file contains a mapping between national stop IDs (rikshållplatser) and Trafikverkets signatures. For example,
CST -&gt; 740000001. Only for train stations.

### agency\_stops.txt

URL: [https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency\_stops.txt](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency_stops.txt)

This file contains a mapping between the operators' local IDs and the national ids (rikshållplatser). For example, the
following mapping means that operator `275` uses the id `41063` for the stop with national id `740066331`.

```xml
agency_id,stop_id,agency_stop_id
275,740066331,41063
```

In the GTFS `agency.txt` file, we find that agency\_id 275 corresponds to SL. In other words, SL uses id `41063` for the
stop with national id `740066331` .

```xml
agency_id,agency_name,agency_url,agency_timezone,agency_lang
275,SL,http://www.sl.se,Europe/Stockholm,sv
```

One or more operators have a local id for each national id. Not every local id corresponds to a national id.

{{% info %}} The local stop id for SL (id 275, Stockholms Lokaltrafik) is used by SL for _Stop-Area_. You
can use SLs API [SL Transport](https://www.trafiklab.se/api/trafiklab-apis/sl/transport) to
translate it to a SiteID used in other SL APIs**.**
{{% /info %}}

### agency\_stops\_&lt;AGENCY\_ID&gt;.txt

URL: [https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency\_stops\_&lt;AGENCY\_ID&gt;.txt](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency_stops_AGENCY_ID.txt?key=YOUR_API_KEY)

This file contains the same information as the agency\_stops.txt file described above, but is already filtered on a
given operator. Replace `<agency_id>` with the operator id of your choice.

### routes\_technical.txt

URL: [https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/routes\_technical.txt](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/routes_technical.txt?key=YOUR_API_KEY)

This file maps route ids to their _technical route number_ used by their operator. A technical route number is unique
within an agency.

### trips\_technical.txt

URL: [https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trips\_technical.txt](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trips_technical.txt?key=YOUR_API_KEY)

This file contains a mapping between trip ids and their corresponding technical trip numbers. The technical trip number
is unique for a route in an agency. In other words, the combination of the 3 values agency\_id, technical\_route\_number
and technical\_trip\_number is unique. Train numbers always have their train number as technical trip number, even if
the train has a public line number (for example Pendeltåg 40 i Stockholm)

## Licence
Data from the GTFS Sverige 2 API is available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

#### Summary

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her
rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by
law.

#### Other Information

In no way are the patent or trademark rights of any person affected by CC0, nor are the rights that other persons may
have in the work or in how the work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with this deed makes no warranties about the work,
and disclaims liability for all uses of the work, to the fullest extent permitted by applicable law.

When using or citing the work, you should not imply endorsement by the author or the affirmer.

{{% info %}}
More information, as well as the complete license text, can be found at
[the creative commons website](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
{{% /info %}} 
