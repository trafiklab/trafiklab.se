---
title: Static GTFS files
weight: 10
---

## How GTFS works

A GTFS File is a zip file containing multiple text files. Every text file contains all data for one specific data type
(stops, routes, ...) as comma-separated values. These files can be compared to a table in a database, with _foreign
keys_ linking these files together.

{{% info %}} A GTFS archive forms a database-like structure with every file as one table, and you can import
these CSV files directly into a new database to run queries on them. One example is
the [csv2db](https://csv2db.github.io/) tool, but there are many other ways to achieve this. {{% /info %}}

The GTFS standard defines files which must be present in the dataset, and files which are optional. In this guide we
will only discuss the files which are present in the Trafiklab datasets.

### The general structure

![The GTFS model, as used by Trafiklab. Fields which are always present are marked in bold.](/media/2020/05/gtfs-static-model.svg)

The GTFS model contains multiple files, which can be required or optional. The fields in these files can be required,
optionally required, or optional. The diagram above shows which fields are used by Trafiklab. The fields which are
always present in a file are marked in bold. The tables marked in green are required by the GTFS standard, the blue ones
are optional files used in the Trafiklab data.

{{% warning %}} GTFS Sverige 2 does not contain a shapes.txt file {{% /warning %}}

### How it's linked together

Before diving deeper into what each field means, it's important to understand how transport data is described in the 7
required files.

A certain "path" on which public transport vehicles travel, is called a **route** and defined in routes.txt. A **route**
is provided by a public transport **agency** (defined in agencies.txt), and can be serviced one or more times in a
day. Every **trip** on a route is defined in the trips.txt file.

{{% info %}}
**Example**: Let's say there is a route "Stockholm - Skövde - Göteborg". There is a train leaving stockholm at 10:00,
12:00, and 16:00. In this case, we have one route with three trips on that route. {{% /info %}}

The stops which are made during a trip are defined as **stop times** in stop\_times.txt. A **stop time** does not
contain information about the stop itself: it only links a **trip** to a **stop**, and includes some additional
information such as the time of arrival and departure. Stops itself are defined in the stops.txt file, including
information such as their name, location and entrances.

{{% warning %}} Different trips on the same route might make use of different stops. {{% /warning %}}

{{% info %}}
**Example**: Let's say there is a trip on the route "Stockholm - Skövde - Göteborg" leaving at 10:00. The GTFS file
would contain the trip, 3 stops, and 3 stop\_times to link the stops to the trip. {{% /info %}}

## What does each GTFS file contain

{{% warning %}} The content below is based on the official GTFS Specification, developed by the GTFS
community and published
at [https://developers.google.com/transit/gtfs/reference/](https://developers.google.com/transit/gtfs/reference/).

We modified the version below to describe the feeds published by Trafiklab. Fields and files that are not included in
any Trafiklab feed are not described below. For the latest version or in case of conflict, refer to the official
documentation. {{% /warning %}}

### agency.txt

| Field Name | Type | Present | Description |
| :--- | :--- | :--- | :--- |
| `agency_id` | ID | **Always** | Uniquely identifies a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies. |
| `agency_name` | Text | **Always** | Full name of the transit agency. |
| `agency_url` | URL | **Always** | URL of the transit agency. |
| `agency_timezone` | Timezone | **Always** | Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each has the same `agency_timezone`. |

The following excerpt gives some example values for the different fields.

```text
agency_id,agency_name,agency_url,agency_timezone,agency_lang
141010000000001418,Västtrafik,https://www.resrobot.se/,Europe/Stockholm,sv
141010000000001001,Västtrafik Göteborgsområdet AB Lokaltrafik AB,https://www.resrobot.se/,Europe/Stockholm,sv
141010000651668112,MTR Express (Sweden) AB,https://www.resrobot.se/,Europe/Stockholm,sv
141010000452254130,Öresundståg,https://www.resrobot.se/,Europe/Stockholm,sv
```


### routes.txt

| Field Name | Type | Present | Description |
| :--- | :--- | :--- | :--- |
| `route_id` | ID | **Always** | Identifies a route. |
| `agency_id` | ID referencing `agency.agency_id` | **Always** | Agency for the specified route. This field is required when the dataset provides data for routes from more than one agency in [agency.txt](https://developers.google.com/transit/gtfs/reference/#agency), otherwise it is optional. |
| `route_short_name` | Text | **Conditionally**  | Short name of a route. This will often be a short, abstract identifier like "32", "100X", or "Green" that riders use to identify a route, but which doesn't give any indication of what places the route serves. Either `route_short_name` or `route_long_name` must be specified, or potentially both if appropriate. |
| `route_long_name` | Text | **Conditionally**  | Full name of a route. This name is generally more descriptive than the `route_short_name` and often includes the route's destination or stop. Either `route_short_name` or `route_long_name` must be specified, or potentially both if appropriate. |
| `route_type` | Enum | **Always** | Indicates the type of transportation used on a route.  |
| `route_url` | URL | Optional | URL of a web page about the particular route. Should be different from the `agency.agency_url` value. |

The GTFS standard defines 9 route_types, but all Trafiklab feeds make use
of [extended route types](https://developers.google.com/transit/gtfs/reference/extended-route-types). Check the
feed-specific documentation for examples.

{{% page-ref "/apis/trafiklab-apis/gtfs-sverige-2/" "/apis/trafiklab-apis/gtfs-regional/" %}}

The following excerpt shows some example values.

```text
route_id,agency_id,route_short_name,route_long_name,route_type
9011014280200000,141010000000001418,302,,717
9011014374100000,141010000000001418,420,,717
9011014471100000,141010000000001418,711,,700
9011014630400000,141010000000001418,304,,700
```

### trips.txt

| Field Name | Type | Present | Description |
| :--- | :--- | :--- | :--- |
| `route_id` | ID referencing `routes.route_id` | **Always** | Identifies a route. |
| `service_id` | ID referencing `calendar.service_id` or `calendar_dates.service_id` | **Always** | Identifies a set of dates when service is available for one or more routes. |
| `trip_id` | ID | **Always** | Identifies a trip. |
| `trip_headsign` | Text | Optional | Text that appears on signage identifying the trip's destination to riders. Use this field to distinguish between different patterns of service on the same route. If the headsign changes during a trip, `trip_headsign` can be overridden by specifying values for the `stop_times.stop_headsign`. |
| `trip_short_name` | Text | Optional | Public facing text used to identify the trip to riders, for instance, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, leave this field empty. A `trip_short_name` value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations. |
| `direction_id` | Enum | Optional | Indicates the direction of travel for a trip. This field is not used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are:  `0` - Travel in one direction (e.g. outbound travel). `1` - Travel in the opposite direction (e.g. inbound travel). |
| `shape_id` | ID referencing `shapes.shape_id` | GTFS Regional only | Identifies a geospatial shape describing the vehicle travel path for a trip. |

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

<table>
  <thead>
    <tr>
      <th>Field Name</th>
      <th>Type</th>
      <th>Present</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>trip_id</code>
      </td>
      <td>ID referencing <code>trips.trip_id</code>
      </td>
      <td><b>Always</b>
      </td>
      <td>Identifies a trip.</td>
    </tr>
    <tr>
      <td><code>arrival_time</code>
      </td>
      <td>Time</td>
      <td><b>Always</b>
      </td>
      <td>Arrival time at a specific stop for a specific trip on a route. If there
        are not separate times for arrival and departure at a stop, enter the same
        value for <code>arrival_time</code> and <code>departure_time</code>. For times
        occurring after midnight on the service day, enter the time as a value
        greater than 24:00:00 in HH:MM:SS local time for the day on which the trip
        schedule begins.
        <br />
        <br />Scheduled stops where the vehicle strictly adheres to the specified arrival
        and departure times are timepoints. If this stop is not a timepoint, it
        is recommended to provide an estimated or interpolated time. If this is
        not available, arrival_time can be left empty. Further, indicate that interpolated
        times are provided with <code>timepoint</code>=<code>0</code>. If interpolated
        times are indicated with <code>timepoint</code>=<code>0</code>, then time
        points must be indicated with <code>timepoint</code>=<code>1</code>. Provide
        arrival times for all stops that are time points. An arrival time must
        be specified for the first and the last stop in a trip.</td>
    </tr>
    <tr>
      <td><code>departure_time</code>
      </td>
      <td>Time</td>
      <td><b>Always</b>
      </td>
      <td>Departure time from a specific stop for a specific trip on a route. For
        times occurring after midnight on the service day, enter the time as a
        value greater than 24:00:00 in HH:MM:SS local time for the day on which
        the trip schedule begins. If there are not separate times for arrival and
        departure at a stop, enter the same value for <code>arrival_time</code> and <code>departure_time</code>.
        See the <code>arrival_time</code> description for more details about using
        timepoints correctly.
        <br />
        <br />The <code>departure_time</code> field should specify time values whenever
        possible, including non-binding estimated or interpolated times between
        timepoints.</td>
    </tr>
    <tr>
      <td><code>stop_id</code>
      </td>
      <td>ID referencing <code>stops.stop_id</code>
      </td>
      <td><b>Always</b>
      </td>
      <td>Identifies the serviced stop. All stops serviced during a trip must have
        a record in <a href="https://developers.google.com/transit/gtfs/reference/#stop_timestxt">stop_times.txt</a>.
        Referenced locations must be stops, not stations or station entrances.
        A stop may be serviced multiple times in the same trip, and multiple trips
        and routes may service the same stop.</td>
    </tr>
    <tr>
      <td><code>stop_sequence</code>
      </td>
      <td>Non-negative integer</td>
      <td><b>Always</b>
      </td>
      <td>
        <p>Order of stops for a particular trip. The values must increase along the
          trip but do not need to be consecutive.</p>
        <p><em>Example: The first location on the trip could have a <code>stop_sequence</code>=<code>1</code>, the second location on the trip could have a <code>stop_sequence</code>=<code>23</code>, the third location could have a <code>stop_sequence</code>=<code>40</code>, and so on.</em>
        </p>
      </td>
    </tr>
    <tr>
      <td><code>stop_headsign</code></td>
      <td>Text</td>
      <td>GTFS Regional only</td>
      <td>
        <p>Text that appears on signage identifying the trip&apos;s destination to
          riders. This field overrides the default <code>trips.trip_headsign</code> when
          the headsign changes between stops. If the headsign is displayed for an
          entire trip, use <code>trips.trip_headsign</code> instead.
          <br />
          <br />A <code>stop_headsign</code> value specified for one <code>stop_time</code> does
          not apply to subsequent <code>stop_time</code>s in the same trip.</p>
        <p>&#x2139;GTFS Regional specifies the stop_headsign for each stop</p>
      </td>
    </tr>
    <tr>
      <td><code>pickup_type</code>
      </td>
      <td>Enum</td>
      <td><b>Always</b>
      </td>
      <td>Indicates pickup method. Valid options are:
        <br />
        <br /><code>0</code> or empty - Regularly scheduled pickup.
        <br /><code>1</code> - No pickup available.
        <br /><code>2</code> - Must phone agency to arrange pickup.
        <br /><code>3</code> - Must coordinate with driver to arrange pickup.</td>
    </tr>
    <tr>
      <td><code>drop_off_type</code>
      </td>
      <td>Enum</td>
      <td><b>Always</b>
      </td>
      <td>Indicates drop off method. Valid options are:
        <br />
        <br /><code>0</code> or empty - Regularly scheduled drop off.
        <br /><code>1</code> - No drop off available.
        <br /><code>2</code> - Must phone agency to arrange drop off.
        <br /><code>3</code> - Must coordinate with driver to arrange drop off.</td>
    </tr>
    <tr>
      <td><code>shape_dist_traveled</code>
      </td>
      <td>Non-negative float</td>
      <td>GTFS Regional only</td>
      <td>
        <p>Actual distance travelled along the associated shape, from the first stop
          to the stop specified in this record. This field specifies how much of
          the shape to draw between any two stops during a trip. Must be in the same
          units used in <a href="https://developers.google.com/transit/gtfs/reference/#shapestxt">shapes.txt</a>.
          Values used for <code>shape_dist_traveled</code> must increase along with <code>stop_sequence</code>;
          they cannot be used to show reverse travel along a route.</p>
        <p><em>Example: If a bus travels a distance of 5.25 kilometers from the start of the shape to the stop,<code>shape_dist_traveled</code>=<code>5.25</code>.</em>
        </p>
      </td>
    </tr>
    <tr>
      <td><code>timepoint</code>
      </td>
      <td>Enum</td>
      <td>GTFS Regional only</td>
      <td>Indicates if arrival and departure times for a stop are strictly adhered
        to by the vehicle or if they are instead approximate and/or interpolated
        times. This field allows a GTFS producer to provide interpolated stop-times,
        while indicating that the times are approximate. Valid options are:
        <br
        />
        <br /><code>0</code> - Times are considered approximate.
        <br /><code>1</code> or empty - Times are considered exact.</td>
    </tr>
  </tbody>
</table>

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

| Field Name | Type | Present | Description |
| :--- | :--- | :--- | :--- |
| `stop_id` | ID | **Always** | Identifies a stop, station, or station entrance. The term "station entrance" refers to both station entrances and station exits. Stops, stations or station entrances are collectively referred to as locations. Multiple routes may use the same stop. |
| `stop_name` | Text | **Always** | Name of the location. Use a name that people will understand in the local and tourist vernacular. When the location is a boarding area (`location_type=4`), the `stop_name` should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER).  |
| `stop_lat` | Latitude | **Always** | Latitude of the location. Conditionally Required: <br>• **Required** for locations which are stops (`location_type=0`), stations (`location_type=1`) or entrances/exits (`location_type=2`). <br>• Optional for locations which are generic nodes (`location_type=3`) or boarding areas (`location_type=4`). |
| `stop_lon` | Longitude | **Always** | Longitude of the location. Conditionally Required: <br>• **Required** for locations which are stops (`location_type=0`), stations (`location_type=1`) or entrances/exits (`location_type=2`). <br>• Optional for locations which are generic nodes (`location_type=3`) or boarding areas (`location_type=4`). |
| `location_type` | Enum | **Always** | Type of the location: <br>• `0` (or blank): **Stop** (or **Platform**). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a `parent_station`. <br>• `1`: **Station**. A physical structure or area that contains one or more platform. <br>• `2`: **Entrance/Exit**. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it can be linked by pathways to both, but the data provider must pick one of them as parent. |
| `parent_station` | ID referencing `stops.stop_id` | GTFS Regional only | Defines hierarchy between the differentlocations defined in `stops.txt`. It contains the ID of the parent location, as followed: <br>• **Stop/platform** (`location_type=0`): the `parent_station` field contains the ID of a station. <br>• **Station** (`location_type=1`): this field must be empty. <br>• **Entrance/exit** (`location_type=2`) or **generic node** (`location_type=3`): the `parent_station` field contains the ID of a station (`location_type=1`) |
| `platform_code`| Text | GTFS Regional only | Platform identifier for a platform stop (a stop belonging to a station). |

```text
stop_id,stop_name,stop_lat,stop_lon,location_type,parent_station,platform_code
9021014016110000,BruksvÃ¤gen,57.828220,12.014754,1,,
9021014016113000,IdrottsvÃ¤gen,57.837484,12.014661,1,,
9021014016118000,Surte kyrka,57.831229,12.013882,1,,
9021014016212000,SkolvÃ¤gen,57.848549,12.014318,1,,
```

### calendar.txt

| Field Name | Type | Present | Description |
| :--- | :--- | :--- | :--- |
| `service_id` | ID | **Always** | Uniquely identifies a set of dates when service is available for one or more routes. Each `service_id` value can appear at most once in a [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt) file. |
| `monday` | Enum | **Always** | Indicates whether the service operates on all Mondays in the date range specified by the `start_date` and `end_date` fields. Note that exceptions for particular dates may be listed in [calendar\_dates.txt](https://developers.google.com/transit/gtfs/reference/#calendar_datestxt). Valid options are:  `1` - Service is available for all Mondays in the date range. `0` - Service is not available for Mondays in the date range. |
| `tuesday` | Enum | **Always** | Functions in the same way as `monday` except applies to Tuesdays |
| `wednesday` | Enum | **Always** | Functions in the same way as `monday` except applies to Wednesdays |
| `thursday` | Enum | **Always** | Functions in the same way as `monday` except applies to Thursdays |
| `friday` | Enum | **Always** | Functions in the same way as `monday` except applies to Fridays |
| `saturday` | Enum | **Always** | Functions in the same way as `monday` except applies to Saturdays. |
| `sunday` | Enum | **Always** | Functions in the same way as `monday` except applies to Sundays. |
| `start_date` | Date | **Always** | Start service day for the service interval. |
| `end_date` | Date | **Always** | End service day for the service interval. This service day is included in the interval. |

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

<table>
  <thead>
    <tr>
      <th>Field Name</th>
      <th>Type</th>
      <th>Present</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>service_id</code>
      </td>
      <td>ID referencing <code>calendar.service_id</code> and <code>trips.service_id</code>
      </td>
      <td><b>Always</b>
      </td>
      <td>Identifies a set of dates when a service exception occurs for one or more
        routes. Each (<code>service_id</code>, <code>date</code>) pair can only
        appear once in <a href="https://developers.google.com/transit/gtfs/reference/#calendar_datestxt">calendar_dates.txt</a> if
        using <a href="https://developers.google.com/transit/gtfs/reference/#calendartxt">calendar.txt</a> and
        <a
        href="https://developers.google.com/transit/gtfs/reference/#calendar_datestxt">calendar_dates.txt</a>in conjunction. The information in <a href="https://developers.google.com/transit/gtfs/reference/#calendar_datestxt">calendar_dates.txt</a> modifies
          the service information specified in <a href="https://developers.google.com/transit/gtfs/reference/#calendartxt">calendar.txt</a>.</td>
    </tr>
    <tr>
      <td><code>date</code>
      </td>
      <td>Date</td>
      <td><b>Always</b>
      </td>
      <td>Date when service exception occurs.</td>
    </tr>
    <tr>
      <td><code>exception_type</code>
      </td>
      <td>Enum</td>
      <td><b>Always</b>
      </td>
      <td>
        <p>Indicates whether service is available on the date specified in the date
          field. Valid options are:
          <br />
          <br /> <code>1</code> - Service has been added for the specified date.
          <br /><code>2</code> - Service has been removed for the specified date.</p>
        <p><em>Example: Suppose a route has one set of trips available on holidays and another set of trips available on all other days. One <code>service_id</code> could correspond to the regular service schedule and another <code>service_id</code> could correspond to the holiday schedule. For a particular holiday, the </em>
          <a
          href="https://developers.google.com/transit/gtfs/reference/#calendar_datestxt"><em>calendar_dates.txt</em>
            </a><em> file could be used to add the holiday to the holiday <code>service_id</code> and to remove the holiday from the regular <code>service_id</code> schedule.</em>
        </p>
      </td>
    </tr>
  </tbody>
</table>

```text
service_id,date,exception_type
1,20200221,1
1,20200224,1
1,20200225,1
1,20200226,1
```

### shapes.txt

<table>
  <thead>
    <tr>
      <th>Field Name</th>
      <th>Type</th>
      <th>Present</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>shape_id</code>
      </td>
      <td>ID</td>
      <td><b>Always</b>
      </td>
      <td>Identifies a shape.</td>
    </tr>
    <tr>
      <td><code>shape_pt_lat</code>
      </td>
      <td>Latitude</td>
      <td><b>Always</b>
      </td>
      <td>Latitude of a shape point. Each record in <a href="https://developers.google.com/transit/gtfs/reference/#shapestxt">shapes.txt</a> represents
        a shape point used to define the shape.</td>
    </tr>
    <tr>
      <td><code>shape_pt_lon</code>
      </td>
      <td>Longitude</td>
      <td><b>Always</b>
      </td>
      <td>Longitude of a shape point.</td>
    </tr>
    <tr>
      <td><code>shape_pt_sequence</code>
      </td>
      <td>Non-negative integer</td>
      <td><b>Always</b>
      </td>
      <td>Sequence in which the shape points connect to form the shape. Values must
        increase along the trip but do not need to be consecutive.</td>
    </tr>
    <tr>
      <td><code>shape_dist_traveled</code>
      </td>
      <td>Non-negative float</td>
      <td><b>Always</b>
      </td>
      <td>
        <p>Actual distance traveled along the shape from the first shape point to
          the point specified in this record. Used by trip planners to show the correct
          portion of the shape on a map. Values must increase along with <code>shape_pt_sequence</code>;
          they cannot be used to show reverse travel along a route. Distance in kilometres.</p>
      </td>
    </tr>
  </tbody>
</table>

```text
shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled
1,57.927181,12.529311,1,0
1,57.927172,12.529295,2,0
1,57.927397,12.529314,3,24.31
1,57.927398,12.529364,4,27.89
```

### transfers.txt

<table>
  <thead>
    <tr>
      <th>Field Name</th>
      <th>Type</th>
      <th>Present</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>from_stop_id</code>
      </td>
      <td>ID referencing <code>stops.stop_id</code>
      </td>
      <td><b>Always</b>
      </td>
      <td>Identifies a stop or station where a connection between routes begins.
        If this field refers to a station, the transfer rule applies to all its
        child stops.</td>
    </tr>
    <tr>
      <td><code>to_stop_id</code>
      </td>
      <td>ID referencing <code>stops.stop_id</code>
      </td>
      <td><b>Always</b>
      </td>
      <td>Identifies a stop or station where a connection between routes ends. If
        this field refers to a station, the transfer rule applies to all child
        stops.</td>
    </tr>
    <tr>
      <td><code>transfer_type</code>
      </td>
      <td>Enum</td>
      <td><b>Always</b>
      </td>
      <td>Indicates the type of connection for the specified (<code>from_stop_id</code>, <code>to_stop_id</code>)
        pair. Valid options are:
        <br />
        <br /> <code>0</code> or empty - Recommended transfer point between routes.
        <br
        /><code>1</code> - Timed transfer point between two routes. The departing
        vehicle is expected to wait for the arriving one and leave sufficient time
        for a rider to transfer between routes.
        <br /><code>2</code> - Transfer requires a minimum amount of time between arrival
        and departure to ensure a connection. The time required to transfer is
        specified by <code>min_transfer_time</code>.
        <br /><code>3</code> - Transfers are not possible between routes at the location.</td>
    </tr>
    <tr>
      <td><code>min_transfer_time</code>
      </td>
      <td>Non-negative integer</td>
      <td>Optional</td>
      <td>Amount of time, in seconds, that must be available to permit a transfer
        between routes at the specified stops. The <code>min_transfer_time</code> should
        be sufficient to permit a typical rider to move between the two stops,
        including buffer time to allow for schedule variance on each route.</td>
    </tr>
    <tr>
      <td><code>from_trip_id</code>
      </td>
      <td>ID referencing <code>trips.trips_id</code>
      </td>
      <td>Optional</td>
      <td>
        <p>Identifies a trip where a connection between trips starts. If empty, this rule applies for all trips.</p>
      </td>
    </tr>
    <tr>
      <td><code>to_trip_id</code>
      </td>
      <td>ID referencing <code>trips.trip_id</code>
      </td>
      <td>Optional</td>
      <td>
        <p>Identifies a trip where a connection between trips ends. If empty, this rule applies for all trips.</p>
      </td>
    </tr>
  </tbody>
</table>

```text
from_stop_id,to_stop_id,transfer_type,min_transfer_time,from_trip_id,to_trip_id
9022014061616002,9022014061616002,1,,141010000981658971,141010000967489295
9022014080420002,9022014080420002,1,,141010000981659030,141010000981658971
9022014080437002,9022014080437002,1,,141010000981659030,141010000981664702
9022014080437002,9022014080437002,1,,141010000981659030,141010000981664817
```
