---
title: SL Service alerts v2.0 (Störningsinformation 2)
weight: 500
date: 2014-03-14
aliases:

- /api/sl-storningsinformation-2
- /api/sl-storningsinformation-2/documentation
- /api/sl-storningsinformation-2/nivaer
- /api/sl-storningsinformation-2/console
- /api/sl-storningsinformation-2/konsol
- /node/12605
- /node/12605/documentation
- /node/12605/nivaer
- /node/12605/console
- /node/12605/konsol

---
<h2>Beskrivning</h2>
Med detta API kan du få fram information om aktuella och planerade störningar i SL-trafiken. Med API ‘et kan du ställa 
frågor om störningar på till exempel en viss linje eller ett visst trafikslag. Svaret består av störningsmeddelanden med 
viss metainformation.

För att se informationen som returneras av detta API, se <a href="https://api.sl.se/ta">https://api.sl.se/ta</a> 
(detta är en störningsinformationssida som är anpassad för SL:s interna behov och inte avsedd att användas av 
resenärerna).

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website. {{% /info %}}

Om ingen av parametrarna ”TransportMode”, ”LineNumber” och ”SiteId” skickas med anropet skickas samtliga avvikelser 
tillbaks som svar.

Är du intresserad av Störningar här och nu i SL trafiken se 
[https://sl.se/sv/find/?query=Störningsinformation](https://sl.se/sv/find/?query=Störningsinformation)

### Metod deviations

#### URL

`https://api.sl.se/api2/deviations.<FORMAT>?key=<DIN API NYCKEL>&transportMode=<TRANSPORTMODE>&lineNumber=<LINENUMBER>&siteId=<SITEID>&fromDate=<FROMDATE>&toDate=<TODATE>`

### API-nyckelnivåer

| Nivå   | Max anrop/minut | Max anrop/månad |
|--------|-----------------|-----------------|
| Brons  | 30              | 10 000          |
| Silver | 60              | 100 000         |
| Guld   |                 | Efter behov     |

#### Format

Json eller xml enligt ändelse till serviceanropet.

#### Parametrar

| Namn          | Typ     | Tvingande                                | Beskrivning                                                                                     |
|---------------|---------|------------------------------------------|-------------------------------------------------------------------------------------------------|
| TransportMode | String  | Nej                                      | Aktuella trafikslag. Tillåtna värden är bus, metro, train, shipoch tram. Kommaseparerad sträng. |
| LineNumber    | String  | Nej                                      | Max 10 linjer. Kommaseparerad sträng.                                                           |
| SiteId        | Integer | Nej                                      | Id för sökt hållplatsområde.                                                                    |
| FromDate      | String  | Nej default, men Ja om ToDate angivits   | Startdatum för aktuell giltighetsperiod.                                                        |
| ToDate        | String  | Nej default, men Ja om FromDate angivits | Slutdatum för aktuell giltighetsperiod.                                                         |
| Key           | String  | Ja                                       | Din API nyckel. Under mockupdataperioden så kan nyckeln vara vad som helst.                     |

#### Svarsstruktur

| Namn          | Datatyp    | Beskrivning                                                                                             |
|---------------|------------|---------------------------------------------------------------------------------------------------------|
| StatusCode    | Integer    | Innehåller statuskod för det eventuella meddelandet.                                                    |
| Message       | String     | Innehåller eventuellt anropsrelaterade meddelanden som t.ex. felmeddelanden. Se ”Felmeddelanden” nedan. |
| ExecutionTime | long       | Anger hur lång tid (i ms) det tog för servern att generera svaret.                                      |
| ResponseData  | Deviations | Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.                                        |

#### Svarsdata

| Namn                    | Datatyp  | Beskrivning                                                                                                                                                                                    |
|-------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Created                 | DateTime | När ärendet blev publicerad.                                                                                                                                                                   |
| MainNews                | Boolean  | Boolean som indikerar om ärendet är en huvudnyhet.                                                                                                                                             |
| SortOrder               | Integer  | Förslag på sorteringsordning av ärendena. Denna returneras som 1. Är man ute efter sortering på prioritet bör denna tas från Deviationsrawdata och återfinns i svarsstrukturen under priority. |
| Header                  | String   | Rubrik.                                                                                                                                                                                        |
| Details                 | String   | Detaljer, samma som presenteras på webbplatsen för resp. ärende.                                                                                                                               |
| Scope                   | String   | Ett alias för ScopeElements.                                                                                                                                                                   |
| DevCaseGid              | Integer  | Ärendets id.                                                                                                                                                                                   |
| DevMessageVersionNumber | Integer  | Anger aktuell version för ärendet.                                                                                                                                                             |
| ScopeElements           | String   | Beskrivning av vilka linjer eller hållplatser ärendet gäller för.                                                                                                                              |
| FromDateTime            | DateTime | När ärendet börjar vara aktivt.                                                                                                                                                                |
| UpToDateTime            | DateTime | När ärendet slutar att vara aktivt.                                                                                                                                                            |
| Updated                 | DateTime | Senast ärendet blev uppdaterat.                                                                                                                                                                |

### Metod deviationsrawdata

#### URL

`api.sl.se/api2/deviationsrawdata.<FORMAT>?key=<DIN API NYCKEL>&transportMode=<TRANSPORTMODE>&lineNumber=<LINENUMBER>&siteId=<SITEID>`

Om ingen av parametrarna ”TransportMode” och ”LineNumber” skickas med anropet skickas samtliga avvikelser tillbaks som svar.

#### Format

Json eller xml enligt ändelse till serviceanropet.

#### Parametrar

|Namn|Datatyp|Tvingande|Beskrivning|
|--- |--- |--- |--- |
|TransportMode|String|Nej|Aktuella trafikslag. Tillåtna värden är ”bus”, ”metro”, ”train”, "ship"och ”tram”. Kommaseparerad sträng.|
|LineNumber|String|Nej|Max 10 linjer. Kommaseparerad sträng.|
|SiteId|Integer|Nej|Id för sökt hållplatsområde.|
|Key|String|Ja|Din API nyckel. Under mockupdataperioden så kan nyckeln vara vad som helst.|

#### Svarsstruktur

| Namn          | Datatyp    | Beskrivning                                                                                             |
|---------------|------------|---------------------------------------------------------------------------------------------------------|
| StatusCode    | Integer    | Innehåller statuskod för det eventuella meddelandet.                                                    |
| Message       | String     | Innehåller eventuellt anropsrelaterade meddelanden som t.ex. felmeddelanden. Se ”Felmeddelanden” nedan. |
| ExecutionTime | Long       | Anger hur lång tid (i ms) det tog för servern att generera svaret.                                      |
| ResponseData  | Deviations | Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.                                        |

#### Svarsdata

| Namn                    | Datatyp  | Beskrivning                                                      |
|-------------------------|----------|------------------------------------------------------------------|
| Created                 | DateTime | När ärendet blev publicerad.                                     |
| MainNews                | Boolean  | Boolean som indikerar om ärendet är en huvudnyhet.               |
| SortOrder               | Integer  | Förslag på sorteringsordning av ärendena.                        |
| Header                  | String   | Rubrik.                                                          |
| Details                 | String   | Detaljer, samma som presenteras på webbplatsen för resp. ärende. |
| Scope                   | String   | Ett beskrivande alias för ScopeElements.                         |
| DevCaseGid              | Integer  | Ärendets id.                                                     |
| DevMessageVersionNumber | Integer  | Anger aktuell version för ärendet.                               |
| ScopeElements           | String   | Uppräkning av vilka linjer eller hållplatser ärendet gäller för. |
| FromDateTime            | DateTime | När ärendet börjar vara aktivt.                                  |
| UpToDateTime            | DateTime | När ärendet slutar att vara aktivt.                              |
| Updated                 | DateTime | Senast ärendet blev uppdaterat.                                  |
| Priority                | Integer  | Prioriteringsordning för ärendet.                                |
| LineNumber              | String   | Linje där ärendet är gällande.                                   |
| SiteId                  | String   | Id för hållplatsområde. Kan vara tom.                            |
| TransportMode           | String   | Trafikslag för ärendet.                                          |

#### Felmeddelanden

| Statuskod | Meddelande                                                                                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| 1001      | problem with request: Key is undefined.Nyckel hare ej skickats med.                                                                |
| 1002      | problem with request: Key is invalid. Nyckel är ogiltig                                                                            |
| 1003      | Invalid api. Ogiltigt api                                                                                                          |
| 1004      | problem with request: This api is currently not available for keys with priority above 2                                           |
| 1005      | Nyckel finns, men ej för detta api. problem with request: Invalid api for key                                                      |
| 1006      | To many requests per minute. För många anrop per minut, för den profil som används                                                 |
| 1007      | To many requests per month. För många anrop per månad, för den profil som används                                                  |
| 4002      | Fråndatum angett utan tilldatum. Båda datumen måste vara angivna vid filtrering på datum.                                          |
| 4002      | Tilldatum angett utan fråndatum. Båda datumen måste vara angivna vid filtrering på datum.                                          |
| 5000      | Ogiltigt formaterad parameter.Serverfel, var god försök lite senare. Ogiltigt formaterat datum, datumet ska formateras YYYY-MM-DD. |

### Support

Räcker inte dokumentationen så [sök gärna bland alla de hundratals 
inlägg som finns på vårt supportforum](https://kundo.se/org/trafiklabse/posts/). Det är troligt att någon redan har 
hittat och löst samma problem som du har.

Hittar du fortfarande inte svar på din fråga så [skriv ett eget inlägg på forumet](https://kundo.se/org/trafiklabse/) 
så hjälper vi dig.
