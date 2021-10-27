---
title: Static data 
aliases: "/node/27769/documentation"
weight: 10 
date: 2019-11-22
---

## Retrieving static data

The static NeTEx Regional dataset contains files describing all planned public transport data, with more technical
details compared to the GTFS Regional feeds.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification.

{{% page-ref "/docs/using-trafiklab/getting-api-keys" "/api/trafiklab-apis/netex-regional/netex-regional-spec" %}}

## Download URLs

### Regional operators

| Operator                                            | Static data                                                                                                                                                            |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Blekingetrafiken (Blekinge län)**                 | [https://opendata.samtrafiken.se/netex/blekinge/blekinge.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/blekinge/blekinge.zip?key=<api-nyckel>)                 |
| **Dalatrafik (Dalarnas län)**                       | [https://opendata.samtrafiken.se/netex/dt/dt.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/dt/dt.zip?key=<api-nyckel>)                                         |
| **DinTur (Västernorrlands län)**                    | [https://opendata.samtrafiken.se/netex/dintur/dintur.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/dintur/dintur.zip?key=<api-nyckel>)                         |
| **Gotlands kollektivtrafik (Gotlands län)**         | [https://opendata.samtrafiken.se/netex/gotland/gotland.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/gotland/gotland.zip?key=<api-nyckel>)                     |
| **Hallandstrafiken**                                | [https://opendata.samtrafiken.se/netex/halland/halland.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/halland/halland.zip?key=<api-nyckel>)                     |
| **JLT (Jönköpings län) **                           | [https://opendata.samtrafiken.se/netex/jlt/jlt.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/jlt/jlt.zip?key=<api-nyckel>)                                     |
| **Kalmar Länstrafik (Kalmar län)**                  | [https://opendata.samtrafiken.se/netex/klt/klt.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/klt/klt.zip?key=<api-nyckel>)                                           |
| **Kronobergs Länstrafik (Kronobergs län)**          | [https://opendata.samtrafiken.se/netex/krono/krono.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/krono/krono.zip?key=<api-nyckel>)                             |
| **LTR (Jämtlands län)**                             | [https://opendata.samtrafiken.se/netex/jamtland/jamtland.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/jamtland/jamtland.zip?key=<api-nyckel>)                 |
| **Länstrafiken Norrbotten**                         | [https://opendata.samtrafiken.se/netex/norrbotten/norrbotten.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/norrbotten/norrbotten.zip?key=<api-nyckel>)         |
| **Länstrafiken Västerbotten**                       | [https://opendata.samtrafiken.se/netex/vasterbotten/vasterbotten.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/vasterbotten/vasterbotten.zip?key=<api-nyckel>) |
| **Länstrafiken Örebro**                             | [https://opendata.samtrafiken.se/netex/orebro/orebro.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/orebro/orebro.zip?key=<api-nyckel>)                         |
| **Skånetrafiken (Skåne län)**                       | [https://opendata.samtrafiken.se/netex/skane/skane.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/skane/skane.zip?key=<api-nyckel>)                             |
| **SL (Stockholm län)**                              | [https://opendata.samtrafiken.se/netex/sl/sl.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sl/sl.zip?key=<api-nyckel>)                                         |
| **Sörmlandstrafiken (Södermanlands län)**           | [https://opendata.samtrafiken.se/netex/sormland/sormland.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sormland/sormland.zip?key=<api-nyckel>)                 |
| **UL (Uppsala län)**                                | [https://opendata.samtrafiken.se/netex/ul/ul.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/ul/ul.zip?key=<api-nyckel>)                                         |
| **VL (Västmanlands län)**                           | [https://opendata.samtrafiken.se/netex/vastmanland/vastmanland.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/vastmanland/vastmanland.zip?key=<api-nyckel>)     |
| **Värmlandstrafik + Karlstadsbuss (Värmlands Län)** | [https://opendata.samtrafiken.se/netex/varm/varm.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/varm/varm.zip?key=<api-nyckel>)                                 |
| **Västtrafik (Västra götalands län)**               | [https://opendata.samtrafiken.se/netex/vt/vt.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/vt/vt.zip?key=<api-nyckel>)                                         |
| **X-trafik (Gävleborgs län)**                       | [https://opendata.samtrafiken.se/netex/xt/xt.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/xt/xt.zip?key=<api-nyckel>)                                         |
| **Östgötatrafiken (Östergötlands län)**             | [https://opendata.samtrafiken.se/netex/otraf/otraf.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/otraf/otraf.zip?key=<api-nyckel>)                             |

### Commercial operators

| Operator                                                                                                                             | Planerad trafik | 
| ------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| ** SJ + Snälltåget + Tågab **  | [https://opendata.samtrafiken.se/netex/sj/sj.zip?key=<api-nyckel>](https://opendata.samtrafiken.se/netex/sj/sj.zip?key=<api-nyckel>) |

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