---
title: The protobuf file format
description: How to use binary protocol buffer files in your application
weight: 30
---

### What is the protobuf file format

Protocol buffers is a language-neutral, platform-neutral, extensible mechanism for serializing structured data – think
XML or JSON, but smaller and faster. A protobuf scheme describes once how the data is structured, after which special
generated source code can be used to easily write and read your structured data to and from a variety of data streams
and using a variety of languages. Protobuf is a binary format, and it does not contain any structural information.
Therefore, you will need a scheme (with the structure) and code to deserialize it in order to access the data.

Protobuf was developed by Google in the early 2000's as a way to communicate between systems, and is now used as the
standard format for GTFS-RT as well

### Why protobuf is used for GTFS-RT

Protobuf is the standard for GTFS-RT data. Since all producers use the same protobuf format and scheme, consumers only
have to code an application once, whereafter it is available

When we publish data in realtime, new data is published and fetched every 15 seconds (TripUpdates, ServiceAlerts) or
even every 3 seconds (VehiclePositions). For TripUpdates, this means 5760 updates, per operator, per day. For example,
a file size reduction with 500kb would result in a saving of 2,5gb of data transfer per day, just for this one feed with
one consumer. This is important both for producers, since data transfer can make up a significant part of the hosting
costs, and for consumers such as you, who also have to pay for transfer.

Thanks to its smaller size,protobuf can bring advantages when it comes to decoding performance. This means that systems
can decode and handle messages quicker, which becomes especially important when you want to consume a large number of
feeds.

### Protobuf schemes

A protobuf scheme defines how the information is structured inside. Take a look at this excerpt from the GTFS-RT
protobuf scheme:

```javascript
 // Realtime update for arrival and/or departure events for a given stop on a
// trip. Updates can be supplied for both past and future events.
// The producer is allowed, although not required, to drop past events.
message
StopTimeUpdate
{
    // The update is linked to a specific stop either through stop_sequence or
    // stop_id, so one of the fields below must necessarily be set.
    // See the documentation in TripDescriptor for more information.

    // Must be the same as in stop_times.txt in the corresponding GTFS feed.
    optional
    uint32
    stop_sequence = 1;
    // Must be the same as in stops.txt in the corresponding GTFS feed.
    optional
    string
    stop_id = 4;

    optional
    StopTimeEvent
    arrival = 2;
    optional
    StopTimeEvent
    departure = 3;

    // The relation between this StopTime and the static schedule.
enum
    ScheduleRelationship
    {
        // The vehicle is proceeding in accordance with its static schedule of
        // stops, although not necessarily according to the times of the schedule.
        // At least one of arrival and departure must be provided. If the schedule
        // for this stop contains both arrival and departure times then so must
        // this update.
        SCHEDULED = 0;

        // The stop is skipped, i.e., the vehicle will not stop at this stop.
        // Arrival and departure are optional.
        SKIPPED = 1;

        // No data is given for this stop. The main intention for this value is to
        // give the predictions only for part of a trip, i.e., if the last update
        // for a trip has a NO_DATA specifier, then StopTimes for the rest of the
        // stops in the trip are considered to be unspecified as well.
        // Neither arrival nor departure should be supplied.
        NO_DATA = 2;
    }
    optional
    ScheduleRelationship
    schedule_relationship = 5
        [
default
    = SCHEDULED
]
    ;

    // The extensions namespace allows 3rd-party developers to extend the
    // GTFS Realtime Specification in order to add and evaluate new features
    // and modifications to the spec.
    extensions
    1000
    to
    1999;
}

```

Every field is described: whether it is optional, the data type, and the position in the binary data (which is
needed to decode the file). Note that these schemes are not meant as a specification for the information/content, but
as a specification for the serialization and deserialisation. If you are looking for the GTFS-RT specification (not the
protobuf scheme), you can find it [here](https://developers.google.com/transit/gtfs-realtime).

{{% info %}} The GTFS Realtime protobuf scheme can be found
here: [https://developers.google.com/transit/gtfs-realtime/gtfs-realtime-proto](https://developers.google.com/transit/gtfs-realtime/gtfs-realtime-proto)
([direct download](https://developers.google.com/transit/gtfs-realtime/gtfs-realtime.proto))
{{% /info %}}

### Decoding a protobuf file

When you decode a protbuf file, you end up with structured data. The exact datastructures which are used to hold this
data can differ between programming languages (for example List vs Arrays), but the content will be the same. Below
you can see a fragment of a GTFS-RT TripUpdate file after it has been decoded from protobuf.

TripUpdate.pb, fragment deserialized to jsonld:

```javascript
header
{
    gtfs_realtime_version: "2.0"
    incrementality: FULL_DATASET
    timestamp: 1608130478
}
entity
{
  id: "205330500466160320"
  trip_update
  {
    trip
    {
      trip_id: "205330000096654402"
      start_date: "20201216"
      schedule_relationship: SCHEDULED
    }
    stop_time_update
    {
      stop_sequence: 49
      arrival
      {
        delay: 173
        time: 1608129893
        uncertainty: 0
      }
      departure
      {
        delay: 190
        time: 1608129910
        uncertainty: 0
      }
      stop_id: "9022020526118002"
    }
  }
}
```

There are protobuf libraries and tools for almost all programming languages. You can find some examples for Java, Python
and C\# below.

* Java
  example: [https://developers.google.com/protocol-buffers/docs/javatutorial](https://developers.google.com/protocol-buffers/docs/javatutorial)
* Python
  example: [https://developers.google.com/protocol-buffers/docs/pythontutorial](https://developers.google.com/protocol-buffers/docs/pythontutorial)
* C\#
  example: [https://developers.google.com/protocol-buffers/docs/csharptutorial](https://developers.google.com/protocol-buffers/docs/csharptutorial)

### Further reading

* Googles official protocol buffer
  documentation: [https://developers.google.com/protocol-buffers](https://developers.google.com/protocol-buffers)
* Protocol buffers on
  Wikipedia: [https://en.wikipedia.org/wiki/Protocol\_Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers)
