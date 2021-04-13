---
title: "Operator data in GTFS Regional"
date: "2021-03-01"
layout: info
image: /images/news/train-unsplash.jpg
---

# Operator data in GTFS Regional Static

In the coming days we will start publishing new data in the GTFS Regional dataset. This new data will show which
operator is servicing each trip, which adds possibilities and enables use-cases which were not possible before. This new
file has been defined as an optional file in the GTFS Specification for a while, and we are now ready to start
publishing this data.

This will affect the GTFS Regional Static API in the following way:

- A new file, attributions.txt, will be added to all GTFS exports.
- The attributions.txt file will contain a mapping between trip_ids and operator names according to the GTFS spec.

## How does this affect you?

This should not affect you or your existing applications. New or updated applications can make use of the new data.
However, in case your application cannot handle new files in the GTFS archive, you may need to update your application
to keep it working. If this change requires you to update your application, we strongly urge you to switch to an
approach where files unknown to your application are ignored.

## When will this data be available?

It will be released in one of the coming days.

If you have any more questions, do not hesitate to contact us at info@trafiklab.se, or to open a support issue at
support.trafiklab.se.

Regards, Team Trafiklab
