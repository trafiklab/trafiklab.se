---
title: "Frequently asked questions"
weight: 100
---
## Trafiklab

### Why do I need API keys? Wouldn't it be easier without?

While we agree, we need the API keys in order to be able to offer this data. Every API call and GTFS download costs us
money. Through API keys we can prevent people from downloading the same GTFS file every 15 or 30 minutes, while we are
clear about the fact that it only updates once a day.

Don't worry if you need an upgrade - you'll most likely get it.

### What happens when an API is discontinued?

We rarely discontinue APIs. When a change is coming up, users are notified in good time (often multiple months
before).

## Data

### Vehicles are appearing in the realtime data, even though they aren't present in the static data. Why is this?

There might be a high load on a certain bus line, in which case the operator may decide to send out one or more extra
buses. These buses are not associated with a planned trip, but will still show up in the realtime data.

Vehicle position data can also include parked vehicles, vehicles on their way to their starting point, or on the way
back after their last stop.

### Can I stress test the APIs?

No. If you're wondering if our APIs can handle a certain load, please ask instead.

### Why doesn´t the usage tracker increase when I make requests using my API key? 

Statistics are only updated once a day. Some API´s need up to 48 hours for statistics to become visible for Trafiklab users.

### Why did my request for an API key upgrade get denied?

You will get a message describing the reason when an API key upgrade gets denied. Typically, this is due to magic mirror
solutions wanting to use more than 10.000 API calls per month, or due to using the wrong data type, in which case we
will point out how other data can make your life easier (for example, when using an API for analytics/mass queries
instead of our GTFS/GTFS-RT data)

## I still have questions

Don't hesitate and reach out to us! You can do so by posting to our support
forum: [https://support.trafiklab.se](https://support.trafiklab.se)
