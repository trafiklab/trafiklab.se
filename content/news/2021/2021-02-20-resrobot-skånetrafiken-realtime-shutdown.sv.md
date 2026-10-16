---
title: "Skånetrafikens API stängs ner, ResRobot påverkas"
date: "2021-02-20"
---

Den 31 mars stänger Skånetrafiken ner sitt realtids-API. Eftersom ResRobot Stolptidtabeller använder detta API innebär
det att realtidsinformation för Skånetrafiken inte längre finns med i datan från ResRobot Stolptidtabeller. Den
planerade (statiska) datan finns kvar, och ResRobot Stolptidtabeller fortsätter att fungera.

## Hur påverkar detta dig?

Detta påverkar inte hur dina applikationer fungerar, eftersom strukturen på API-svaren är oförändrad. Avgångar
som trafikeras av Skånetrafiken kommer inte längre att innehålla realtidsdata. Tågavgångar har fortsatt realtidsdata
eftersom dessa data levereras av Trafikverket.

## När träder ändringen i kraft?

Dessa data är inte längre tillgängliga från och med den 31 mars.

## Vilka alternativ finns?

Vi erbjuder realtidsdata av betydligt högre kvalitet genom datasetet GTFS Regional Realtime. Datasetet innehåller
förseningar i realtid och GPS-positioner för Skånetrafiken. Du kan behöva använda ytterligare programvara, till exempel
OpenTripPlanner, för att komma åt dessa realtidsdata via ett API. Vi erbjuder till och med några exempel, till
exempel [ett GTFS Timetable API](https://github.com/trafiklab/gtfs-examples/tree/master/python/gtfsToTimetableApi) som
innehåller realtidsdata och fordonspositioner. Du kan köra exemplen direkt med våra GTFS- och GTFS-RT-flöden.

Om du har fler frågor, tveka inte att kontakta oss på info@trafiklab.se eller att skapa ett supportärende på
support.trafiklab.se.

Med vänliga hälsningar, Team Trafiklab
