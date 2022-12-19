---
title: Static data
weight: 10 
date: 2022-06-01
---

The static NeTEx Sweden dataset contains files describing all planned public transport data, with more technical
details compared to the GTFS Sweden feed but with the overall same timetable data.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification.

To see which operators are included in this dataset see the documentation in the [Netex Regional API](/api/trafiklab-apis/netex-regional/#which-operators-are-covered-by-this-dataset).

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/netex-sweden/sweden.zip?key={apikey}](https://opendata.samtrafiken.se/netex-sweden/sweden.zip?key={apikey}).

Replace `{apikey}` with your own API key. If you don´t have a key yet, read [here](/docs/using-trafiklab/getting-api-keys) on how to get one.
{{% /note %}}

#### API key levels

| Level  | Maximum calls per minute | Maximum calls per month |
|:-------|:------------------------:|:-----------------------:|
| Bronze |            10            |           50            |
| Silver |            10            |           250           |

{{% page-ref "/api/trafiklab-apis/netex-sweden/netex-sweden-specification" %}}

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