---
title: Förbättringar i GTFS Sverige 2
date: 2018-05-31
aliases:
  - "/post/174432207508/förbättringar-i-gtfs-sverige-2"
draft: true
image: "/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-1.png"
---

 <h2>Hej alla trafiklabbare!</h2>
Från och med 2018-06-18 kommer det ske några förändringar i GTFS Sverige 2. Den kommer nämligen att innehålla två nya extra-filer, trips_technical.txt och routes_technical.txt. Vi kommer även införa förändringar i trip_id och route_id. Våra nya IDn är längre än tidigare och vi vill informera er innan vi driftsätter detta så att ni har tid att vid behov anpassa era applikationer.
Kortfattat så kommer detta hända:


![](/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-1.png)

<h2>Vad är Trips_technical.txt?</h2>
Tanken med trips_technical.txt är att ni med hjälp av den kan få tag på tekniskt turnummer (technical_trip_number) givet en trip_id från GTFS. Ett exempel på användningsområde är att kunna ta technical_trip_number för tåg och söka vidare på annonserad information för tåg i Trafikverkets APIer. Trips_technical.txt är en kommaseparerad fil med två fält enligt nedan:


![](/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-2.jpg)


Ett exempel på förbättring är pendeltågens benämning i trips_short_name och trips_long_name som kommer mer i linje med [GTFS best practice](http://gtfs.org/best-practices/). Rent konkret kommer denna förändring innebärar att pendeltågens tågnummer försvinner från trip_short_name. Det kommer i en övergångsperiod att ligga dubbelt i både trip_short_name och technical_trip_number. Efter övergångsperioden kommer vi att lägga pendeltågens linjenummer i route_long_name istället, t.ex. Pendeltåg 40 istället för bara Pendeltåg som det är idag.
<h2>Vad är Routes_technical.txt?</h2>
Det tekniskta linjenumret (technical_route_number) kan vara till stor hjälp för er när ni vill filtrera ut viss trafik ur hela GTFS-datasetet, t.ex. enbart bussar tillhörande Malmö stadstrafik. Routes_technical.txt är en kommaseparerad fil med två fält enligt nedan:


![](/media/2018/05/2018-05-31-forbattringar-i-gtfs-sverige-2-3.jpg)

<h2>Förändringar i trip_id och route_id</h2>
Nedan kan ni se exempel på hur trip_id och route_id kan se ut efter förändringen.
Viktigt: Vi rekommenderar starkt att **inte **försöka extrahera data ur de olika delarna, t.ex. tekniskt turnummer från pos 9-14 i trip_id, utan se dem som slumpmässiga nummer. För att t.ex. få tekniskt turnummer måste man gå till trips_technical.txt. Strukturen på IDn kan komma att ändras utan förvarningen. Istället ska ni hämta de fält där de ligger, dvs agency.agency_id, trips_technical.technical_trip_id och routes_technical.technical_route_id. Detta enligt GTFS best practice.
Exampel på trip_id: 23334444666666
Pos 1-1 (2) = Class ID for trip id is 2. (Class ID for route id is 1).
Pos 2-4 (333) = Transport authority number
Pos 5-8 (4444) = Technical line number
Pos 9-14 (666666) = Technical trip number or a running number if needed to make the trip unique
Exampel på route_id: 1333444455555
Pos 1-1 (1) = Class ID for route id is 1. (Class ID for trip id is 2).
Pos 2-4 (333) = Transport authority number
Pos 5-8 (4444) = Technical line number
Pos 9-13 (55555) = Running number to make it unique with regards to short name, long name and means-of-transport
Har ni frågor kring detta är ni välkomna att kontakta oss på [här ](http://kundo.se/org/trafiklabse/)
 
