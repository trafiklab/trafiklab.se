---
title: Siri
aliases:
- "api/netex-regional-siri"
weight: 20 
date: 2022-04-14
---

Siri is service Interface for Real Time Information.

The Norwegian profile includes Estimated Timetables (ET), Situation Exchange (SX) and Vehicle Monitoring (VM) data.
These are consistent with GTFS-RT TripUpdates, ServiceAlerts and VehiclePositions.


{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:

- [https://opendata.samtrafiken.se/siri/siri.pb?key={apikey}](https://opendata.samtrafiken.se/siri/siri.pb?key={apikey})

Replace `{apikey}` with your own API key.
{{% /note %}}

{{% page-ref page="/docs/using-trafiklab/getting-api-keys" %}}

## Available Siri data

### Estimated Timetables (ET)

SIRI-ET is used to model the status of existing VehicleJourneys and to ensure that deviations from the planned data (for
the same operating day) such as cancellations, additional departures, delays, detours and changes in stops, can be
published on short notice. The data is linked to objects in the planned data by use of ID's, which ensures data quality.
For more information about Estimated Timetables (ET) see [SIRI-ET](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370392/SIRI-ET).

### Situation Exchange (SX)

SIRI-SX is used to model textual descriptions of disruptions, or deviations from the planned public transport
information. The messages can be applied directly to stops, lines, vehicles etc. in the already existing public
transport data by the use of ID references. For more information about Situation Exchange (SX)
see [SIRI-SX](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370605/SIRI-SX).
### Vehicle Monitoring (VM)

SIRI-VM is used to model vehicle-movements and their progress compared to a planned timetable. The data is linked to
objects in the planned data by use of ID's, which ensures data quality. For more information about Vehicle Monitoring (
VM) see [SIRI-VM](https://enturas.atlassian.net/wiki/spaces/PUBLIC/pages/637370425/SIRI-VM).
