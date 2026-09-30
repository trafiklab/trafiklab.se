---
title: API:er
menu: "main"
weight: 1
sidebar: true
layout: "single"
image: '/media/2024/09/banner_varm_tag_Oyvind_Lund.jpg'
cascade:
  - image: '/media/2024/09/banner_varm_tag_Oyvind_Lund.jpg'
---

## Trafiklabs API:er

Trafiklab erbjuder ett brett utbud av API:er och dataset. Varje API och dataset tillhandahåller data av olika slag eller
i olika format. Genom att välja rätt data för ditt projekt får du bäst resultat.

På följande sidor får du en översikt över all vår data: vad som ingår, vilket format den har, hur du hämtar den och
några exempel. Läs även
[Rätt datatyp för ditt projekt](../docs/using-trafiklab-data/the-right-data-type-for-your-project/) för hjälp
att välja rätt datakälla. [Använda vår data](../docs/using-trafiklab-data/) hjälper dig att komma igång med våra
API:er och dataset.

| API                                                                        |  Filformat   | Tidtabellsdata |                                                 Realtidsdata                                                 | Vad är det                                                                                                 |
|:---------------------------------------------------------------------------|:------------:|:--------------:|:------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------|
| [GTFS Sverige 2](/api/gtfs-datasets/gtfs-sverige-2/)                       |     GTFS     |       ✅       |                                                      ❌                                                      | Dataset med all kollektivtrafik, statisk och historisk data                                                |
| [GTFS Regional](/api/gtfs-datasets/gtfs-regional/)                         |  GTFS(-RT)   |       ✅       |          Delvis, [se detaljer](/api/gtfs-datasets/gtfs-regional/#operators-covered-by-this-dataset)          | Dataset med kollektivtrafikdata                                                                            |
| [NeTEx/SIRI Regional](/api/netex-datasets/netex-regional/)                 | NeTEx & SIRI |       ✅       |         Delvis, [se detaljer](/api/netex-datasets/netex-regional/#operators-covered-by-this-dataset)         | Mycket detaljerade dataset med kollektivtrafikdata                                                         |
| [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/)                           |     GTFS     |       ✅       |           Delvis, [se detaljer](/api/gtfs-datasets/gtfs-sweden/#operators-covered-by-this-dataset)           | Kollektivtrafikdata för Sverige, som ett statiskt dataset och flera realtidsdataset                        |
| [NeTEx Sweden](/api/netex-datasets/netex-sweden/)                          |    NeTEx     |       ✅       |                                                      ❌                                                      | Mycket detaljerad kollektivtrafikdata för Sverige, endast statisk data                                     |
| [Stops data](/api/netex-datasets/stops-data/)                              |    NeTEx     |       ✅       |                                                      ❌                                                      | Alla hållplatser i Sverige med koppling till regionala ID:n                                                |
| [KoDa](/api/our-apis/koda/)                                                |  GTFS(-RT)   |       ✅       | Delvis, [se detaljer för GTFS Regional](/api/gtfs-datasets/gtfs-regional/#operators-covered-by-this-dataset) | Historisk data av hög kvalitet                                                                             |
| [Trafiklab Realtime APIs](/api/our-apis/trafiklab-realtime-apis/_index.md) |     Json     |       ✅       |                                                      ✅                                                      | API:er för avgångs- och ankomsttavlor, turdetaljer och hållplatsuppslag                                    |
| [ResRobot Stolptidstabeller](/api/our-apis/resrobot-v21/timetables.md)     |  Json, XML   |       ✅       |                                                      ❌                                                      | API för avgångs- och ankomsttavlor                                                                         |
| [ResRobot Reseplanerare](/api/our-apis/resrobot-v21/route-planner.md)      |  Json, XML   |       ✅       |                                                      ❌                                                      | API för reseplanering                                                                                      |
| [Oxyfi Vehicle Positions](/api/our-apis/oxyfi.md)                          |  Websocket   |       ❌       |                                                      ✅                                                      | API för tågpositioner i realtid                                                                            |

## Andra API:er

Vi erbjuder ett brett utbud av API:er och dataset om kollektivtrafik som är lätta att komma åt via Trafiklab, men ibland
behöver du något som är mindre inriktat på kollektivtrafik, eller data som inte finns på Trafiklab.

API:erna i kategorin "Related data and APIs" är inte del av Trafiklab, men kan ändå vara värdefulla tillägg till ditt
projekt.
