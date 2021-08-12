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

This data is also available in the NeTEx format. For the NeTEx format, see the [NeTEx regional API](/api/netex-regional/).

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
