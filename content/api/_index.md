---
title: APIs
menu: "main"
weight: 1
layout: "single"
sidebar: true
image: '/media/2024/09/banner_varm_tag_Oyvind_Lund.jpg'
cascade:
  - image: '/media/2024/09/banner_varm_tag_Oyvind_Lund.jpg'
---

## Trafiklabs APIs

At Trafiklab we're offering a wide range of APIs and datasets. Each API and dataset provides data of a different kind or
format. Choosing the right data for your project will help you to get the best results.

The following pages will give you an overview of all our data, describing what's included, the format, how to get it,
and some examples. Make sure you also check
out [The right data type for your project](../docs/using-trafiklab-data/the-right-data-type-for-your-project/) to help you
choose the right data source. [Using our data](../docs/using-trafiklab-data/) will help you to get started with our APIs
and datasets.

| API                                                                          | File format  | Scheduled data |                                             Real-time data                                             | What is it                                                                                                |
|:-----------------------------------------------------------------------------|:------------:|:--------------:|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------|
| [GTFS Sverige 2](/api/gtfs-datasets/gtfs-sverige-2/)                         |     GTFS     |       ✅        |                                                   ❌                                                    | Dataset with all public transport, static and historical                                                  |
| [GTFS Regional](/api/gtfs-datasets/gtfs-regional/)                           |  GTFS(-RT)   |       ✅        |        Some, [see details](/api/gtfs-datasets/gtfs-regional/#operators-covered-by-this-dataset)        | Public transport datasets                                                                                 |
| [NeTEx/SIRI Regional](/api/netex-datasets/netex-regional/)                   | NeTEx & SIRI |       ✅        |       Some, [see details](/api/netex-datasets/netex-regional/#operators-covered-by-this-dataset)       | Highly detailed public transport datasets                                                                 |
| [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/)                             |     GTFS     |       ✅        |         Some, [see details](/api/gtfs-datasets/gtfs-sweden/#operators-covered-by-this-dataset)         | Public transport dataset of Sweden, as one static dataset and multiple realtime datasets                  |
| [NeTEx Sweden](/api/netex-datasets/netex-sweden/)                            |    NeTEx     |       ✅        |                                                   ❌                                                    | Highly detailed public transport datasets of Sweden, as one static dataset and multiple realtime datasets | 
| [Stops data](/api/netex-datasets/stops-data/)                                |    NeTEx     |       ✅        |                                                   ❌                                                    | All stops of Sweden with mappings to regional IDs                                                         |
| [KoDa](/api/our-apis/koda/)                                            |  GTFS(-RT)   |       ✅        | Some, [see GTFS Regional details](/api/gtfs-datasets/gtfs-regional/#operators-covered-by-this-dataset) | High quality historical data                                                                              |
| [ResRobot Stolptidstabeller](/api/our-apis/resrobot-v21/timetables.md) |  Json, XML   |       ✅        |                  Some, [see details](/api/our-apis/resrobot-v21/timetables.md)                   | Departure & Arrival board API                                                                             |
| [ResRobot Reseplanerare](/api/our-apis/resrobot-v21/route-planner.md)  |  Json, XML   |       ✅        |                                                   ❌                                                    | Travel planner API                                                                                        |
| [SLs APIs ](/api/our-apis/sl/)                                         |  Json, XML   |       ✅        |                                                   ✅                                                    | API collection                                                                                            |
| [Oxyfi Vehicle Positions](/api/our-apis/oxyfi.md)                      |  Websocket   |       ❌        |                                                   ✅                                                    | Realtime train position API                                                                               |
| [Trafikverkets API](/api/our-apis/trafikverket.md)                     |  Json, XML   |       ✅        |                                                   ✅                                                    | Road and rail API                                                                                         |

## Other APIs

While we offer a wide range of APIs and datasets covering public transport, easily accessible through Trafiklab, you
sometimes need something less focused on public transport, or data not available on Trafiklab.

The APIs in the "related data and APIs" category cannot be accessed through Trafiklab, but might still be valuable additions for your
project.
