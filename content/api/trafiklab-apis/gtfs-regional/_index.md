---
title: GTFS Regional
layout: "single"
weight: 10
url: "/api/trafiklab-apis/gtfs-regional/"
---

{{% info %}} For technical details about HTTP headers and URLs, please use the OpenAPI Specification
available on our developer portal. {{% /info %}}

## What does this dataset contains?

This dataset contains high quality detailed data, both static and real-time, in the GTFS format. Each dataset contains
data for a specific region or operator. While the combined GTFS feeds do cover all regional public transport and some
private companies as well, each feed uses their own ids for each stop. If you are looking for an aggregated national
feed, please look at GTFS Sverige 2

### Data format

The data is in the GTFS format, and makes use of the GTFS Extensions. Realtime data follows the GTFS-Realtime
(GTFS-RT) standard, and is stored in the protobuf format.

### How often is this dataset updated?

The static data in this dataset is updated on a daily basis, typically between 03:00 and 07:00. The real-time data
(ServiceAlerts.pb and TripUpdates.pb) is updated every 15 seconds. The vehicle position data (VehiclePositions.pb)
is updated every 3 seconds.

### Which operators are covered by this dataset?

The following table shows which operators

| Operator | Static data | Real-time data | Vehicle positions | Occupancy data positions |
| :--- | :---: | :---: | :---: | :---: |
| Blekingetrafiken (Blekinge län)| ✅ |  |  |  |
| Dalatrafik (Dalarnas län)| ✅ | ✅ | ✅ |  |
| DinTur (Västernorrlands län)| ✅ |  |  |  |
| Gotlands kollektivtrafik (Gotlands län)| ✅ |  |  |  |
| Hallandstrafiken (Hallands län)| ✅ |  |  |  |
| JLT (Jönköpings län)| ✅ |  |  |  |
| Kalmar länstrafik (Kalmar län)| ✅ | ✅ | ✅ |  |
| Kronobergs länstrafik (Kronobergs län)| ✅ |  |  |  |
| LTR (Jämtlands län)| ✅ |  |  |  |
| Länstrafiken Norrbotten| ✅ |  |  |  |
| Länstrafiken Västerbotten| ✅ |  |  |  |
| Länstrafiken Örebro| ✅ |  |  |  |
| Skånetrafiken (Skåne län) | ✅ |✅ | ✅ | ✅ |
| SL (Stockholms län) | ✅ |✅ | ✅ |  |
| Sörmlandstrafiken (Södermanlands län) | ✅ |  |  |  |
| UL (Uppsala län) | ✅ |✅ | ✅ |  |
| VL (Västmanlands län) | ✅ |  |  |  |
| Värmlandstrafik & Karlstadbuss (Värmlands län) | ✅ |✅ | ✅ |  |
| Västtrafik (Västra götalands län) | ✅ |  |  |  |
| X-Trafik (Gävleborgs län) | ✅ |  |  |  |
| Östgötatrafiken (Östergötlands län)| ✅ | ✅ | ✅ |  |
| SJ, Tågab, Snälltåget | ✅ |  |  |  |

### How often does the data format changes? Do breaking changes happen?

This dataset has the **beta** status. This means that the fields can be added, or changed without prior warning.
However, when breaking changes are made, you will get one or two months to update your implementations.
