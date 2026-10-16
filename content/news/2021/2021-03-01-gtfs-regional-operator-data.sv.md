---
title: "Operatörsdata i GTFS Regional"
date: "2021-03-01"

image: /media/2021/01/bus-patrik-carlberg-unsplash.jpg
image_credit: Patrik Carlberg, Unsplash
---

Under de kommande dagarna börjar vi publicera nya data i datasetet GTFS Regional. De nya datan visar vilken
operatör som kör varje tur, vilket öppnar nya möjligheter och användningsfall som inte var möjliga tidigare. Den nya
filen har funnits som en valfri fil i GTFS-specifikationen ett tag, och nu är vi redo att börja
publicera dessa data.

Detta påverkar GTFS Regional Static-API:et på följande sätt:

- En ny fil, attributions.txt, läggs till i alla GTFS-exporter.
- Filen attributions.txt innehåller en koppling mellan trip_ids och operatörsnamn enligt GTFS-specifikationen.

## Hur påverkar detta dig?

Detta bör inte påverka dig eller dina befintliga applikationer. Nya eller uppdaterade applikationer kan använda de nya datan.
Om din applikation däremot inte kan hantera nya filer i GTFS-arkivet kan du behöva uppdatera din applikation
för att den ska fortsätta fungera. Om ändringen kräver att du uppdaterar din applikation rekommenderar vi starkt att du
går över till ett arbetssätt där filer som din applikation inte känner till ignoreras.

## När blir dessa data tillgängliga?

De släpps någon av de kommande dagarna.

Om du har fler frågor, tveka inte att kontakta oss på info@trafiklab.se eller att skapa ett supportärende på
support.trafiklab.se.

Med vänliga hälsningar, Team Trafiklab

