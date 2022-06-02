---
title: Realtime data (SIRI)
weight: 20
date: 2022-04-14
draft: true
---

Service Interface for Real-time Information (SIRI) is a data-format for real-time data. This data contains updates and real-time changes to the static NeTEx data. The two data formats should be used together, since the real-time data refers to elements defined in the static data.

This SIRI feed is based on version 1.1 of the Norwegian SIRI profile. The profile is based on SIRI 2.0. The full profile documentation can be found here: https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370420/Norwegian+SIRI+profile

{{% info %}}
**Availability of regional data** differs per operator. See the [overview page](https://www.trafiklab.se/api/trafiklab-apis/netex-regional/) to see which data is provided
by the operator(s) you are interested in.
{{% /info %}}

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:

- [https://opendata.samtrafiken.se/siri/{operator}/SituationExchange.xml?key={apikey}](https://opendata.samtrafiken.se/siri/{operator}/SituationExchange.xml?key={apikey})
- [https://opendata.samtrafiken.se/siri/{operator}/EstimatedTimetable.xml?key={apikey}](https://opendata.samtrafiken.se/siri/{operator}/EstimatedTimetable.xml?key={apikey})
- [https://opendata.samtrafiken.se/siri/{operator}/VehicleMonitoring.xml?key={apikey}](https://opendata.samtrafiken.se/siri/{operator}/VehicleMonitoring.xml?key={apikey})


Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on the [static data documentation page](static.md). Replace `{apikey}` with your own API key.
{{% /note %}}

{{% page-ref page="/docs/using-trafiklab/getting-api-keys" %}}

## Available Siri data

### Estimated Timetables (ET)

SIRI-ET is used to model the status of existing VehicleJourneys and to ensure that deviations from the planned data (for
the same operating day) such as cancellations, additional departures, delays, detours and changes in stops, can be
published on short notice. The data is linked to objects in the planned data by use of ID's, which ensures data quality.
For more information and technical specifications, see [SIRI-ET](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370392/SIRI-ET).

### Situation Exchange (SX)

SIRI-SX is used to model textual descriptions of disruptions, or deviations from the planned public transport
information. The messages can be applied directly to stops, lines, vehicles etc. in the already existing public
transport data by the use of ID references. For more information and technical specifications, see [SIRI-SX](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370605/SIRI-SX).
### Vehicle Monitoring (VM)

SIRI-VM is used to model vehicle-movements and their progress compared to a planned timetable. The data is linked to
objects in the planned data by use of ID's, which ensures data quality. For more information and technical specifications, see [SIRI-VM](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370425/SIRI-VM).
