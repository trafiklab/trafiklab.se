---
title: "Sneak preview of new journey planning API"
date: 2017-06-22
draft: true

---

**A new test API from SL is now available on Trafiklab. The API is called SL Reseplanerare 3 and contains a number of new features.**

During the summer the new API will be available for test runs, but it will only go into production after the summer. This new API will eventually replace SL Reseplanerare 2, but initially it will only be available for testing and with relatively few calls per key. For a smooth transition, both versions will run in production in parallel for at least 3 months. This means that SL Reseplanerare 2 will be shut down in November 2017 at the earliest. We will get back to you with exact dates after the summer.

Below we describe some highlights of the new API. You can find the full documentation at [trafiklab.se](http://www.trafiklab.se/). There you can also get an API key for the new API, ask questions and leave feedback. We will try to answer questions and handle any bugs on an ongoing basis, but due to summer holidays there may be periods with longer response times.

**New possibilities in Reseplanerare 3**

- Intermediate stops\
  To know which stops are passed during a journey, in version 2 you have to call journeyDetail after a search with trip. In v3 this is no longer necessary; by specifying passlist=1 this information is returned directly by trip.
- Detailed routes\
  The journey's detailed route in the form of geographic coordinates can also be obtained directly from trip/reconstruction/journeyDetail by specifying poly=1.
- Price information\
  In version 3 the actual ticket prices for a journey are presented, not just zone information as before.
- Earlier/later journeys\
  To ”scroll” to earlier and later journeys after a search with trip, you can send the same search, supplemented with a scroll parameter from the previous response, to get the next or previous journeys (see API documentation)
- Share journey\
  The new reconstruction service makes it easier to share a journey result, not just a search (which can give a different result at another time)

**Key level**

During the summer only one key level will be available: ”test”. Allowed calls: 5,000 per month and 15 per minute.
