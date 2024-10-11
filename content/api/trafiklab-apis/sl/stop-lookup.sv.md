---
title: SL Stop lookup v1.0 (Platsuppslag)
weight: 200
date: 2014-03-14

---

## Beskrivning

Med detta API kan du få information om en plats genom att skicka in delar av platsens namn. Du kan välja mellan att bara
söka efter hållplatsområden eller hållplatser, adresser och platser.

## URL

`https://journeyplanner.integration.sl.se/v1/typeahead.<FORMAT>?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&searchstring=<QUERY>`

{{% warning %}}
Den tidigare länken `https://api.sl.se/api2/typeahead.<FORMAT>?key=TRAFIKLAB-SLAPI-INTEGRATION-2024&searchstring=<QUERY>` har ändrats den 16:e november, och kommer sluta fungera den 15e mars 2024. 
Parametrar, svarsstrukturer och API nycklar är oförändrade.
{{% /warning %}}

## Format

Json eller xml enligt ändelse till serviceanropet.

## Parametrar

| Namn         | Datatyp | Tvingande | Beskrivning                                                                                                                                                                                                                                                                                   |
|--------------|---------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key          | String  | Ja        | API-nyckeln, `TRAFIKLAB-SLAPI-INTEGRATION-2024` för nya användare eller projekt efter den 1:a oktober 2024.                                                                                                                                                                                   |
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

{{% note %}}
**SL Stop Lookup i kombination med andra APIer**

SiteId-värden som returneras av SL Stop lookup API matchar med SiteId-värden som förväntas av SL Reseplanerare 3.1 API som parameter. Dessa värden förändrades i februari
men matchar fortfarande varandra (förutsatt att båda API:erna nås genom domänen integration.sl.se).

För att kunna använda värdena som returneras av SL Stop Lookup APIet i kombination med SL Transport API så måste du konvertera returvärdet från SL Stop Lookup
API. Detta värde kommer i formen `3BA1CDEFG`, och ska konverteras till ett nummer `ABCDEFG`. Vi rekommenderar dock att använda de siteId-värden som returneras av 
Transport Api `/sites` om möjligt, istället för att kombinera APIer.
{{% /note %}}

## Felmeddelanden

Än så länge finns inga felmeddelanden.

## Support

Räcker inte dokumentationen så <a href="http://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de hundratals
inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.

Hittar du fortfarande inte svar på din fråga så <a href="http://kundo.se/org/trafiklabse/">skriv ett eget inlägg på
forumet</a> så hjälper vi dig.
