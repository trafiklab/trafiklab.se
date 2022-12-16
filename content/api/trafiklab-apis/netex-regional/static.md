---
title: Static data 
aliases:
  - "/node/27769/documentation"
weight: 10 
date: 2019-11-22
---

The static NeTEx Regional dataset contains files describing all planned public transport data, with more technical
details compared to the GTFS Regional feeds.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/netex/{operator}/{operator}.zip?key={apikey}](https://opendata.samtrafiken.se/netex/{operator}/{operator}.zip?key={apikey}).

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on [the overview page for this API](_index.md). Replace `{apikey}` with your own API key.
If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |
| Gold   |            20            |          2500           |

{{% page-ref "/api/trafiklab-apis/netex-regional/netex-regional-specification" %}}

## Example download URLs

Below are some example download URLs. For a complete list all operators with data available, check [the overview page for this API](_index.md).

### Regional operators

| Operator                                            | Static data                                                                                                                                                            |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Skånetrafiken (Skåne län)**                       | [https://opendata.samtrafiken.se/netex/skane/skane.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/skane/skane.zip?key=<api-nyckel>)                             |
| **SL (Stockholm län)**                              | [https://opendata.samtrafiken.se/netex/sl/sl.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sl/sl.zip?key=<api-nyckel>)                                         |
| **UL (Uppsala län)**                                | [https://opendata.samtrafiken.se/netex/ul/ul.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/ul/ul.zip?key=<api-nyckel>)                                         |
| **Östgötatrafiken (Östergötlands län)**             | [https://opendata.samtrafiken.se/netex/otraf/otraf.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/otraf/otraf.zip?key=<api-nyckel>)                             |

### Commercial operators

| Operator                                                                                                                             | Planerad trafik | 
| ------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| **SJ + Snälltåget + Tågab**  | [https://opendata.samtrafiken.se/netex/sj/sj.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sj/sj.zip?key=<api-nyckel>) |

## File structure

Each archive contains three types of files:

- **_shared_data.xml** - contains common information, such as calendar schedules 
- **_stops.xml** - contains information about stops, such as quays, stop areas and entrances
- **line\_\[lineNumber\].xml** - contains the specific schedule for a line

## Important details

- Your HTTP client has to have support for Gzip or deflate compression. This needs to be signalled through the
  HTTP `Accept` header. If your client does not support this, or is configured incorrectly, you will receive an HTTP 406
  error code 
- This API supports conditional requests, and sends out HTTP Last-modified and etag headers. This way you can prevent
  downloading the same data twice.
  See [the conditional get requests chapter](/docs/best-practices/conditional-get-requests/) in
  our [best practices](/docs/best-practices/) for more information.