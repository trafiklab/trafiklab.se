---
title: "FAQ: How do I ...?"
description: Answers to the questions we get most often on our support forum, sorted by what you are trying to build
layout: "single"
weight: 1000
---

This page collects som of the questions which come up most often on [our support forum](https://support.trafiklab.se)
.For account and API key basics, see
[Using Trafiklab.se](/docs/getting-started/using-trafiklab/) and
[the general FAQ](/docs/getting-started/frequently-asked-questions/).

## Choosing the right data

### I want to show the next departures from a stop. Which API do I use?

Use the [Trafiklab Realtime APIs](/api/our-apis/trafiklab-realtime-apis/). The
[Timetables endpoint](/api/our-apis/trafiklab-realtime-apis/timetables/) returns departures or arrivals for a stop,
including realtime times, cancellations, platforms and alerts, as JSON. Find the stop id with the
[Stop Lookup endpoint](/api/our-apis/trafiklab-realtime-apis/stop-lookup/).

This applies to digital signage, smart mirrors, home automation (there is a community Home Assistant integration),
widgets and mobile apps. The ResRobot Timetables API is deprecated, only has realtime data for trains, and upgrade
requests for it are no longer approved when the Realtime APIs fit the use case.

### I want to let users plan a journey from A to B

Use the [ResRobot Route planner](/api/our-apis/resrobot-v21/route-planner/). Origin and destination can be stop ids or
coordinates. ResRobot is the right tool when a user asks a question and you need one answer. It is the wrong tool when
you need to run hundreds or thousands of searches (see below).

If you need more control, more requests, or an SLA, run your
own [OpenTripPlanner](https://github.com/opentripplanner/OpenTripPlanner)
instance fed with [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/)
or [GTFS Sverige 2](/api/gtfs-datasets/gtfs-sverige-2/).

### I want travel times between many places, an isochrone map, or a reachability analysis

Download a GTFS file and compute locally, for example with OpenTripPlanner or a routing library. ResRobot is not an
option for this: every request costs money on our side, the quota will not cover it, and upgrade requests for scraping
a journey planner are always denied. Rule of thumb: if you need more than ten requests to get your answer, you should be
using GTFS.

### I want to analyse delays, punctuality or vehicle movements over time

Use [KoDa](/api/our-apis/koda/), which archives every GTFS and GTFS-RT file published through GTFS Regional since
February 2020. The live GTFS-RT feeds only contain the current state; nothing is kept. If you want to act on delays
from the last few hours, store the realtime feeds yourself as they are published.

Older timetables (back to 2012) are in
the [GTFS Sverige 2 archive](https://data.samtrafiken.se/trafiklab/gtfs-sverige-2/),
which does not need an API key.

### I want live vehicle positions on a map

Use the `VehiclePositions.pb` feed from [GTFS Regional Realtime](/api/gtfs-datasets/gtfs-regional/#realtime-data) or
[GTFS Sweden 3 Realtime](/api/gtfs-datasets/gtfs-sweden/#realtime-data). Positions are updated roughly every two
seconds for most operators. Check the availability table on those pages: not every operator delivers positions. Neither
ResRobot nor the Trafiklab Realtime APIs provide vehicle positions.

Positions for some regional trains are also available as a websocket stream from [Oxyfi](/api/our-apis/oxyfi/).

### I want a list of all stops in Sweden

Pick depending on the detail you need:

- `stops.txt` in [GTFS Sverige 2](/api/gtfs-datasets/gtfs-sverige-2/): every stop in the country, one entry per stop
  area, no platforms. Ids are the national stop ids (rikshållplatser) used by ResRobot and the Realtime APIs.
- `stops.txt` and `areas.txt` in [GTFS Sweden 3](/api/gtfs-datasets/gtfs-sweden/): stops and platforms, with
  `stop_areas.txt` mapping them to the national ids.
- [Stops data](/api/netex-datasets/stops-data/) (NeTEx): the most detailed dataset, including mappings between all id
  systems, Trafikverket signatures and municipality.
- The [Realtime API stop list](/api/our-apis/trafiklab-realtime-apis/stop-lookup/): JSON, sorted by number of
  departures, meant for search boxes and autocomplete.

### I want all lines serving a stop, or all stops on a line

No API returns this directly. Join the GTFS files: `routes.txt` → `trips.txt` → `stop_times.txt` → `stops.txt`. Do this
once a day after the new GTFS file is published, store the result, and serve it from your own backend.

### I want timetables or stops in a GIS tool (QGIS, ArcGIS)

We do not offer WMS or WFS services. Load the GTFS files with a GTFS plugin for your tool, or import `stops.txt` and
`shapes.txt` as CSV. Shapes are only present in GTFS Regional and GTFS Sweden 3.

### I want disruption messages

Use `ServiceAlerts.pb` from GTFS Regional Realtime or GTFS Sweden 3 Realtime, or the `alerts` field on each departure
in the Realtime APIs. Delays and cancellations of individual trips are in `TripUpdates.pb`, not in service alerts.

### I want passenger counts or how crowded a vehicle is

Exact passenger counts are not available. Occupancy levels (`occupancy_status`, six levels) are present in the
VehiclePositions feeds for the operators which deliver it, currently Skånetrafiken and Östgötatrafiken.

### I want fare zones, municipalities or counties for stops

GTFS does not contain this and we have no plans to add zones. Use the
NeTEx [Stops data](/api/netex-datasets/stops-data/)
(`TopographicPlaceRef`, tariff zones in NeTEx Regional), or derive it yourself from the stop coordinates and
municipality boundaries from OpenStreetMap or Lantmäteriet.

### I want to sell tickets

Trafiklab offers traffic data only. Ticketing goes through [Samtrafiken](https://samtrafiken.se) and its reseller
platform, or through the individual operators. The [Samtrafiken Sales data](/api/netex-datasets/samtrafiken-sales-data/)
feed describes which traffic is sellable, but does not sell anything.

### GTFS Sverige 2, GTFS Regional or GTFS Sweden 3?

|                              | GTFS Sverige 2      | GTFS Regional                      | GTFS Sweden 3                                            |
|:-----------------------------|:--------------------|:-----------------------------------|:---------------------------------------------------------|
| Coverage                     | All of Sweden       | One operator per feed              | All regional operators, merged                           |
| Realtime                     | No                  | Yes, per operator                  | Yes, per operator                                        |
| Platforms, shapes, headsigns | No                  | Yes                                | Yes                                                      |
| Stop ids                     | National (`740...`) | Operator-local (`9021.../9022...`) | Operator-local, with `areas.txt` mapping to national ids |
| History                      | Archive since 2012  | KoDa since 2020                    | -                                                        |

Use Sverige 2 when you need every operator in one simple file. Use Regional when you only care about one region, or
need the richest data for that region. Use Sweden 3 when you need national coverage with realtime and detail. The
regional feeds are unfiltered and can overlap (the same trip can be in both SL's and UL's feed); Sweden 3 is
deduplicated.

### GTFS or NeTEx?

The same traffic is published in both formats, generated from the same system. NeTEx carries more detail: stop
entrances, accessibility, tariff zones, notices, interchange rules. GTFS has far more tooling. Unless you need something
GTFS cannot represent, use GTFS. There is no need to combine the two.

## Stop ids

### Which id do I give to the Realtime APIs?

The id of a national stop (rikshållplats) or a meta-stop. These are the `740...` ids from GTFS Sverige 2 `stops.txt`,
`areas.txt` in GTFS Sweden 3, and the `extId` in ResRobot. Do not use the ids of the individual stops inside a stop
group.

Meta-stops group a whole city centre (Stockholm is `740098000`; meta-stop ids start with `740098`). Searching a
meta-stop returns departures from every stop in it. ResRobot expands to the meta-stop automatically; the Realtime APIs
do not, so "Stockholm Centralstation" and "Stockholm" give different results.

### Can I combine stop ids between datasets?

- ResRobot, GTFS Sverige 2, GTFS Sweden 3 `areas.txt` and the Realtime APIs share the national ids.
- GTFS Regional and NeTEx Regional use operator-local ids. Different operators use different ids for the same stop.
  GTFS Sweden 3 keeps those local ids and maps them to national ids through `stop_areas.txt`.
- The NeTEx [Stops data](/api/netex-datasets/stops-data/) contains all mappings, including Trafikverket signatures.
- SL's APIs use yet another id system which cannot be mapped automatically to any of the above, see below.

### Can I combine SL's APIs with ResRobot, the Realtime APIs or GTFS?

No. SL's APIs are run by SL on their own systems and use their own site, stop area and stop point ids, as well as
their own line and journey ids. None of these match the national ids used by ResRobot and the Realtime APIs, nor the
ids in GTFS Sverige 2 or GTFS Sweden 3. There is no lookup table, and matching on names or coordinates is unreliable.

Pick one id system and stay within it. All SL traffic is included in the Trafiklab datasets and APIs, so if you need
to combine SL data with the rest of Sweden, use the Realtime APIs, ResRobot or GTFS for SL as well. The only exception
is the SL GTFS Regional feed, whose `stop_id` equals the `gid` returned by SL's stop-point endpoints.

### How do I find stops near a coordinate?

Use [ResRobot Nearby stops](/api/our-apis/resrobot-v21/nearby-stops/), which returns national ids you can use in the
Realtime APIs as well. Or download the full stop list once (Realtime API stop list or GTFS `stops.txt`) and calculate
distances locally; that is faster and works offline.

{{% warning %}} A user's position is personal data. Ask for consent before sending it to any API and mention it in your
privacy policy. {{% /warning %}}

### Are stop names unique? Do they contain the municipality?

No and no. Many stops share a name ("Centrum", "Stationen"). The GTFS files have no municipality field; derive it from
the coordinates, or use the Stops data.

## API keys and quota

### My key gives "Key does not exist" or "Key does not have access to file"

Every API has its own key and its own URL. A GTFS Regional key does not open GTFS Sweden 3, a GTFS Sweden 3 key does
not open the Realtime APIs, and so on. Check that the key in your project was created for the API in the URL.

If the key is right, the URL usually is not: a trailing `;` or `.`, a space, two URLs copied with one button, or
`{operator}` and `{apikey}` placeholders left in place. Type the URL by hand to rule out hidden characters, and
URL-encode non-ASCII characters such as `ä` (`%C3%A4`).

### I got HTTP 429 but my statistics say I am far below the quota

Usage statistics on developer.trafiklab.se are updated once a day, so they lag behind. A 429 means the quota is really
exceeded, either per minute or per 30 days. For GTFS file downloads, HEAD requests and conditional requests count as
calls too. Reuse the file you already downloaded while developing.

### How do I get a higher quota?

Click "Upgrade quota" next to the key on developer.trafiklab.se and describe the project, the expected number of
requests and the number of users. All levels are free. Requests are usually handled within a few working days.
Requests which will not be approved: scraping a journey planner for analytics (use GTFS), stress tests, and more than
the base level for private departure boards. One bronze key is enough for a smart mirror if you
[adjust the update frequency during the day](/docs/using-trafiklab-data/best-practices/limiting-requests/).

### Can my mobile app call the APIs directly?

For the Realtime APIs and ResRobot: yes, with your key in the app. Prefer a backend in between if you can, so you can
cache responses, so all users share the quota efficiently and so you can switch APIs without an app update.

For GTFS and GTFS-RT: no. Build a small backend which downloads the files, merges static and realtime data, and exposes
the slice your app needs as JSON. Phones should not process GTFS files, and one key must not be embedded in thousands
of clients polling protobuf feeds.

### How often may I call the APIs?

- Realtime APIs: responses are cached for 60 seconds, so calling more often for the same stop gives no new data. Lower
  the frequency at night and when nobody is looking at the screen.
- GTFS-RT: TripUpdates and ServiceAlerts are regenerated every 15 seconds, VehiclePositions every 2 seconds. Polling
  every 15 to 30 seconds is enough for most uses. Use `If-Modified-Since` and read `Last-Modified`; never poll on
  exactly the generation interval, add a few hundred milliseconds margin.
- Static GTFS and NeTEx: once per day. Files are published nightly; fetching at 06:00 is safe for all feeds.
- KoDa: one file at a time, wait for HTTP 200 before requesting the next.

### May I cache and redistribute the data?

Yes. All datasets are CC0 except the Realtime APIs, which are CC-BY 4.0. Caching GTFS files and passing them on is
explicitly allowed.

### Do I need to show attribution?

For CC0 data (GTFS, NeTEx, ResRobot, KoDa): not required, but appreciated. For the Realtime APIs (CC-BY): yes. A line in
your app's settings or about page is enough for apps; a public display or website widget should carry a small
"data from Trafiklab.se" note, since viewers cannot look it up otherwise.

## Working with GTFS

### Which protobuf schema do I need for GTFS-RT?

The standard `gtfs-realtime.proto` from [gtfs.org](https://gtfs.org/documentation/realtime/proto/). Use the official
`gtfs-realtime-bindings` package for your language. GTFS-RT cannot be parsed without a protobuf library. See
[the protobuf file format](/docs/using-trafiklab-data/the-protobuf-file-format/).

### The trip_id in the realtime feed does not exist in my trips.txt

Almost always one of two things:

- You are mixing datasets. GTFS Regional Realtime must be combined with the static GTFS Regional file of the same
  operator; GTFS Sweden 3 Realtime with the static GTFS Sweden 3 file. The realtime feeds share ids only with their own
  static feed.
- Your static file is stale. Download it daily; ids can change between publications and some operators add trips
  daily. Match realtime data against a static file published at most a few days before.

Trips with `schedule_relationship: ADDED` are extra vehicles and have no static counterpart. That is expected.

### How do I uniquely identify a trip or a departure?

`trip_id` together with `start_date`. The same `trip_id` runs on many days. For a departure, add `stop_id` and the
scheduled time. Do not parse or interpret ids; they are opaque strings and may change at timetable changes.

### What does start_date mean for trips after midnight?

GTFS uses service days. A departure at `25:30:00` with service date 12 April happens at 01:30 on 13 April, and its
`start_date` in the realtime feed is `20240412`. To list everything departing on day D, take trips with service date D
and times below `24:00:00`, plus trips with service date D-1 and times from `24:00:00` upward. Do not simply take the
time modulo 24 hours.

### calendar.txt has all weekdays set to 0

By design. `calendar.txt` only defines the validity period of a service; the actual operating days are listed in
`calendar_dates.txt` with `exception_type = 1`. Derive weekday patterns from those dates if you need them.

### What is the difference between route_short_name, route_long_name, trip_short_name and the headsign?

- `route_short_name`: the line number. May be empty for some operators.
- `route_long_name`: the line name when a line is known by name. When both are set, the long name is the correct public
  name and the short name is for displays that cannot show it.
- `trip_short_name`: the announced trip number, typically the train number. Empty when the operator only announces the
  line (SL commuter trains show "42"). `samtrafiken_internal_trip_number` holds the operator's technical trip number.
- `trip_headsign` / `stop_headsign`: what the vehicle's display shows. Present in GTFS Regional and Sweden 3; GTFS
  Sverige 2 has no headsigns and ResRobot shows the last stop instead.
- `direction_id`: operator-defined, has no fixed meaning. Use headsigns or the last stop to tell directions apart.

### pickup_type is 3 on ordinary bus stops. Is that an error?

No. `3` means "coordinate with the driver", which is how "press the stop button / signal the driver" is expressed, as
most buses do not stop unless asked. `0` is used where vehicles always stop (trains, metro). `2` with
`booking_rules.txt` means the trip must be booked in advance. Trips with both `pickup_type` and `drop_off_type` set
to `1` on every stop are non-revenue runs; filter them out.

### shape_dist_traveled is empty or not increasing

Both are allowed by the specification. The field is only filled when the operator delivers it, and ferries, trains and
demand-responsive traffic often lack it. If a tool refuses the feed, drop `shapes.txt` and the column rather than
expecting us to fabricate values.

### What does uncertainty: 0 mean in TripUpdates?

The stop has been observed: the vehicle actually arrived or departed at that time. A missing `uncertainty` means a
prediction. Observed stops stay in the feed for about ten minutes and then disappear, so use the static `stop_times`
for the full stop list. VehiclePositions contain position, speed and bearing but not `current_status` or
`current_stop_sequence`.

### There are vehicles in VehiclePositions without a trip, and cancelled trips without a trip_id

Vehicles without a trip are on their way to or from the depot, parked, or reinforcement buses. We deliberately publish
what the operators send without filtering, so you can see all vehicles. Cancellations without `trip_id` carry
`route_id`, `direction_id`, `start_date` and `start_time`; match on those.

### How many days of traffic does a static file contain?

From roughly three days back to several months ahead. Files are largest right after the timetable changes in June and
December. Changes with less than a day's notice are published as realtime data, not in the static file.

### Where are the trip numbers and operator-internal ids?

Since March 2026 in `trips.txt` (`trip_short_name`, `samtrafiken_internal_trip_number`) of GTFS Regional and GTFS
Sweden 3. The older `_extra.zip` files with `trips_dated_vehicle_journey.txt` still exist for backwards compatibility
and use the same key and quota. They are not GTFS; do not run a GTFS validator on them.

### Why do trains lack realtime data, platforms or shapes in GTFS Sweden 3 and the Realtime APIs?

Since spring 2026, all rail traffic in GTFS Sweden 3 comes from Trafikverket, which is the single source of truth for
trains in Sweden. The data stream we use from Trafikverket does not include platforms, shapes or realtime yet, so
trains show `scheduled_platform: null` and `is_realtime: false`. The operator's own GTFS Regional feed still has
realtime and shapes for those trains, and the
[Trafikverket Open API](/api/other-apis/trafikverket/) has platforms and realtime for all trains. We are working on
bringing this data into GTFS Sweden 3.

## Working with the Realtime APIs

### Can I get more than 60 minutes of departures?

The window is fixed at 60 minutes so responses can be cached. Call `/v1/departures/{id}/{yyyy-MM-ddTHH:mm}` once per
hour you need. There are no filters on line, direction or destination; filter on the client. A filter would never
return more than the unfiltered response.

### I see duplicate departures at the same minute

You are probably querying a meta-stop which contains several national stops served by the same line. Each departure
carries its own `stop` object; use `trip_id`, `start_date` and `stop.id` together to tell them apart.

### The usage counter does not move

Statistics are updated nightly. Quota is enforced in real time regardless of what the counter shows.

## Working with ResRobot

### The response is HTTP 200 but contains no results

ResRobot returns `SVC_NO_RESULT` with status 200. Always check for an `errorCode` field in the response rather than
relying on the HTTP status alone. See [error codes](/api/our-apis/resrobot-v21/error-codes/).

### maxJourneys does not limit the departure board

For searches close to the current time `maxJourneys` is ignored. Use `duration` (minutes, default 60) to control the
window, and cut the list on your side.

### Why are some journeys missing from the route planner results?

Alternatives which depart earlier but arrive at the same time or later are dropped, as are connections where the
transfer time is judged too short. The planner only returns the best alternatives. You can influence results with
`maxChange`, `products`, `operators`, `originWalk` and `destWalk`, but you cannot force a specific journey.

### Are times UTC or local?

Local Swedish time (CET/CEST), always. The same goes for the Realtime APIs and GTFS.

### Does ResRobot contain platforms, vehicle positions or realtime for buses?

No. Platform information appears only as `rtTrack` when realtime data exists, which is the case for trains only. Use
the Realtime APIs for platforms and bus realtime, and GTFS-RT for vehicle positions.

## Working with KoDa

### The download returns HTTP 202

The archive for that day is being built. Poll the same URL every 30 seconds until you receive HTTP 200. Building can
take up to an hour for large operators. Request one file at a time; parallel requests slow down or break the job for
everyone.

### The archive does not open

Archives are 7-Zip (LZMA2), not gzip or tar. Use `7z x` or a 7-Zip library. Each archive contains a directory tree, so
several days can be extracted into the same folder. The `pykoda` library from the original research project is
unmaintained and does not handle 202 responses or the archive format correctly.

### Which static file do I combine with historical realtime data?

The static file published closest before the realtime data, and at most a week older. Download it from the same KoDa
endpoint for that date. Using a static file from another timetable period will leave most trips unmatched.

## Data quality

### The data is wrong (coordinates, missing trips, odd route types)

Trafiklab publishes what the operators deliver. We do not correct regional data ourselves, so the fix has to come from
the operator. Post on the support forum with the operator, the stop or trip id and the date; we verify it and forward
it. There is no SLA for operator fixes.

### A feed is down

Check [status.trafiklab.se](https://status.trafiklab.se) first. Nightly low traffic can make a feed look empty without
being down. Trafiklab-run feeds change only with months of notice, sent to the e-mail address on your account, so keep
it valid.

## Still stuck?

Post on [support.trafiklab.se](https://support.trafiklab.se). Include the exact URL (without your key), the response
you got, and what you expected. Questions about third-party apps built on our data go to those apps' developers;
general programming questions are better placed on Stack Overflow.
