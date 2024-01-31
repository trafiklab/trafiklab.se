---
title: SL Realtidsinformation 4
weight: 200
date: 2016-11-30

---

{{% error %}}
Denna API kommer stängas ned vid slutet av mars 2024. Den ersätts av [SLs nya network API](sl-network.md).
{{% /error %}}

## Beskrivning

Realtidsinformation gällande buss, tunnelbana, pendeltåg och lokalbana.

## URL

`https://api.sl.se/api2/realtimedeparturesV4.<FORMAT>?key=<DIN API NYCKEL>&siteid=<SITEID>&timewindow=<TIMEWINDOW>`

### API-nyckelnivåer

| Nivå     | Max anrop/minut | Max anrop/månad |
|----------|-----------------|-----------------|
| Brons    | 30              | 10 000          |
| Silver   | 60              | 500 000         |
| Silver + | 60              | 1 500 000       |
| Guld     |                 | 10 000 000      |
| Guld +   |                 | 30 000 000      |
| Platina  |                 | Efter behov     |

## Format

Json eller xml enligt ändelse till serviceanropet.

## Parametrar

| Parametrar       | Datatyp | Tvingande | Beskrivning                                                                                                                                           |
|------------------|---------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format           | String  | Ja        | Format på svarsdatat. Giltiga värden är “json” eller “xml”.                                                                                           |
| SiteId           | Integer | Ja        | Unikt identifikationsnummer för den plats som aktuella avgångar skall hämtas för, t.ex. 9192 för Slussen. Detta id fås från tjänsten SL Platsuppslag. |
| TimeWindow       | Integer | Ja        | Hämta avgångar inom önskat tidsfönster. Där tidsfönstret är antalet minuter från och med nu. Max 60.                                                  |
| Key              | String  | Ja        | En giltig API-nyckel.                                                                                                                                 |
| Bus              | Boolean | Nej       | Default = true. Om false, så exkluderas trafikslaget från svaret.                                                                                     |
| Metro            | Boolean | Nej       | Default = true. Om false, så exkluderas trafikslaget från svaret.                                                                                     |
| Train            | Boolean | Nej       | Default = true. Om false, så exkluderas trafikslaget från svaret.                                                                                     |
| Tram             | Boolean | Nej       | Default = true. Om false, så exkluderas trafikslaget från svaret.                                                                                     |
| Ship             | Boolean | Nej       | Default = false. Om true inkluderas information om osäker prognos.                                                                                    |
| EnablePrediction | Boolean | Nej       | Default = true. Om false, så exkluderas trafikslaget från svaret.                                                                                     |

## Resultat

Resultat från realtidssökning. Vid xml-format är rotelementets namn ResponseOfDepartures.

### Svarsstruktur

| Namn          | Datatyp   | Beskrivning                                                                                             |
|---------------|-----------|---------------------------------------------------------------------------------------------------------|
| StatusCode    | Integer   | Innehåller statuskod för det eventuella meddelandet.                                                    |
| Message       | String    | Innehåller eventuellt anropsrelaterade meddelanden som t.ex. felmeddelanden. Se ”Felmeddelanden” nedan. |
| ExecutionTime | Long      | Anger hur lång tid (i ms) det tog för servern att generera svaret.                                      |
| ResponseData  | Departure | Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.                                        |

### Svarsdata/ResponseData

| Namn                | Datatyp  | Beskrivning                                                                                                               |
|---------------------|----------|---------------------------------------------------------------------------------------------------------------------------|
| LatestUpdate        | DateTime | Anger när realtidsinformationen (DPS) senast uppdaterades.                                                                |
| DataAge             | Integer  | Antal sekunder sedan tidsstämpeln LatestUpdate.                                                                           |
| Buses               | List     | Lista över samtliga bussavgångar för givet siteId, se svarsstruktur.                                                      |
| Metros              | List     | Lista över samtliga tunnelbaneavgångar för givet siteId, se svarsstruktur.                                                |
| Trains              | List     | Lista över samtliga pendeltågsavgångar för givet siteId, se svarsstruktur.                                                |
| Trams               | List     | Lista över samtliga lokalbaneavgångar för givet siteId, se svarsstruktur.                                                 |
| Ships               | List     | Lista över samtliga båtavgångar för givet siteId, se svarsstruktur.                                                       |
| StopPointDeviations | List     | Lista över hållplatsområdesspecifika avvikelser/störningar. D.v.s. störningar som inte är knutna till en specifik avgång. |

#### Departure

| Namn                     | Datatyp  | Beskrivning                                                                                                                                                                                                                                                                                                           |
|--------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TransportMode            | String   | Trafikslag: ”BUS”,"METRO", ”TRAIN”, ”TRAM” eller ”SHIP”.                                                                                                                                                                                                                                                              |
| LineNumber               | String   | Linjebeteckning/nummer.                                                                                                                                                                                                                                                                                               |
| Destination              | String   | Namn på linjens ändhållplats.                                                                                                                                                                                                                                                                                         |
| JourneyDirection         | Integer  | Reseriktnings-id. 0 vid okänd riktning, annars 1 eller 2.                                                                                                                                                                                                                                                             |
| GroupOfLine              | String   | För buss: Anger om det är en blå buss. Om det är en blå buss står det ”blåbuss”, annars saknas elementet(xml) eller är null(json). För lokalbana: Linjegrupp, t.ex. “Tvärbanan” eller “Roslagsbanan”. För tunnelbana: Linjegruppering. Röd/grön/blå linje. För båt: Anger om det är pendlarbåt eller Waxholmsbolaget. |
| StopAreaName             | String   | Hållplatsnamn.                                                                                                                                                                                                                                                                                                        |
| StopAreaNumber           | Integer  | Id för aktuell hållplats. Tunnelbana före övergång: 0.                                                                                                                                                                                                                                                                |
| StopPointNumber          | Integer  | Id för aktuellt stoppställe. Tunnelbana före övergång: 0.                                                                                                                                                                                                                                                             |
| StopPointDesignation     | String   | Ytterligare identifierare för stoppställe, t.ex. bokstav för busskur eller spår för pendeltåg.                                                                                                                                                                                                                        |
| TimeTabledDateTime       | DateTime | Avgångstid enligt tidtabell.                                                                                                                                                                                                                                                                                          |
| ExpectedDateTime         | DateTime | Förväntad avgångstid. Om det finns tillhörande störning med tillräckligt hög prioritet så kan denna ha null/tomt värde. Detta fram till ett par minuter innan avgång.                                                                                                                                                 |
| DisplayTime              | String   | Avgångstid för presentation. Kan anta formaten x min, HH:mm eller Nu. Om det finns tillhörande störning med tillräckligt hög prioritet så kan denna ha värdet ”-”. Detta fram till ett par minuter innan avgång.                                                                                                      |
| JourneyNumber            | Integer  | Turnummer för avgången.                                                                                                                                                                                                                                                                                               |
| Deviations               | List     | Innehåller typen ”Deviation” nedan. Denna kan vara tom, eller innehålla 1 till flera avvikelser.                                                                                                                                                                                                                      |
| SecondaryDestinationName | String   | Finns bara för: Pendeltåg. Namn på delmål.                                                                                                                                                                                                                                                                            |
| PredictionState          | String   | Kan ha tre olika värden, NORMAL, UNRELIABLE, UNKNOWN. UNRELIABLE betecknar en osäker prognos. Namn på delmål.                                                                                                                                                                                                         |

#### Deviation

| Namn            | Datatyp | Beskrivning                                                            |
|-----------------|---------|------------------------------------------------------------------------|
| Consequence     | String  | Konsekvensbeskrivning för aktuell avvikelse.                           |
| ImportanceLevel | Integer | Signifikationsnivå för aktuell avvikelse. 0-9 där 9 är mest allvarlig. |
| Text            | String  | Beskrivning av aktuell avvikelse.                                      |

#### StopPointDeviations

| Namn      | Datatyp   | Beskrivning                            |
|-----------|-----------|----------------------------------------|
| StopInfo  | StopInfo  | StopInfo. Kan vara tom. Se StopInfo    |
| Deviation | Deviation | Deviation. Kan vara tom. Se Deviation. |

#### StopInfo

| Namn           | Datatyp | Beskrivning                                                                                                                                                                                                 |
|----------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GroupOfLine    | String  | Om TransportMode är ”TRAM” så innehåller noden något av följande värden: ”Lidingöbanan”, ”Nockebybanan”, ”Roslagsbanan”, ”Saltsjöbanan”, ”Spårväg City”, ”Tvärbanan”. Annars blankt (kan komma att ändras). |
| StopAreaName   | String  | Namn på hållplatsen som avvikelsen gäller.                                                                                                                                                                  |
| StopAreaNumber | Integer | Id för hållplatsen som avvikelsen gäller. Är noll om TransportMode inte är BUS.                                                                                                                             |
| TransportMode  | String  | ”METRO”, ”BUS”, ”TRAIN”, ”TRAM” eller ospecificerat.                                                                                                                                                        |

## Felmeddelanden

| Statuskod | Meddelande                                                                                                                                                                           |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1001      | Nyckel har ej skickats med.                                                                                                                                                          |
| 1002      | Nyckel är ogiltig                                                                                                                                                                    |
| 1003      | Ogiltigt api                                                                                                                                                                         |
| 1004      | problem with request: This api is currently not available for keys with priority above 2                                                                                             |
| 1005      | Nyckel finns, men ej för detta api                                                                                                                                                   |
| 1006      | För många anrop per minut, för den profil som används                                                                                                                                |
| 1007      | För många anrop per månad, för den profil som används                                                                                                                                |
| 4001      | SiteId måste gå att konvertera till heltal.                                                                                                                                          |
| 5321      | Kunde varken hämta information från TPI (tunnelbanan) eller DPS (övriga trafikslag).                                                                                                 |
| 5322      | Kunde inte hämta information från DPS.                                                                                                                                               |
| 5323      | Kunde inte hämta information från TPI.                                                                                                                                               |
| 5324      | Kunde varken hämta information från TPI (tunnelbanan) eller DPS (övriga trafikslag) p.g.a. inaktuell DPS-data. Detta uppstår om DPS-datan är äldre än 2 minuter vid svarstillfället. |

## Support

Räcker inte dokumentationen så [sök gärna bland alla de hundratals inlägg som finns på vårt supportforum](https://kundo.se/org/trafiklabse/posts/). Det är
troligt att någon redan har hittat och löst samma problem som du har.

Hittar du fortfarande inte svar på din fråga så[skriv ett eget inlägg på forumet](https://kundo.se/org/trafiklabse/)så hjälper vi dig.
