---
title: API:er
menu: "main"
weight: 1
sidebar: true
layout: "single"
is_fallback_source_page: true
---

{{% warning %}}
**Obs:** Detta innehåll finns inte tillgängligt på svenska. Därför ser du engelska versionen.

Om du tycker att denna sida borde översättas till svenska, kan du skriva till oss på
[support.trafiklab.se](https://suport.trafiklab.se).

Om du vill se webbsidan på engelska, [klicka här](/en/).
{{% /warning %}}


## Trafiklabs APIs

At Trafiklab we're offering a wide range of APIs and datasets. Each API and dataset provides data of a different kind or
format. Choosing the right data for your project will help you getting the best results.

The following pages will give you an overview of all our data, describing what's included, the format, how to get it,
and some examples. Make sure you also check
out [The right data type for your project](../../using-trafiklab-data/the-right-data-type-for-your-project/) to help you
choose the right data source. [Using our data](../transport-data-formats/) will help you to get started with our APIs
and datasets.

| API | File format | Scheduled data | Real-time data | Coverage | What is it |
| :--- | :---: | :---: | :---: | :---: | :--- |
| [GTFS Sverige 2](gtfs/gtfs-sverige-2-static/) | GTFS | ✅ | ❌ | Entire Sweden | All Public Transport Dataset |
| [GTFS Regional](gtfs/gtfs-regional/) | GTFS(-RT) | ✅ | Some, [see details](gtfs/gtfs-regional/#which-operators-are-covered-by-this-dataset) | [See details](gtfs/gtfs-regional/#which-operators-are-covered-by-this-dataset) | Public Transport Datasets |
| [ResRobot Stolptidstabeller](/api/trafiklab-apis/resrobot-v2/resrobot-timetables.md) | Json, XML | ✅ | Some, [see details](/api/trafiklab-apis/resrobot-v2/resrobot-timetables.md) | Entire Sweden | Departure & Arrival board API |
| [ResRobot Reseplanerare](/api/trafiklab-apis/resrobot-v2/resrobot-routeplanner.md) | Json, XML | ✅ | ❌ | Entire Sweden | Travel planner API |
| [SLs APIs ](sl/) | Json, XML | ✅ | ✅ | SL, Waxholmsbolaget | API collection |
| Oxyfi Vehicle Positions | Websocket | ❌ | ✅ | Värmlandstrafik, Norrtåg, Tåg i Bergslagen, Blekingetrafiken, Kalmars länstrafik | Realtime train position API |
| Trafikverkets API | Json, XML |  |  | Road and national rail | Road and rail API |

## Other APIs

While we offer a wide range of APIs and datasets covering public transport, easily accessible through Trafiklab, you
sometimes need something less focussed on public transport, or data not available on Trafiklab.

The APIs in the "other" category cannot be accessed through Trafiklab, but might still be valuable additions for your
project.
