---
title: "Changes to SL Stop lookup"
date: "2023-11-16"
image: /media/2023/11/train-stop-pole.jpg
image_position: "center"
image_credit: Samtrafiken
---

The API SL Stop lookup is going to get some fresh updates. You will still be able to use your current API-key but you need to switch to the new URL before March
15th 2024.

<!--more--> 

The new URL is: `https://journeyplanner.integration.sl.se/v1/typeahead.<FORMAT>?key=<YOUR_KEY>&searchstring=<QUERY>`.

Later on, other APIs will also receive new URLs, with NearbyStopsV2 and TravelPlanner3.1 being the first in line. The APIs Departures, Stops and lines and
Service alerts are also getting updates, with changes expected to arrive before the end of 2023. These changes will
require changes on the client side, with XML being dropped in favor for JSON being the biggest change. The Traffic status API (Trafikläget 2) will be
discontinued and replaced by this updated version of the Service Alerts API. For SL Realtime information 4, the upcoming update will result in improved
stability.


