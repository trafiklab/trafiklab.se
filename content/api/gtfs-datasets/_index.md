---
title: GTFS Datasets
weight: 1
layout: "single"
sidebar: true
aliases:
  - /docs/using-trafiklab-data/using-gtfs-files/
  - /docs/using-trafiklab-data/using-gtfs-files/static-gtfs-files/
  - /docs/using-trafiklab-data/using-gtfs-files/realtime-gtfs-files/
image: '/media/2024/09/banner_building.jpg'
cascade:
  - image: '/media/2024/09/banner_building.jpg'
---

## GTFS at Trafiklab

At Trafiklab, we offer three GTFS feeds.

[**GTFS Sverige 2**](/api/gtfs-datasets/gtfs-sverige-2) which includes information for entire Sweden

[**GTFS Regional**](/api/gtfs-datasets/gtfs-regional) which consists of multiple GTFS feeds, each of which covers an
operator in Sweden

[**GTFS Sweden 3**](/api/gtfs-datasets/gtfs-sweden) which is an aggregated dataset of all the different datasets
  in GTFS Regional. It gives a single GTFS feed for static data while the realtime feeds are, for performance
  reasons, split up by specific regions or operators

#### What is the difference?
It can be hard to understand the differences between all GTFS feeds but here is a short description. GTFS Sverige 2 is
the only feed with complete coverage of operators in Sweden and only contains static data. GTFS Regional is per
region/operator and perfect if you are interested in for example only SL or only Skånetrafiken. GTFS Regional also
contains
more details like for example shapes or stop points (instead of only stop areas) which is missing in GTFS Sverige.
GTFS Sweden 3 is an aggregated dataset of all GTFS Regional so the level of detail is the same. The goal is to replace
GTFS Sverige with this dataset but that requires a 100% coverage of operators which is not the case at the moment

You can see the general difference between GTFS Sverige 2 and GTFS Regional data below.
<div class="wide">

|                          | GTFS Sverige 2   | GTFS Regional/ GTFS Sweden 3                   |
|:-------------------------|:-----------------|:-----------------------------------------------|
| Coverage                 | 100%             | 92%                                            |
| Data quality             | Average quality  | High quality, based on higher level of details |
| Real-time data           | Only static data | Static + Real-time + GPS positions             |
| Historical data (static) | Since 2012       | Partly available in Koda                       |

{{% info %}} You can find the complete GTFS reference
at [https://developers.google.com/transit/gtfs/reference/](https://developers.google.com/transit/gtfs/reference/).

You can find the complete GTFS-RT reference
at [https://developers.google.com/transit/gtfs-realtime/reference](https://developers.google.com/transit/gtfs-realtime/reference)
{{% /info %}}

{{% note %}} If you want to learn about what GTFS is and how it works, read further [down](./_index.md#gtfs-basics)
on this page.
{{% /note %}}

## Static GTFS files

### What does each GTFS file contain

{{% warning %}} The content below is based on the official GTFS Specification, developed by the GTFS
community and published
at [https://developers.google.com/transit/gtfs/reference/](https://developers.google.com/transit/gtfs/reference/).

We modified the version below to describe the feeds published by Trafiklab. Fields and files that are not included in
any Trafiklab feed are not described below. For the latest version or in case of conflict, refer to the official
documentation. {{% /warning %}}

* In the tables below, the column 'available in dataset' will be bold if the field is always present and not bold if it 
is not always present.

### agency.txt

| Field Name        | Type          | Available in dataset | Description                                                                                                                                                                                                                                                                     |
|:------------------|:--------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `agency_id`       | ID            | **All**              | Uniquely identifies a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies. |
| `agency_name`     | Text          | **All**              | Full name of the transit agency.                                                                                                                                                                                                                                                |
| `agency_url`      | URL           | **All**              | URL of the transit agency.                                                                                                                                                                                                                                                      |
| `agency_timezone` | Timezone      | **All**              | Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each has the same `agency_timezone`.                                                                                                                                           |
| `agency_lang`     | Language code | **All**              | Primary language used by this transit agency                                                                                                                                                                                                                                    |
| `agency_fare_url` | URL           | GTFS Regional        | URL of a web page that allows a rider to purchase tickets or other fare instruments for that agency online                                                                                                                                                                      |

The following excerpt gives some example values for the different fields.

```text
agency_id,agency_name,agency_url,agency_timezone,agency_lang
141010000000001418,Västtrafik,https://www.resrobot.se/,Europe/Stockholm,sv
141010000000001001,Västtrafik Göteborgsområdet AB Lokaltrafik AB,https://www.resrobot.se/,Europe/Stockholm,sv
141010000651668112,MTR Express (Sweden) AB,https://www.resrobot.se/,Europe/Stockholm,sv
141010000452254130,Öresundståg,https://www.resrobot.se/,Europe/Stockholm,sv
```

### routes.txt

| Field Name         | Type                              | Available in dataset | Description                                                                                                                                                                                                                                                                                                            |
|:-------------------|:----------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `route_id`         | ID                                | **All**              | Identifies a route.                                                                                                                                                                                                                                                                                                    |
| `agency_id`        | ID referencing `agency.agency_id` | **All**              | Agency for the specified route. This field is required when the dataset provides data for routes from more than one agency in [agency.txt](https://developers.google.com/transit/gtfs/reference/#agency), otherwise it is optional.                                                                                    |
| `route_short_name` | Text                              | All                  | Short name of a route. This will often be a short, abstract identifier like "32", "100X", or "Green" that riders use to identify a route, but which doesn't give any indication of what places the route serves. Either `route_short_name` or `route_long_name` must be specified, or potentially both if appropriate. |
| `route_long_name`  | Text                              | All                  | Full name of a route. This name is generally more descriptive than the `route_short_name` and often includes the route's destination or stop. Either `route_short_name` or `route_long_name` must be specified, or potentially both if appropriate.                                                                    |
| `route_type`       | Enum                              | **All**              | Indicates the type of transportation used on a route.                                                                                                                                                                                                                                                                  |
| `route_url`        | URL                               | None                 | URL of a web page about the particular route. Should be different from the `agency.agency_url` value. Not used.                                                                                                                                                                                                        |
| `route_desc`       | Text                              | GTFS Regional        | Description of a route that provides useful, quality information. Should not be a duplicate of `route_short_name` or `route_long_name`.                                                                                                                                                                                |

The GTFS standard defines 9 route_types, but all Trafiklab feeds make use
of [extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types). Check the
feed-specific documentation for examples.

The following excerpt shows some example values.

```text
route_id,agency_id,route_short_name,route_long_name,route_type
9011014280200000,141010000000001418,302,,717
9011014374100000,141010000000001418,420,,717
9011014471100000,141010000000001418,711,,700
9011014630400000,141010000000001418,304,,700
```

### trips.txt

| Field Name        | Type                                                                | Available in dataset | Description                                                                                                                                                                                                                                                                                                                                                               |
|:------------------|:--------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `route_id`        | ID referencing `routes.route_id`                                    | **All**              | Identifies a route.                                                                                                                                                                                                                                                                                                                                                       |
| `service_id`      | ID referencing `calendar.service_id` or `calendar_dates.service_id` | **All**              | Identifies a set of dates when service is available for one or more routes.                                                                                                                                                                                                                                                                                               |
| `trip_id`         | ID                                                                  | **All**              | Identifies a trip.                                                                                                                                                                                                                                                                                                                                                        |
| `trip_headsign`   | Text                                                                | **GTFS Sverige 2**   | Text that appears on signage identifying the trip's destination to riders. Use this field to distinguish between different patterns of service on the same route. If the headsign changes during a trip, `trip_headsign` can be overridden by specifying values for the `stop_times.stop_headsign`.                                                                       |
| `trip_short_name` | Text                                                                | GTFS Sverige 2       | Public facing text used to identify the trip to riders, for instance, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, leave this field empty. A `trip_short_name` value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations. |
| `direction_id`    | Enum                                                                | **GTFS Regional**    | Indicates the direction of travel for a trip. This field is not used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are:  `0` - Travel in one direction (e.g. outbound travel). `1` - Travel in the opposite direction (e.g. inbound travel).                                                                    |
| `shape_id`        | ID referencing `shapes.shape_id`                                    | **GTFS Regional**    | Identifies a geospatial shape describing the vehicle travel path for a trip.                                                                                                                                                                                                                                                                                              |

The following excerpt shows what a trips.txt file can look like:

```text
route_id,service_id,trip_id,trip_headsign,direction_id,shape_id
9011014255000000,1,141010000961947846,,0,1
9011014255000000,1,141010000961947902,,0,1
9011014255000000,1,141010000961947958,,0,1
9011014255000000,1,141010000961948014,,0,1
```

{{% info %}} This example doesn't include a headsign, which means descriptions must be obtained from a higher
lever (route) or lower level (stop time). {{% /info %}}

### stop\_times.txt

A stop time is a certain trip picking up or dropping of passengers at a certain stop, at a certain time.

| Field Name            | Type                           | Available in dataset | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:----------------------|:-------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `trip_id`             | ID referencing `trips.trip_id` | **All**              | Identifies a trip.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `arrival_time`        | Time                           | **All**              | Arrival time at a specific stop for a specific trip on a route. If there are not separate times for arrival and departure at a stop, enter the same value for `arrival_time` and `departure_time`. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. <br/> <br/> Scheduled stops where the vehicle strictly adheres to the specified arrival and departure times are timepoints. If this stop is not a timepoint, it is recommended to provide an estimated or interpolated time. If this is not available, arrival_time can be left empty. Further, indicate that interpolated times are provided with `timepoint`=`0`. If interpolated times are indicated with `timepoint`=`0`, then time points must be indicated with `timepoint`=`1`. Provide arrival times for all stops that are time points. An arrival time must be specified for the first and the last stop in a trip. |
| `departure_time`      | Time                           | **All**              | Departure time from a specific stop for a specific trip on a route. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. If there are not separate times for arrival and departure at a stop, enter the same value for `arrival_time` and `departure_time`. See the `arrival_time` description for more details about using timepoints correctly. <br> <br> The `departure_time` field should specify time values whenever possible, including non-binding estimated or interpolated times between timepoints.                                                                                                                                                                                                                                                                                                                                                                        |
| `stop_id`             | ID referencing `stops.stop_id` | **All**              | Identifies the serviced stop. All stops serviced during a trip must have a record in [stop_times.txt](https://developers.google.com/transit/gtfs/reference/#stop_timestxt). Referenced locations must be stops, not stations or station entrances. A stop may be serviced multiple times in the same trip, and multiple trips and routes may service the same stop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `stop_sequence`       | Non-negative integer           | **All**              | Order of stops for a particular trip. The values must increase along the trip but do not need to be consecutive. <br> <br> <em>Example: The first location on the trip could have a `stop_sequence`=`1`, the second location on the trip could have a `stop_sequence`=`23`, the third location could have a `stop_sequence`=`40`, and so on.</em>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stop_headsign`       | Text                           | **GTFS Regional**    | Text that appears on signage identifying the trip&apos;s destination to riders. This field overrides the default `trips.trip_headsign` when the headsign changes between stops. If the headsign is displayed for an entire trip, use `trips.trip_headsign` instead. <br /> <br />A `stop_headsign` value specified for one `stop_time` does not apply to subsequent `stop_time`s in the same trip. <br> &#x2139;GTFS Regional specifies the stop_headsign for each stop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `pickup_type`         | Enum                           | **All**              | Indicates pickup method. Valid options are: <br> <br> `0` or empty - Regularly scheduled pickup. <br> `1` - No pickup available. <br> `2` - Must phone agency to arrange pickup. <br> `3` - Must coordinate with driver to arrange pickup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `drop_off_type`       | Enum                           | **All**              | Indicates drop off method. Valid options are: <br> <br> `0` or empty - Regularly scheduled drop off. <br> `1` - No drop off available. <br> `2` - Must phone agency to arrange drop off. <br> `3` - Must coordinate with driver to arrange drop off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `shape_dist_traveled` | Non-negative float             | GTFS Regional        | Actual distance travelled along the associated shape, from the first stop to the stop specified in this record. This field specifies how much of the shape to draw between any two stops during a trip. Must be in the same units used in [shapes.txt](https://developers.google.com/transit/gtfs/reference/#shapestxt). Values used for `shape_dist_traveled` must increase along with `stop_sequence`; they cannot be used to show reverse travel along a route. <br> <br> <em>Example: If a bus travels a distance of 5.25 kilometers from the start of the shape to the stop,`shape_dist_traveled`=`5.25`.</em>                                                                                                                                                                                                                                                                                                                                                                                           |
| `timepoint`           | Enum                           | **GTFS Regional**    | Indicates if arrival and departure times for a stop are strictly adhered to by the vehicle or if they are instead approximate and/or interpolated times. This field allows a GTFS producer to provide interpolated stop-times, while indicating that the times are approximate. Valid options are: <br> <br> `0` - Times are considered approximate. <br> `1` or empty - Times are considered exact.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |


{{% warning %}} Stop\_times.txt is usually the largest file in a GTFS feed. Depending on the hardware and
programming language, it can be computationally intensive to read all the data. Make sure you read this file in an
efficient way (for example by caching data, not reading the entire file into memory, ...). {{% /warning %}}

The following excerpt shows some stop\_times from a GTFS Regional feed.

```xml
trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled,timepoint
        141010000961947846,08:30:00,08:30:00,9022014017767002,1,Borås,3,1,0,1
        141010000961947846,08:32:00,08:32:00,9022014017513002,2,Borås,3,3,794,1
        141010000961947846,08:32:51,08:32:51,9022014017516002,3,Borås,3,3,1071,0
        141010000961947846,08:34:27,08:34:27,9022014017568002,4,Borås,3,3,1620.12,0
```

### stops.txt

| Field Name       | Type                           | Present            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------------|:-------------------------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `stop_id`        | ID                             | **All**            | Identifies a stop, station, or station entrance. The term "station entrance" refers to both station entrances and station exits. Stops, stations or station entrances are collectively referred to as locations. Multiple routes may use the same stop.                                                                                                                                                                                                                                                                                                    |
| `stop_name`      | Text                           | **All**            | Name of the location. Use a name that people will understand in the local and tourist vernacular. When the location is a boarding area (`location_type=4`), the `stop_name` should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER).                                                                                                                       |
| `stop_lat`       | Latitude                       | **All**            | Latitude of the location. Conditionally Required: <br>• **Required** for locations which are stops (`location_type=0`), stations (`location_type=1`) or entrances/exits (`location_type=2`). <br>• Optional for locations which are generic nodes (`location_type=3`) or boarding areas (`location_type=4`).                                                                                                                                                                                                                                               |
| `stop_lon`       | Longitude                      | **All**            | Longitude of the location. Conditionally Required: <br>• **Required** for locations which are stops (`location_type=0`), stations (`location_type=1`) or entrances/exits (`location_type=2`). <br>• Optional for locations which are generic nodes (`location_type=3`) or boarding areas (`location_type=4`).                                                                                                                                                                                                                                              |
| `location_type`  | Enum                           | **All**            | Type of the location: <br>• `0` (or blank): **Stop** (or **Platform**). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a `parent_station`. <br>• `1`: **Station**. A physical structure or area that contains one or more platform. <br>• `2`: **Entrance/Exit**. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it can be linked by pathways to both, but the data provider must pick one of them as parent. |
| `parent_station` | ID referencing `stops.stop_id` | GTFS Regional only | Defines hierarchy between the differentlocations defined in `stops.txt`. It contains the ID of the parent location, as followed: <br>• **Stop/platform** (`location_type=0`): the `parent_station` field contains the ID of a station. <br>• **Station** (`location_type=1`): this field must be empty. <br>• **Entrance/exit** (`location_type=2`) or **generic node** (`location_type=3`): the `parent_station` field contains the ID of a station (`location_type=1`)                                                                                   |
| `platform_code`  | Text                           | GTFS Regional only | Platform identifier for a platform stop (a stop belonging to a station).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

```text
stop_id,stop_name,stop_lat,stop_lon,location_type,parent_station,platform_code
9021014016110000,BruksvÃ¤gen,57.828220,12.014754,1,,
9021014016113000,IdrottsvÃ¤gen,57.837484,12.014661,1,,
9021014016118000,Surte kyrka,57.831229,12.013882,1,,
9021014016212000,SkolvÃ¤gen,57.848549,12.014318,1,,
```

### calendar.txt

| Field Name   | Type | Present | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-------------|:-----|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `service_id` | ID   | **All** | Uniquely identifies a set of dates when service is available for one or more routes. Each `service_id` value can appear at most once in a [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt) file.                                                                                                                                                                                                       |
| `monday`     | Enum | **All** | Indicates whether the service operates on all Mondays in the date range specified by the `start_date` and `end_date` fields. Note that exceptions for particular dates may be listed in [calendar\_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt). Valid options are:  `1` - Service is available for all Mondays in the date range. `0` - Service is not available for Mondays in the date range. |
| `tuesday`    | Enum | **All** | Functions in the same way as `monday` except applies to Tuesdays                                                                                                                                                                                                                                                                                                                                                                        |
| `wednesday`  | Enum | **All** | Functions in the same way as `monday` except applies to Wednesdays                                                                                                                                                                                                                                                                                                                                                                      |
| `thursday`   | Enum | **All** | Functions in the same way as `monday` except applies to Thursdays                                                                                                                                                                                                                                                                                                                                                                       |
| `friday`     | Enum | **All** | Functions in the same way as `monday` except applies to Fridays                                                                                                                                                                                                                                                                                                                                                                         |
| `saturday`   | Enum | **All** | Functions in the same way as `monday` except applies to Saturdays.                                                                                                                                                                                                                                                                                                                                                                      |
| `sunday`     | Enum | **All** | Functions in the same way as `monday` except applies to Sundays.                                                                                                                                                                                                                                                                                                                                                                        |
| `start_date` | Date | **All** | Start service day for the service interval.                                                                                                                                                                                                                                                                                                                                                                                             |
| `end_date`   | Date | **All** | End service day for the service interval. This service day is included in the interval.                                                                                                                                                                                                                                                                                                                                                 |

{{% info %}} Trafiklab feeds use the calendar.txt file to define the periods during which lines are
operated/valid. The actual operating days are defined in calendar\_dates.txt. {{% /info %}}

```text
service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date
1,0,0,0,0,0,0,0,20200221,20200612
2,0,0,0,0,0,0,0,20200222,20200613
3,0,0,0,0,0,0,0,20200223,20200614
4,0,0,0,0,0,0,0,20200615,20201211
```

### calendar\_dates.txt

| Field Name       | Type                                                        | Present | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-----------------|:------------------------------------------------------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `service_id`     | ID referencing `calendar.service_id` and `trips.service_id` | **All** | Identifies a set of dates when a service exception occurs for one or more routes. Each (`service_id`, `date`) pair can only appear once in [calendar_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt) if using [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt) and [calendar_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt) in conjunction. The information in [calendar_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt) modifies the service information specified in [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt)                                                                           |
| `date`           | Enum                                                        | **All** | Date when service exception occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `exception_type` | Enum                                                        | **All** | Indicates whether service is available on the date specified in the date field. Valid options are: <br> <br> `1` - Service has been added for the specified date. <br> `2` - Service has been removed for the specified date. <br> <br> <em>Example: Suppose a route has one set of trips available on holidays and another set of trips available on all other days. One `service_id` could correspond to the regular service schedule and another `service_id` could correspond to the holiday schedule. For a particular holiday, the [calendar_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt) file could be used to add the holiday to the holiday `service_id` and to remove the holiday from the regular `service_id` schedule. </em> |

```text
service_id,date,exception_type
1,20200221,1
1,20200224,1
1,20200225,1
1,20200226,1
```

### shapes.txt

| Field Name            | Type                 | Present           | Description                                                                                                                                                                                                                                                                                                                |
|:----------------------|:---------------------|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `shape_id`            | ID                   | **GTFS Regional** | Identifies a shape.                                                                                                                                                                                                                                                                                                        |
| `shape_pt_lat`        | Latitude             | **GTFS Regional** | Latitude of a shape point. Each record in [shapes.txt](https://developers.google.com/transit/gtfs/reference/#shapestxt) represent a shape point used to define the shape.                                                                                                                                                  |
| `shape_pt_lon`        | Longitude            | **GTFS Regional** | Longitude of a shape point.                                                                                                                                                                                                                                                                                                |
| `shape_pt_sequence`   | Non-negative integer | **GTFS Regional** | Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive.                                                                                                                                                                                       |
| `shape_dist_traveled` | Non-negative float   | **GTFS Regional** | Actual distance traveled along the shape from the first shape point to the point specified in this record. Used by trip planners to show the correct portion of the shape on a map. Values must increase along with `shape_pt_sequence`; they cannot be used to show reverse travel along a route. Distance in kilometres. |

```text
shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled
1,57.927181,12.529311,1,0
1,57.927172,12.529295,2,0
1,57.927397,12.529314,3,24.31
1,57.927398,12.529364,4,27.89
```

### transfers.txt

| Field Name          | Type                           | Present | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------------------|:-------------------------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `from_stop_id`      | ID referencing `stops.stop_id` | **All** | Identifies a stop or station where a connection between routes begins. If this field refers to a station, the transfer rule applies to all its child stops.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `to_stop_id`        | ID referencing `stops.stop_id` | **All** | Identifies a stop or station where a connection between routes ends. If this field refers to a station, the transfer rule applies to all child stops.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `transfer_type`     | Enum                           | **All** | Indicates the type of connection for the specified (`from_stop_id`, `to_stop_id`) pair. Valid options are: <br> <br> `0` or empty - Recommended transfer point between routes. <br> `1` - Timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one and leave sufficient time for a rider to transfer between routes. <br> `2` - Transfer requires a minimum amount of time between arrival and departure to ensure a connection. The time required to transfer is specified by `min_transfer_time`. <br> `3` - Transfers are not possible between routes at the location. |
| `min_transfer_time` | Non-negative integer           | All     | Amount of time, in seconds, that must be available to permit a transfer between routes at the specified stops. The `min_transfer_time` should be sufficient to permit a typical rider to move between the two stops, including buffer time to allow for schedule variance on each route.                                                                                                                                                                                                                                                                                                                                 |
| `from_trip_id`      | ID referencing `trips.trip_id` | All     | Identifies a trip where a connection between trips starts. If empty, this rule applies for all trips.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `to_trip_id`        | ID referencing `trips.trip_id` | All     | Identifies a trip where a connection between trips ends. If empty, this rule applies for all trips.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  

```text
from_stop_id,to_stop_id,transfer_type,min_transfer_time,from_trip_id,to_trip_id
9022014061616002,9022014061616002,1,,141010000981658971,141010000967489295
9022014080420002,9022014080420002,1,,141010000981659030,141010000981658971
9022014080437002,9022014080437002,1,,141010000981659030,141010000981664702
9022014080437002,9022014080437002,1,,141010000981659030,141010000981664817
```

</div>

## GTFS Extensions

Both GTFS Sverige 2 and GTFS Regional uses some
of [the GTFS Extensions](https://developers.google.com/transit/gtfs/reference/gtfs-extensions).
These extensions are not part of the specification, but are additions to offer additional details.

### Extended Route Types

[Extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types) allow for more
specific transport modes to be used. GTFS Sverige and GTFS Regional does not use the standard one digit GTFS route
types, but only uses
extended route types.

The following list shows the most used transport modes for GTFS Sverige and GTFS Regional. This is a non-extensive list,
only meant to give an idea of the
types you should support. You should still be able to handle the other types in a graceful way, as new traffic may make
use of them without prior warning.

| Code | Name                       | Example                                                     |
|:-----|:---------------------------|:------------------------------------------------------------|
| 100  | Railway Service            |                                                             |
| 101  | High Speed Rail Service    | X2000                                                       |
| 102  | Long Distance Rail Service | Mälartåg                                                    |
| 105  | Sleeper Rail Service       | Night train (Nattåg)                                        |
| 106  | Regional Rail Service      | Commuter trains (Pendeltåg)                                 |
| 401  | Metro Service              | Tunnelbanan Stockholm                                       |
| 700  | Bus Service                |                                                             |
| 702  | Express Bus Service        |                                                             |
| 717  | Share Taxi Service         | Advance order traffic (Förbeställningstrafik)               |
| 900  | Tram Service               | Trams in Göteborg                                           |
| 1000 | Water Transport Service    | SL Pendelbåt, Stockholm-Helsinki                            |
| 1501 | Communal Taxi Service      | Buses with advance order conditions (Förbeställningstrafik) |

A complete list of all route types can be found
at [https://developers.google.com/transit/gtfs/reference/extended-route-types](https://developers.google.com/transit/gtfs/reference/extended-route-types)
.

### Trip-to-trip transfers

GTFS Sverige 2 and GTFS Regional includes trip-to-trip transfers, which are detailed transfer rules that provide
additional details on
which transfers are possible, and how long they take.

{{% info %}}
**Trip-to-trip transfers used to be an extension** to the GTFS standard, but [this extension has been
formally adopted](https://github.com/google/transit/pull/284) into the GTFS standard in October 2021.
{{% /info %}}

[Trip to trip transfers ](https://developers.google.com/transit/gtfs/reference/gtfs-extensions#TripToTripTransfers)make
use of the `from_trip_id`  and `to_trip_id` columns in the transfers.txt file.

From Googles documentation:
The `from_trip_id` and `to_trip_id` fields can contain a `trip_id`, as specified by `trips.txt`. If `from_trip_id` is
specified, the transfer will only apply to the arriving trip with the given trip id, at the given `from_stop_id`. If
`to_trip_id` is specified, the transfer will only apply to the departing trip with the given trip id, at the given
`to_stop_id`.


## Realtime GTFS files
Realtime data refers to elements defined in the [static data](#static-gtfs-files). You therefore need to download both 
the static dataset and the realtime files if you want to make use of Realtime GTFS.  

{{% info %}} We will only discuss the general working and contents of GTFS Realtime feeds. You can find the
complete technical specification
at [https://developers.google.com/transit/gtfs-realtime/](https://developers.google.com/transit/gtfs-realtime/).
{{% /info %}}

{{% warning %}} GTFS Realtime communicates deviations from the data in the static GTFS file. You need both in
order to create realtime timetables. {{% /warning %}}

The GTFS Realtime standard uses
the [protobuf format](/docs/using-trafiklab-data/the-protobuf-file-format) to transfer compact messages
which describe deviations between the
real world and the schedules for a public transport network. There are 3 different feeds, each of which provides their
own type of information.

### ServiceAlerts

ServiceAlerts provide information about incidents, planned maintenance, ... which affect more than one or a couple of
trips. They can describe a closed station, incidents like electricity failures or defect trains, extra services for
certain events, ... . They typically contain similar information as the messages shown on digital signs in stations.
Usually a header, description and link are provided, along with a cause and an effect (provided as an enum). Service
alerts can be limited in time or to certain agencies, trips, stops, transport types, ...

### TripUpdates

TripUpdates provide information about deviations between the scheduled timetable of a trip and the real world. This can
be a delay, a vehicle running early, a partial cancellation, a platform change, ... . Each TripUpdates file contains
multiple TripDescriptors, each of which describes deviations in a trip. If a scheduled trip isn't present in a
TripUpdates file, this can both mean that there are no delays, or that no information is available.

### VehicleUpdates

VehicleUpdates contain realtime GPS positions of public transport vehicles. These allow you to see where a vehicle is
located, along with its speed and bearing. These can be used to show vehicles on a map, to analyze traffic congestion,
...

### Continue reading

{{% page-ref page="/docs/using-trafiklab-data/the-protobuf-file-format" %}}

<br>

## GTFS basics

### What is GTFS?

The **General Transit Feed Specification** is a file format which originally was developed by Google in 2006. It
combines all the data in one compact file. This means you can download a single file to get timetable information for
the entirety of Sweden. The GTFS standard defines files which must be present in the dataset, and files which are
optional. In this guide we will only discuss the files which are present in the Trafiklab datasets.

The GTFS Standard consists of 2 parts: static and real-time data. In the following sections, we will help you to get
started with both.

### How does GTFS Work?

A GTFS file is a zip archive that contains several \*.txt files. You can compare this archive file with a database. The
files inside the archive contain Comma Separated Values (CSV) data, meaning they are easy to read, both for computers
and humans. Each file contains all the instances of a certain type, just like a database table. For example, one file
contains all the routes, another file contains all the stops. The files are linked together through ids, similar to how
foreign keys work in a database. The image below gives an idea of the structure.
{{% warning %}} GTFS Sverige 2 does not contain a shapes.txt file {{% /warning %}}

![The GTFS model, as used by Trafiklab. Fields which are always present are marked in bold.](/media/2020/05/gtfs-model.png)
The GTFS model contains multiple files, which can be required or optional. The fields in these files can be always
present, present for certain feed (e.g. only in GTFS Regional) or optional. The diagram above shows which fields are
used by Trafiklab. The fields which are always present in a file are marked in bold. The tables marked in green are
required by the GTFS standard, the blue ones are optional files used in the Trafiklab data.

{{% info %}} A GTFS archive forms a database-like structure with every file as one table, and you can import
these CSV files directly into a new database to run queries on them. One example is
the [csv2db](https://csv2db.github.io/) tool, but there are many other ways to achieve this. {{% /info %}}

### How it is linked together

Before diving deeper into what each field means, it's important to understand how transport data is described in the 7
required files.

A certain "path" on which public transport vehicles travel, is called a **route** and defined in routes.txt. A **route**
is provided by a public transport **agency** (defined in agencies.txt), and can be serviced one or more times in a
day. Every **trip** on a route is defined in the trips.txt file.

**Example**: Let's say there is a route "Stockholm - Skövde - Göteborg". There is a train leaving stockholm at 10:00,
12:00, and 16:00. In this case, we have one route with three trips on that route.

{{% warning %}} Different trips on the same route might make use of different stops. {{% /warning %}}

The stops which are made during a trip are defined as **stop times** in stop\_times.txt. A **stop time** does not
contain information about the stop itself: it only links a **trip** to a **stop**, and includes some additional
information such as the time of arrival and departure. Stops itself are defined in the stops.txt file, including
information such as their name, location and entrances.

**Example**: Let's say there is a trip on the route "Stockholm - Skövde - Göteborg" leaving at 10:00. The GTFS file
would contain the trip, 3 stops, and 3 stop\_times to link the stops to the trip.

### When should I use GTFS?

A dataset like GTFS is the opposite of an API like ResRobot. Each has its own benefits and drawbacks. When you want to
create a simple app, or let users search for the next departure from your website, an API is easier to use. However,
when you want to analyze data, an API would need millions of requests compared to a single GTFS file that has all the
data.

| Well suited for                                                                | Not so suited for                                   |
|:-------------------------------------------------------------------------------|:----------------------------------------------------|
| Analysing (real-time) transport data                                           | Quickly getting the next departures from a stop     |
| Building your own route-planner or API                                         | Quickly calculating a route from A to B             |
| Getting a list of all public transport stop-areas for an operator or a country | Projects where large files (&gt;25MB) can't be used |
| Getting the live position of all public transport vehicles                     |                                                     |

{{% info %}} There are hundreds of libraries, examples and demos for GTFS. You can find some
at [https://github.com/andredarcie/awesome-gtfs](https://github.com/andredarcie/awesome-gtfs)
and [https://github.com/CUTR-at-USF/awesome-transit](https://github.com/CUTR-at-USF/awesome-transit). {{% /info %}}