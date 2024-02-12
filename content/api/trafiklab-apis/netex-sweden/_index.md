---
title: NeTEx Sweden
layout: "single"
weight: 35
date: 2022-06-01
---

NeTEx Sweden is a NeTEx feed of high quality. The feed contains all data present in GTFS Sweden, as
well as additional data which can't be represented in GTFS.

At the moment this dataset does not contain all of the public transport data of Sweden.
If that is what you are looking for we recommend GTFS Sverige 2, which is much less detailed but does contain all of the public transport data of Sweden.

### What does this dataset contain?

This dataset contains high quality detailed data in the NeTEx format. Realtime SIRI data is not available for the aggregated NeTEx data. If your use case
requires real-time data, please use the regional NeTEx data or national GTFS data.
This dataset is an aggregated dataset of all the different datasets in the [Netex Regional API](/api/trafiklab-apis/netex-regional/).

### Data format

The data is in the NeTEx (**Ne**twork and **T**imetable **Ex**change) format. This is a format in which all European
operators have to publish their data. The data is aimed at both operator-to-traveller communication and internal
communication between different organizations.

### How often is this dataset updated?

The static data in this dataset is updated on a daily basis, typically between 10:00 and 13:00.

### Which operators are covered by this dataset?

| Operator                                       |    Abbreviation    | Static data |
|:-----------------------------------------------|:------------------:|:-----------:|
| Blekingetrafiken (Blekinge län)                |     `blekinge`     |     ✔️      |
| Dalatrafik (Dalarnas län)                      |        `dt`        |     ✔️      |
| DinTur (Västernorrlands län)                   |      `dintur`      |     ✔️      |
| Gotlands kollektivtrafik (Gotlands län)        |     `gotland`      |     ✔️      |
| Hallandstrafiken (Hallands län)                |     `halland`      |     ✔️      |
| JLT (Jönköpings län)                           |       `jlt`        |     ✔️      |
| Kalmar länstrafik (Kalmar län)                 |       `klt`        |     ✔️      |
| Kronobergs länstrafik (Kronobergs län)         |      `krono`       |     ✔️      |
| Länstrafiken Jämtland (JLT)                    |     `jamtland`     |     ✔️      |
| Länstrafiken Norrbotten                        |    `norrbotten`    |     ✔️      |
| Länstrafiken Västerbotten                      |   `vasterbotten`   |     ✔️      |
| Länstrafiken Örebro                            |      `orebro`      |     ✔️      |
| Skånetrafiken (Skåne län)                      |      `skane`       |     ✔️      |
| SL (Stockholms län)                            |        `sl`        |     ✔️      |
| Sörmlandstrafiken (Södermanlands län)          |     `sormland`     |     ✔️      |
| UL (Uppsala län)                               |        `ul`        |     ✔️      |
| VL (Västmanlands län)                          |   `vastmanland`    |     ✔️      |
| Värmlandstrafik & Karlstadbuss (Värmlands län) |       `varm`       |     ✔️      |
| Västtrafik (Västra götalands län)              |        `vt`        |     ✔️      |
| X-Trafik (Gävleborgs län)                      |        `xt`        |     ✔️      |
| Östgötatrafiken (Östergötlands län)            |      `otraf`       |     ✔️      |
| BT buss                                        |      `btbuss`      |     ✔️      |
| Bussbolaget Östergötland                       |     `bussost`      |     ✔️      |
| Destination Gotland                            |        `dg`        |     ✔️      |
| Flixtrain                                      |    `flixtrain`     |     ✔️      |
| Härjedalingen                                  |      `harje`       |     ✔️      |
| Inlandsbanan                                   |      `inban`       |     ✔️      |
| Lennakatten                                    |      `lenna`       |     ✔️      |
| Masexpressen                                   |      `masen`       |     ✔️      |
| Ressel Rederi                                  |      `ressel`      |     ✔️      |
| Roslagens sjötrafik                            |     `roslagen`     |     ✔️      |
| SJ, Tågab, Snälltåget                          |        `sj`        |     ✔️      |
| Sjöstadstrafiken (Stockholm Stad)              | `sjostadstrafiken` |     ✔️      |
| Stavsnäs båttaxi                               |     `battaxi`      |     ✔️      |
| Strömma Turism & Sjöfart AB                    |     `stromma`      |     ✔️      |
| TJF Smalspåret                                 |       `tjf`        |     ✔️      |
| Uddevalla Turism AB                            |    `uddevalla`     |     ✔️      |
| Y-Buss                                         |      `ybuss`       |     ✔️      |

### How often does the data format changes? Do breaking changes happen?

This dataset has the **stable** status. This means that the fields can be added without prior warning, but when changes
to existing fields are made, you will get three months to update your implementations.
