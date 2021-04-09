---
title: "Skånetrafiken API shutting down, ResRobot affected"
date: "2021-02-20"
layout: info
---

# Skånetrafiken real-time data dissapearing from ResRobot

On March 31st Skånetrafiken will be shutting down their realtime API. As Resrobot Stolptidtabeller uses this API, this
means that realtime information for Skånetrafiken will no longer be present in the ResRobot Stolptidtabeller data. The
scheduled (static) data will still be present, and ResRobot Stolptidtabeller will continue working.

## How does this affect you?

This will not affect the working of your applications, as the API response-structure remains unchanged. Departures
operated by Skånetrafiken will no longer include realtime data. Train departures will continue having realtime data as
this data is provided by Trafikverket.

## When will this change take effect?

This data will no longer be available starting March 31st.

## What are the alternatives?

We offer realtime data of much higher quality through the GTFS Regional Realtime dataset. This dataset includes realtime
delays and GPS positions for Skånetrafiken. You might need to use additional software, such as OpenTripPlanner, to
access this realtime data through an API. We even offer some examples such
as [a GTFS Timetable API](https://github.com/trafiklab/gtfs-examples/tree/master/python/gtfsToTimetableApi) which
includes realtime and vehicle position data. You can run these examples instantly using our GTFS and GTFS-RT feeds.

If you have any more questions, do not hesitate to contact us at info@trafiklab.se, or to open a support issue at
support.trafiklab.se.

Regards, Team Trafiklab