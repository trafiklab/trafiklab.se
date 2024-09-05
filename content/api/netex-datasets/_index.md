---
title: NeTEx Datasets
weight: 2
layout: "single"
sidebar: true
image: '/media/2024/09/banner_building.jpg'
cascade:
  - image: '/media/2024/09/banner_building.jpg'
---

## NeTEx at Trafiklab

At Trafiklab, we offer three different NeTEx datasets. NeTEx regional and NeTEx Sweden offer the same coverage as
GTFS regional and GTFS Sweden, which is not full coverage. If you are looking for 100% coverage we recommend
GTFS Sverige 2, which is much less detailed but does contain all the public transport data of Sweden.

Our three datasets:

[**NeTEx Regional**](/api/netex-datasets/netex-regional/) which consists of multiple NeTEx feeds, each feed containing data
  for a specific region or operator. This data contains all details present in GTFS Regional, as well as additional data
  which can't be represented in GTFS. Both static and real-time data available.

[**NeTEx Sweden**](/api/netex-datasets/netex-sweden/) which is an aggregated dataset of all the different datasets in
  NeTEx Regional as a single feed. The feed contains all data present in GTFS Sweden, as well as additional data which
  can't be represented in GTFS. Realtime SIRI data is not available for the aggregated static NeTEx data.

[**Stops data**](/api/netex-datasets/stops-data/) which is an API that contains detailed data of Sweden's national stops
  and their mappings to stops from the [GTFS Regional](/api/gtfs-datasets/gtfs-regional/)
  and [Netex Regional](/api/netex-datasets/netex-regional/) APIs. This dataset contains all of
  Sweden's stops in the NeTEx format.

You can see the general difference between GTFS Regional and NeTEx Regional data below.
<div class="wide">

|                          | GTFS Regional/ GTFS Sweden 3                                       | NeTEx Regional/ NeTEx Sweden                                           |
|:-------------------------|:-------------------------------------------------------------------|:-----------------------------------------------------------------------|
| Coverage                 | 92%                                                                | 92%                                                                    |
| Data quality             | High quality, based on higher level of details than GTFS Sverige 2 | Highest quality, based on higher level of details than GTFS Regional   |
| Real-time data           | Static + Real-time + GPS positions                                 | Static + Real-time + GPS positions / only static data for NeTEx Sweden |
| Historical data (static) | Partly available in Koda                                           | Not available                                                          |

</div>

## Static data
### File structure
The NeTEx dataset consists of three different types of files, described here below. For more technical information about each of these files, please
visit [Samtrafiken Open Data - NeTEx](https://samtrafiken.atlassian.net/wiki/spaces/SamtrafikenOpenData/pages/989233182/Samtrafiken+NeTEx+export).

**_shared_data.xml:** 
This file contains common information, such as calendar schedules, authority and operator

**_stops.xml:**
This file contains information about stops, such as quays, stop areas and entrances

**line\_\[lineNumber\].xml:**
This file contains the specific schedule for a line as well as information like route, transport mode, interchanges etc. There
is one line file per line

### Important details

- Your HTTP client has to have support for Gzip or deflate compression. This needs to be signalled through the
  HTTP `Accept` header. If your client does not support this, or is configured incorrectly, you will receive an HTTP 406
  error code
- This API supports conditional requests, and sends out HTTP Last-modified and etag headers. This way you can prevent
  downloading the same data twice.
  See [the conditional get requests chapter](/docs/using-trafiklab-data/best-practices/conditional-get-requests/) in
  our [best practices](/docs/using-trafiklab-data/best-practices/) for more information.