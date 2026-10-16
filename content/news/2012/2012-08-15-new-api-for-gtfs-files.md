---
title: "New API for GTFS files"
date: 2012-08-15

---
In connection with Sweden Social Web Camp we are launching a new API on Trafiklab. Through the new API you can download information about all planned public transport in Sweden in GTFS format. GTFS stands for General Transit Feed Specification and is an international standard for public transport information.

We have received several requests for access to the collected information in order to create different kinds of services. Based on the needs of these parties and international practice, we have chosen to make the information available in the GTFS (General Transit Feed Specification) file format. There are a number of open source tools that handle this format, and we at Trafiklab see this as a big step forward towards more open and easily accessible information about all public transport in Sweden.

One example of what you can do with the GTFS files is the project restidskarta, created by Hannes. With this application you can get a clear overview of how far you can travel by public transport from a given point in Sweden. The work of making the information available through GTFS files is supported by Vinnova.

## Samtrafiken - a hub for information about Swedish public transport

The information published through the new API comes from Samtrafiken i Sverige AB (which is also behind Trafiklab). Since the turn of the year, Samtrafiken has been responsible for collecting information about planned public transport (timetables) for all public transport operated in Sweden. This is gathered in a _common traffic information system_ (GTI). The assignment is regulated by a regulation from Transportstyrelsen and is a consequence of new legislation for public transport in Sweden. Until now, Samtrafiken has only been able to make the information available through the national journey planner ResRobot, in apps and through an  API for the journey planner. Since the turn of the year, however, we have been working to find a way to make the information available in a way that doesn't require queries to ResRobot, which has now resulted in this API.
