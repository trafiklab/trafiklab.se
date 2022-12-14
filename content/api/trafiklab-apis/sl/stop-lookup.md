---
title: SL Stop lookup v1.0 (Platsuppslag)
weight: 300
date: 2014-03-14
aliases:
- /api/sl-platsuppslag
- /api/sl-platsuppslag/dokumentation
- /api/sl-platsuppslag/nivaer
- /api/sl-platsuppslag/konsol
- /node/12617
- /node/12617/dokumentation
- /node/12617/nivaer
- /node/12617/konsol

---

## Beskrivning

Med detta API kan du få information om en plats genom att skicka in delar av platsens namn. Du kan välja mellan att bara
söka efter hållplatsområden eller hållplatser, adresser och platser.

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website. {{% /info %}}

## URL

`https://api.sl.se/api2/typeahead.<FORMAT>?key=<DIN NYCKEL>&searchstring=<SÖKORD>&stationsonly=<ENDAST STATIONER>&maxresults<MAX ANTAL SVAR>`

## Format

Json eller xml enligt ändelse till serviceanropet.

## Parametrar

| Namn         | Datatyp | Tvingande | Beskrivning                                                                                                                                                                                                                                                                                   |
|--------------|---------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key          | String  | Ja        | Din API nyckel.                                                                                                                                                                                                                                                                               |
| SearchString | String  | Ja        | Söksträngen. (Max 20 tecken)                                                                                                                                                                                                                                                                  |
| StationsOnly | Boolean | Nej       | Om ”True” returneras endast hållplatser. True = default.                                                                                                                                                                                                                                      |
| MaxResults   | Integer | Nej       | Maximalt antal resultat som önskas. 10 är default, det går inte att få mer än 50.                                                                                                                                                                                                             |
| type         | String  | Nej       | Typfilter för platser: <ul><li>S: sök efter endast stationer <li>P: Sök efter endast POI <li>A: Sök endast efter adresser <li>SP: Sök efter stationer och POI <li>SA: Sök endas efter stationer och Adresser <li>AP: Sök endast på adresser och POI <li>ALL: adresser, stationer och POI</ul> |

## Resultat

### Svarsstruktur

| Namn          | Datatyp | Beskrivning                                                                                             |
|---------------|---------|---------------------------------------------------------------------------------------------------------|
| StatusCode    | Integer | Innehåller statuskod för det eventuella meddelandet.                                                    |
| Message       | String  | Innehåller eventuellt anropsrelaterade meddelanden som t.ex. felmeddelanden. Se ”Felmeddelanden” nedan. |
| ExecutionTime | Long    | Anger hur lång tid (i ms) det tog för servern att generera svaret.                                      |
| ResponseData  | Sites   | Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.                                        |

### Svarsdata

| Namn  | Datatyp | Beskrivning                                        |
|-------|---------|----------------------------------------------------|
| Sites | List    | Lista med de platser som hittats. Se ”Site” nedan. |

#### Site

| Namn   | Datatyp | Beskrivning                                                         |
|--------|---------|---------------------------------------------------------------------|
| Name   | String  | Namnet på platsen.                                                  |
| SiteId | Integer | Id för hållplatsområde.                                             |
| Type   | String  | Typ av plats: ”Station”, ”Address” eller ”Poi” (Point of interest). |
| X      | String  | X-koordinat för placering.                                          |
| Y      | String  | Y-koordinat för placering.                                          |

## Felmeddelanden

Än så länge finns inga felmeddelanden.

## Support

Räcker inte dokumentationen så <a href="http://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de hundratals
inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.

Hittar du fortfarande inte svar på din fråga så <a href="http://kundo.se/org/trafiklabse/">skriv ett eget inlägg på
forumet</a> så hjälper vi dig.
