---
title: GTFS Regional
layout: "single"
weight: 10
aliases:
  - /api/gtfs-regional-static-data
  - /api/gtfs-regional-realtime
---

GTFS regional is a set of GTFS feeds of high quality, with realtime data and even realtime GPS positions for 
vehicles for some operators.  

### What does this dataset contains?

This dataset contains high quality detailed data, both static and real-time, in the GTFS format. Each dataset contains
data for a specific region or operator. While the combined GTFS feeds do cover all regional public transport operators, 
and some private companies as well, each feed uses their own ids for each stop. If you are looking for an aggregated 
national feed, please look at GTFS Sverige 2.

### Data format

The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the GTFS-Realtime
(GTFS-RT) standard, and is stored in the protobuf format.

This data is also available in the NeTEx format. For the NeTEx format, see the 
[NeTEx regional API](/api/trafiklab-apis/netex-regional/).

### How often is this dataset updated?

The static data in this dataset is updated on a daily basis. The real-time data receives multiple updates per minute,
see [realtime data](realtime) for more information.

### Which operators are covered by this dataset?

The following table shows which operators are covered by this dataset.

{{% success %}}
**New!** Realtime data for Västmanlands län is available starting 10/03/2022.
{{% /success %}}

| Operator                                       | Static data | Real-time data | Vehicle positions | Occupancy data |
|:-----------------------------------------------| :---: |:--------------:|:-----------------:| :---: |
| Blekingetrafiken (Blekinge län)                | ✔️ |                |                   |  |
| Dalatrafik (Dalarnas län)                      | ✔️ |       ✔️        |         ✔️         |  |
| DinTur (Västernorrlands län)                   | ✔️ |                |                   |  |
| Gotlands kollektivtrafik (Gotlands län)        | ✔️ |                |                   |  |
| Hallandstrafiken (Hallands län)                | ✔️ |                |                   |  |
| JLT (Jönköpings län)                           | ✔️ |   🕒 Q4 2022   |    🕒 Q4 2022     |  |
| Kalmar länstrafik (Kalmar län)                 | ✔️ |       ✔️        |         ✔️         |  |
| Kronobergs länstrafik (Kronobergs län)         | ✔️ |                |                   |  |
| Länstrafiken Jämtland (JLT)                    | ✔️ |                |                   |  |
| Länstrafiken Norrbotten                        | ✔️ |                |                   |  |
| Länstrafiken Västerbotten                      | ✔️ |       🕒       |        🕒         |  |
| Länstrafiken Örebro                            | ✔️ |       🕒       |                   |  |
| Skånetrafiken (Skåne län)                      | ✔️ |       ✔️        |         ✔️         | ✔️ |
| SL (Stockholms län)                            | ✔️ |       ✔️        |         ✔️         |  |
| Sörmlandstrafiken (Södermanlands län)          | ✔️ |                |                   |  |
| UL (Uppsala län)                               | ✔️ |       ✔️        |         ✔️         |  |
| VL (Västmanlands län)                          | ✔️ |       ✔️        |         ✔️         |  |
| Värmlandstrafik & Karlstadbuss (Värmlands län) | ✔️ |       ✔️        |         ✔️         |  |
| Västtrafik (Västra götalands län)              | ✔️ |                |                   |  |
| X-Trafik (Gävleborgs län)                      | ✔️ |       ✔️        |         ✔️         |  |
| Östgötatrafiken (Östergötlands län)            | ✔️ |       ✔️        |         ✔️         |  |
| Flixtrain                                      | ✔️ |                |                   |  |
| Ressel Rederi                                  | ✔️ |                |                   |  |
| SJ, Tågab, Snälltåget                          | ✔️ |                |                   |  |
| Sjöstadstrafiken (Stockholm Stad)              | ✔️ |                |                   |  |
| Stavsnäs båttaxi                               | ✔️ |                |                   |  |
| Y-Buss                                         | ✔️ |                |                   |  |

### How often does the data format changes? Do breaking changes happen?

Both the static and realtime datafeeds are stable. While we add new data all the time, we don't make breaking 
changes. Should we need to make a breaking change, we'll inform users first, and you'll have around 6 months time to 
make the necessary adjustments to your code.
