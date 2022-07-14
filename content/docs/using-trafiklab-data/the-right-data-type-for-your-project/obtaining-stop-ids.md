---
title: Obtaining stop ids
---

### ResRobot and GTFS Sverige 2

{{% info %}} ResRobot and GTFS Sverige 2 use the same ids for stops. You can combine them however you want.
{{% /info %}}

When you want to specify a station by its id, you will need at least one of the following:

* A list of all nearby stations, so you can either pick the nearest or let the user choose
* A way to search an existing station based on the user's input
* A list of all stations, so the user can pick an existing station, for example using autocompletion.

You can
use the [Resrobot Stop lookup API ](/api/trafiklab-apis/resrobot-v21/stop-lookup.md)
to find stops which match a given search query.

If you want a list of all stops, you can use the stops.txt file
from the [GTFS Sverige 2 dataset](/api/trafiklab-apis/gtfs-sverige-21/). Using this
list, you can search locally on the device, which often results in a superior user experience. Furthermore, you can
choose how your search function will rank stops. You can rank them based on the number of daily departures, distance
from the user, type of transport, which region or kommun they are or aren't in, ... . The downside is that you need to
find a way to keep this data updated on the client side. Updates happen no more than once per day.

If you want to find the nearest stations using an API, you can use Resrobot Närliggande Hållplatser API.

### GTFS Regional

GTFS Regional does not share stop ids with any other dataset. You can find the stop id for an operator's stop in the
stops.txt file of that operator's GTFS Regional feed.

{{% warning %}} Different operators use different ids for the same stop. This means that, for example,
Stockholm Centralen has different ids in SJ's, SL's and UL's GTFS Regional feed. {{% /warning %}}
