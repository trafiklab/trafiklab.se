---
title: NeTEx Regional
layout: "single"
weight: 30
url: "api/netex-regional"
alias: "api/netex-regional-static-data"
---

NeTEx regional is a set of NeTEx feeds of high quality. These feeds contain all data present in GTFS Regional, as 
well as additional data which can't be represented in GTFS.

### What does this dataset contains?

This dataset contains high quality detailed data, both static and real-time, in the NeTEx format. Each dataset contains
data for a specific region or operator.

### Data format

The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations.

### How often is this dataset updated?

The static data in this dataset is updated on a daily basis, typically between 03:00 and 07:00.

### Which operators are covered by this dataset?

The following table shows which operators

| Operator | Static data |
| :--- | :---: |
| Blekingetrafiken (Blekinge län)    | ✅ |
| Dalatrafik (Dalarnas län)    | ✅ |
| DinTur (Västernorrlands län)    | ✅ |
| Gotlands kollektivtrafik (Gotlands län)    | ✅ |
| Hallandstrafiken    | ✅ |
| JLT (Jönköpings län)    | ✅ |
| Kalmar Länstrafik (Kalmar län)    | ✅ |
| Kronobergs Länstrafik (Kronobergs län)    | ✅ |
| LTR (Jämtlands län)    | ✅ |
| Länstrafiken Norrbotten    | ✅ |
| Länstrafiken Västerbotten    | ✅ |
| Länstrafiken Örebro    | ✅ |
| Skånetrafiken (Skåne län)    | ✅ |
| SL (Stockholm län)    | ✅ |
| Sörmlandstrafiken (Södermanlands län)    | ✅ |
| UL (Uppsala län)    | ✅ |
| VL (Västmanlands län)    | ✅ |
| Värmlandstrafik + Karlstadsbuss (Värmlands Län)    | ✅ |
| Västtrafik (Västra götalands län)    | ✅ |
| X-trafik (Gävleborgs län)    | ✅ |
| Östgötatrafiken (Östergötlands län)| ✅ |

### How often does the data format changes? Do breaking changes happen?

This dataset has the **stable** status. This means that the fields can be added without prior warning, but when changes
to existing fields are made, you will get three months to update your implementations.
